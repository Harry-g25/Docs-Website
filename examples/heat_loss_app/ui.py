from __future__ import annotations

import csv
import json
import logging
from dataclasses import asdict
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk

from . import db
from .calc import Room as CalcRoom
from .calc import Surface as CalcSurface
from .calc import room_heat_loss_w
from .model import Project, Room, Surface


KINDS = ["wall", "window", "roof", "floor", "door", "other"]


def _float_or_error(raw: str, label: str) -> float:
    try:
        return float(raw.strip().replace(",", "."))
    except Exception:
        raise ValueError(f"{label} must be a number")


def _validate_positive(value: float, label: str) -> None:
    if value <= 0:
        raise ValueError(f"{label} must be > 0")


class HeatLossApp(ttk.Frame):
    def __init__(self, master: tk.Tk, db_path: Path) -> None:
        super().__init__(master)
        self.db_path = db_path
        self.conn = db.connect(db_path)

        self.projects: list[Project] = []
        self.rooms: list[Room] = []
        self.surfaces: list[Surface] = []

        master.title("Heat Loss Calculator (Stdlib Example)")
        master.geometry("980x560")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_toolbar()
        self._build_body()
        self._refresh_all()

    # ---- UI ----

    def _build_toolbar(self) -> None:
        bar = ttk.Frame(self)
        bar.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        bar.columnconfigure(12, weight=1)

        ttk.Label(bar, text="Project:").grid(row=0, column=0, sticky="w")
        self.project_var = tk.StringVar(value="")
        self.project_combo = ttk.Combobox(bar, textvariable=self.project_var, state="readonly", width=28)
        self.project_combo.grid(row=0, column=1, sticky="w", padx=(6, 12))
        self.project_combo.bind("<<ComboboxSelected>>", lambda _e: self._on_project_selected())

        ttk.Button(bar, text="New", command=self._new_project).grid(row=0, column=2, sticky="w")
        ttk.Button(bar, text="Delete", command=self._delete_project).grid(row=0, column=3, sticky="w", padx=(6, 12))

        ttk.Label(bar, text="ΔT (K):").grid(row=0, column=4, sticky="w")
        self.delta_t_var = tk.StringVar(value="20")
        ttk.Entry(bar, textvariable=self.delta_t_var, width=8).grid(row=0, column=5, sticky="w", padx=(6, 12))
        ttk.Button(bar, text="Save ΔT", command=self._save_delta_t).grid(row=0, column=6, sticky="w")

        ttk.Button(bar, text="Summary", command=self._open_summary).grid(row=0, column=7, sticky="w", padx=(18, 6))
        ttk.Button(bar, text="Export JSON", command=self._export_json).grid(row=0, column=8, sticky="w", padx=(18, 6))
        ttk.Button(bar, text="Export CSV", command=self._export_csv).grid(row=0, column=9, sticky="w")
        ttk.Button(bar, text="Export Report", command=self._export_report).grid(row=0, column=10, sticky="w", padx=(6, 0))

    def _build_body(self) -> None:
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.grid(row=1, column=0, sticky="nsew")

        left = ttk.Frame(paned)
        right = ttk.Frame(paned)
        left.columnconfigure(0, weight=1)
        left.rowconfigure(1, weight=1)
        right.columnconfigure(0, weight=1)
        right.rowconfigure(2, weight=1)

        paned.add(left, weight=1)
        paned.add(right, weight=3)

        # Rooms
        room_head = ttk.Frame(left)
        room_head.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        ttk.Label(room_head, text="Rooms", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Button(room_head, text="Add", command=self._add_room).grid(row=0, column=1, sticky="e", padx=(6, 0))
        ttk.Button(room_head, text="Edit", command=self._edit_room).grid(row=0, column=2, sticky="e", padx=(6, 0))
        ttk.Button(room_head, text="Delete", command=self._delete_room).grid(row=0, column=3, sticky="e", padx=(6, 0))
        room_head.columnconfigure(0, weight=1)

        self.room_list = tk.Listbox(left, height=10)
        self.room_list.grid(row=1, column=0, sticky="nsew")
        self.room_list.bind("<<ListboxSelect>>", lambda _e: self._on_room_selected())

        # Right: room settings + totals + surfaces
        top = ttk.Frame(right)
        top.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        top.columnconfigure(6, weight=1)

        ttk.Label(top, text="Selected room:").grid(row=0, column=0, sticky="w")
        self.room_name_var = tk.StringVar(value="")
        ttk.Label(top, textvariable=self.room_name_var, font=("Segoe UI", 10, "bold")).grid(row=0, column=1, sticky="w", padx=(6, 12))

        ttk.Label(top, text="Volume (m³):").grid(row=0, column=2, sticky="w")
        self.room_volume_var = tk.StringVar(value="")
        ttk.Entry(top, textvariable=self.room_volume_var, width=10).grid(row=0, column=3, sticky="w", padx=(6, 12))

        ttk.Label(top, text="ACH:").grid(row=0, column=4, sticky="w")
        self.room_ach_var = tk.StringVar(value="")
        ttk.Entry(top, textvariable=self.room_ach_var, width=10).grid(row=0, column=5, sticky="w", padx=(6, 12))

        ttk.Button(top, text="Save room", command=self._save_room_quick).grid(row=0, column=6, sticky="w")

        totals = ttk.Frame(right)
        totals.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        totals.columnconfigure(0, weight=1)
        self.total_var = tk.StringVar(value="")
        ttk.Label(totals, textvariable=self.total_var).grid(row=0, column=0, sticky="w")

        surf_head = ttk.Frame(right)
        surf_head.grid(row=2, column=0, sticky="ew", pady=(0, 6))
        surf_head.columnconfigure(0, weight=1)
        ttk.Label(surf_head, text="Surfaces", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Button(surf_head, text="Add", command=self._add_surface).grid(row=0, column=1, sticky="e", padx=(6, 0))
        ttk.Button(surf_head, text="Edit", command=self._edit_surface).grid(row=0, column=2, sticky="e", padx=(6, 0))
        ttk.Button(surf_head, text="Delete", command=self._delete_surface).grid(row=0, column=3, sticky="e", padx=(6, 0))

        cols = ("kind", "name", "area_m2", "u_value")
        self.surface_tree = ttk.Treeview(right, columns=cols, show="headings", height=12)
        self.surface_tree.heading("kind", text="Type")
        self.surface_tree.heading("name", text="Name")
        self.surface_tree.heading("area_m2", text="Area (m²)")
        self.surface_tree.heading("u_value", text="U (W/m²K)")
        self.surface_tree.column("kind", width=110, anchor="w")
        self.surface_tree.column("name", width=240, anchor="w")
        self.surface_tree.column("area_m2", width=120, anchor="e")
        self.surface_tree.column("u_value", width=120, anchor="e")
        self.surface_tree.grid(row=3, column=0, sticky="nsew")
        right.rowconfigure(3, weight=1)

        y = ttk.Scrollbar(right, orient="vertical", command=self.surface_tree.yview)
        self.surface_tree.configure(yscrollcommand=y.set)
        y.grid(row=3, column=1, sticky="ns")

    # ---- Data refresh ----

    def _refresh_all(self) -> None:
        self.projects = db.list_projects(self.conn)
        self.project_combo["values"] = [p.name for p in self.projects]

        if not self.projects:
            self.project_var.set("")
            self.delta_t_var.set("20")
            self.rooms = []
            self._render_rooms()
            self._clear_room_detail()
            return

        if self.project_var.get() not in {p.name for p in self.projects}:
            self.project_var.set(self.projects[0].name)

        self._on_project_selected()

    def _on_project_selected(self) -> None:
        proj = self._selected_project()
        if not proj:
            return
        self.delta_t_var.set(str(proj.delta_t_k))
        self.rooms = db.list_rooms(self.conn, proj.id)
        self._render_rooms()
        if self.rooms:
            self.room_list.selection_set(0)
            self._on_room_selected()
        else:
            self._clear_room_detail()

    def _render_rooms(self) -> None:
        self.room_list.delete(0, tk.END)
        proj = self._selected_project()
        delta_t_k = proj.delta_t_k if proj else None
        for r in self.rooms:
            if delta_t_k is None:
                label = r.name
            else:
                surfaces = db.list_surfaces(self.conn, r.id)
                _q_cond, _q_vent, q_total = self._room_totals(r, surfaces, delta_t_k)
                label = f"{r.name}  —  {q_total:.1f} W"

            self.room_list.insert(tk.END, label)

    def _on_room_selected(self) -> None:
        room = self._selected_room()
        if not room:
            self._clear_room_detail()
            return

        self.room_name_var.set(room.name)
        self.room_volume_var.set(str(room.volume_m3))
        self.room_ach_var.set(str(room.ach))

        self.surfaces = db.list_surfaces(self.conn, room.id)
        self._render_surfaces()
        self._render_totals()

    def _render_surfaces(self) -> None:
        for item in self.surface_tree.get_children():
            self.surface_tree.delete(item)
        for s in self.surfaces:
            self.surface_tree.insert(
                "",
                "end",
                iid=str(s.id),
                values=(s.kind, s.name, f"{s.area_m2:.3f}", f"{s.u_value_w_m2k:.3f}"),
            )

    def _render_totals(self) -> None:
        room = self._selected_room()
        proj = self._selected_project()
        if not room or not proj:
            self.total_var.set("")
            return

        calc_room = CalcRoom(name=room.name, volume_m3=room.volume_m3, ach=room.ach)
        calc_surfaces = [
            CalcSurface(name=s.name, kind=s.kind, area_m2=s.area_m2, u_value_w_m2k=s.u_value_w_m2k)
            for s in self.surfaces
        ]
        q_cond, q_vent, q_total = room_heat_loss_w(calc_room, calc_surfaces, proj.delta_t_k)
        self.total_var.set(
            f"Conduction: {q_cond:.1f} W    Ventilation: {q_vent:.1f} W    Total: {q_total:.1f} W"
        )

    def _clear_room_detail(self) -> None:
        self.room_name_var.set("")
        self.room_volume_var.set("")
        self.room_ach_var.set("")
        self.total_var.set("")
        for item in self.surface_tree.get_children():
            self.surface_tree.delete(item)

    def _room_totals(self, room: Room, surfaces: list[Surface], delta_t_k: float) -> tuple[float, float, float]:
        calc_room = CalcRoom(name=room.name, volume_m3=room.volume_m3, ach=room.ach)
        calc_surfaces = [
            CalcSurface(name=s.name, kind=s.kind, area_m2=s.area_m2, u_value_w_m2k=s.u_value_w_m2k)
            for s in surfaces
        ]
        return room_heat_loss_w(calc_room, calc_surfaces, delta_t_k)

    def _open_summary(self) -> None:
        proj = self._selected_project()
        if not proj:
            return

        win = tk.Toplevel(self)
        win.title("Project summary")
        win.geometry("860x420")
        win.transient(self.winfo_toplevel())

        outer = ttk.Frame(win, padding=10)
        outer.pack(fill="both", expand=True)
        outer.columnconfigure(0, weight=1)
        outer.rowconfigure(1, weight=1)

        ttk.Label(
            outer,
            text=f"Project: {proj.name}    ΔT: {proj.delta_t_k} K",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        cols = ("room", "volume", "ach", "q_cond", "q_vent", "q_total")
        tree = ttk.Treeview(outer, columns=cols, show="headings", height=12)
        tree.heading("room", text="Room")
        tree.heading("volume", text="Volume (m³)")
        tree.heading("ach", text="ACH")
        tree.heading("q_cond", text="Conduction (W)")
        tree.heading("q_vent", text="Ventilation (W)")
        tree.heading("q_total", text="Total (W)")
        tree.column("room", width=220, anchor="w")
        tree.column("volume", width=110, anchor="e")
        tree.column("ach", width=80, anchor="e")
        tree.column("q_cond", width=140, anchor="e")
        tree.column("q_vent", width=140, anchor="e")
        tree.column("q_total", width=140, anchor="e")
        tree.grid(row=1, column=0, sticky="nsew")

        y = ttk.Scrollbar(outer, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=y.set)
        y.grid(row=1, column=1, sticky="ns")

        q_cond_all = 0.0
        q_vent_all = 0.0
        q_total_all = 0.0

        for room in self.rooms:
            surfaces = db.list_surfaces(self.conn, room.id)
            q_cond, q_vent, q_total = self._room_totals(room, surfaces, proj.delta_t_k)
            q_cond_all += q_cond
            q_vent_all += q_vent
            q_total_all += q_total

            tree.insert(
                "",
                "end",
                iid=str(room.id),
                values=(
                    room.name,
                    f"{room.volume_m3:.2f}",
                    f"{room.ach:.2f}",
                    f"{q_cond:.1f}",
                    f"{q_vent:.1f}",
                    f"{q_total:.1f}",
                ),
            )

        total = ttk.Frame(outer)
        total.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        total.columnconfigure(0, weight=1)
        ttk.Label(
            total,
            text=(
                f"Totals: Conduction {q_cond_all:.1f} W    "
                f"Ventilation {q_vent_all:.1f} W    "
                f"Grand Total {q_total_all:.1f} W"
            ),
        ).grid(row=0, column=0, sticky="w")
        ttk.Button(total, text="Close", command=win.destroy).grid(row=0, column=1, sticky="e")

    # ---- Helpers ----

    def _selected_project(self) -> Project | None:
        name = self.project_var.get().strip()
        for p in self.projects:
            if p.name == name:
                return p
        return None

    def _selected_room(self) -> Room | None:
        sel = self.room_list.curselection()
        if not sel:
            return None
        idx = sel[0]
        if idx < 0 or idx >= len(self.rooms):
            return None
        return self.rooms[idx]

    def _selected_surface(self) -> Surface | None:
        sel = self.surface_tree.selection()
        if not sel:
            return None
        sid = int(sel[0])
        for s in self.surfaces:
            if s.id == sid:
                return s
        return None

    # ---- Project actions ----

    def _new_project(self) -> None:
        name = simpledialog.askstring("New project", "Project name:", parent=self)
        if not name:
            return
        name = name.strip()

        delta_raw = simpledialog.askstring("ΔT", "Default ΔT (K):", initialvalue="20", parent=self)
        if delta_raw is None:
            return

        try:
            dt = _float_or_error(delta_raw, "ΔT")
            _validate_positive(dt, "ΔT")
            db.create_project(self.conn, name, dt)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)
            return

        self.project_var.set(name)
        self._refresh_all()

    def _delete_project(self) -> None:
        proj = self._selected_project()
        if not proj:
            return
        if not messagebox.askyesno("Delete project", f"Delete project '{proj.name}'?", parent=self):
            return
        db.delete_project(self.conn, proj.id)
        self._refresh_all()

    def _save_delta_t(self) -> None:
        proj = self._selected_project()
        if not proj:
            return
        try:
            dt = _float_or_error(self.delta_t_var.get(), "ΔT")
            _validate_positive(dt, "ΔT")
            db.update_project_delta_t(self.conn, proj.id, dt)
            self._refresh_all()
        except Exception as e:
            messagebox.showerror("Invalid input", str(e), parent=self)

    # ---- Room actions ----

    def _add_room(self) -> None:
        proj = self._selected_project()
        if not proj:
            messagebox.showinfo("No project", "Create a project first.", parent=self)
            return

        result = self._room_form("New room")
        if not result:
            return

        try:
            name, vol, ach = result
            db.create_room(self.conn, proj.id, name, vol, ach)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)
            return

        self._on_project_selected()

    def _edit_room(self) -> None:
        room = self._selected_room()
        if not room:
            return

        result = self._room_form("Edit room", existing=room)
        if not result:
            return

        try:
            name, vol, ach = result
            db.update_room(self.conn, room.id, name, vol, ach)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)
            return

        self._on_project_selected()

    def _save_room_quick(self) -> None:
        room = self._selected_room()
        if not room:
            return

        try:
            vol = _float_or_error(self.room_volume_var.get(), "Volume")
            _validate_positive(vol, "Volume")
            ach = _float_or_error(self.room_ach_var.get(), "ACH")
            if ach < 0:
                raise ValueError("ACH must be >= 0")

            db.update_room(self.conn, room.id, room.name, vol, ach)
            self._on_project_selected()
        except Exception as e:
            messagebox.showerror("Invalid input", str(e), parent=self)

    def _delete_room(self) -> None:
        room = self._selected_room()
        if not room:
            return
        if not messagebox.askyesno("Delete room", f"Delete room '{room.name}'?", parent=self):
            return
        db.delete_room(self.conn, room.id)
        self._on_project_selected()

    # ---- Surface actions ----

    def _room_form(self, title: str, existing: Room | None = None) -> tuple[str, float, float] | None:
        win = tk.Toplevel(self)
        win.title(title)
        win.transient(self.winfo_toplevel())
        win.grab_set()
        win.resizable(False, False)

        frame = ttk.Frame(win, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(1, weight=1)

        name_var = tk.StringVar(value=(existing.name if existing else ""))
        vol_var = tk.StringVar(value=(str(existing.volume_m3) if existing else "50"))
        ach_var = tk.StringVar(value=(str(existing.ach) if existing else "0.5"))

        ttk.Label(frame, text="Room name:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        name_entry = ttk.Entry(frame, textvariable=name_var, width=34)
        name_entry.grid(row=0, column=1, sticky="ew", pady=(0, 6))

        ttk.Label(frame, text="Volume (m³):").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        ttk.Entry(frame, textvariable=vol_var, width=16).grid(row=1, column=1, sticky="w", pady=(0, 6))

        ttk.Label(frame, text="ACH:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        ttk.Entry(frame, textvariable=ach_var, width=16).grid(row=2, column=1, sticky="w", pady=(0, 6))

        result: dict[str, object] = {"value": None}

        def on_ok() -> None:
            try:
                name = name_var.get().strip()
                if not name:
                    raise ValueError("Room name is required")

                vol = _float_or_error(vol_var.get(), "Volume")
                _validate_positive(vol, "Volume")

                ach = _float_or_error(ach_var.get(), "ACH")
                if ach < 0:
                    raise ValueError("ACH must be >= 0")

                result["value"] = (name, vol, ach)
                win.destroy()
            except Exception as e:
                messagebox.showerror("Invalid input", str(e), parent=win)

        def on_cancel() -> None:
            win.destroy()

        btns = ttk.Frame(frame)
        btns.grid(row=3, column=0, columnspan=2, sticky="e", pady=(10, 0))
        ttk.Button(btns, text="Cancel", command=on_cancel).grid(row=0, column=0, padx=(0, 6))
        ttk.Button(btns, text="OK", command=on_ok).grid(row=0, column=1)

        name_entry.focus_set()
        win.bind("<Return>", lambda _e: on_ok())
        win.bind("<Escape>", lambda _e: on_cancel())

        self.wait_window(win)
        return result["value"]  # type: ignore[return-value]

    def _surface_form(self, title: str, existing: Surface | None = None) -> tuple[str, str, float, float] | None:
        win = tk.Toplevel(self)
        win.title(title)
        win.transient(self.winfo_toplevel())
        win.grab_set()
        win.resizable(False, False)

        frame = ttk.Frame(win, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(1, weight=1)

        kind_var = tk.StringVar(value=(existing.kind if existing else "wall"))
        name_var = tk.StringVar(value=(existing.name if existing else ""))
        area_var = tk.StringVar(value=(str(existing.area_m2) if existing else "10"))
        u_var = tk.StringVar(value=(str(existing.u_value_w_m2k) if existing else "0.3"))

        ttk.Label(frame, text="Type:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        kind_combo = ttk.Combobox(frame, textvariable=kind_var, values=KINDS, state="readonly", width=14)
        kind_combo.grid(row=0, column=1, sticky="w", pady=(0, 6))

        ttk.Label(frame, text="Name:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        name_entry = ttk.Entry(frame, textvariable=name_var, width=34)
        name_entry.grid(row=1, column=1, sticky="ew", pady=(0, 6))

        ttk.Label(frame, text="Area (m²):").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        ttk.Entry(frame, textvariable=area_var, width=16).grid(row=2, column=1, sticky="w", pady=(0, 6))

        ttk.Label(frame, text="U-value (W/m²K):").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
        ttk.Entry(frame, textvariable=u_var, width=16).grid(row=3, column=1, sticky="w", pady=(0, 6))

        result: dict[str, object] = {"value": None}

        def on_ok() -> None:
            try:
                kind = kind_var.get().strip().lower() or "wall"
                if kind not in KINDS:
                    raise ValueError(f"Type must be one of: {', '.join(KINDS)}")

                name = name_var.get().strip()
                if not name:
                    raise ValueError("Name is required")

                area = _float_or_error(area_var.get(), "Area")
                _validate_positive(area, "Area")

                u = _float_or_error(u_var.get(), "U-value")
                _validate_positive(u, "U-value")

                result["value"] = (kind, name, area, u)
                win.destroy()
            except Exception as e:
                messagebox.showerror("Invalid input", str(e), parent=win)

        def on_cancel() -> None:
            win.destroy()

        btns = ttk.Frame(frame)
        btns.grid(row=4, column=0, columnspan=2, sticky="e", pady=(10, 0))
        ttk.Button(btns, text="Cancel", command=on_cancel).grid(row=0, column=0, padx=(0, 6))
        ttk.Button(btns, text="OK", command=on_ok).grid(row=0, column=1)

        if not existing:
            kind_combo.current(0)
        name_entry.focus_set()
        win.bind("<Return>", lambda _e: on_ok())
        win.bind("<Escape>", lambda _e: on_cancel())

        self.wait_window(win)
        return result["value"]  # type: ignore[return-value]

    def _add_surface(self) -> None:
        room = self._selected_room()
        if not room:
            messagebox.showinfo("No room", "Select or create a room first.", parent=self)
            return
        try:
            result = self._surface_form("Add surface")
            if not result:
                return
            kind, name, area, u = result
            db.create_surface(self.conn, room.id, kind, name, area, u)
            self._on_room_selected()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)

    def _edit_surface(self) -> None:
        s = self._selected_surface()
        if not s:
            return
        try:
            result = self._surface_form("Edit surface", existing=s)
            if not result:
                return
            kind, name, area, u = result
            db.update_surface(self.conn, s.id, kind, name, area, u)
            self._on_room_selected()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self)

    def _delete_surface(self) -> None:
        s = self._selected_surface()
        if not s:
            return
        if not messagebox.askyesno("Delete surface", f"Delete '{s.name}'?", parent=self):
            return
        db.delete_surface(self.conn, s.id)
        self._on_room_selected()

    # ---- Export ----

    def _export_json(self) -> None:
        proj = self._selected_project()
        if not proj:
            return
        path = filedialog.asksaveasfilename(
            title="Export JSON",
            defaultextension=".json",
            filetypes=[("JSON", "*.json")],
        )
        if not path:
            return

        payload = {
            "project": asdict(proj),
            "rooms": [asdict(r) for r in self.rooms],
            "surfaces": [asdict(s) for r in self.rooms for s in db.list_surfaces(self.conn, r.id)],
        }
        Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        messagebox.showinfo("Export", f"Wrote {path}", parent=self)

    def _export_csv(self) -> None:
        proj = self._selected_project()
        if not proj:
            return
        path = filedialog.asksaveasfilename(
            title="Export CSV",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
        )
        if not path:
            return

        out = Path(path)
        with out.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["project", "delta_t_k", "room", "volume_m3", "ach", "q_cond_w", "q_vent_w", "q_total_w"])
            for room in self.rooms:
                surfaces = db.list_surfaces(self.conn, room.id)
                calc_room = CalcRoom(name=room.name, volume_m3=room.volume_m3, ach=room.ach)
                calc_surfaces = [
                    CalcSurface(name=s.name, kind=s.kind, area_m2=s.area_m2, u_value_w_m2k=s.u_value_w_m2k)
                    for s in surfaces
                ]
                q_cond, q_vent, q_total = room_heat_loss_w(calc_room, calc_surfaces, proj.delta_t_k)
                w.writerow([proj.name, proj.delta_t_k, room.name, room.volume_m3, room.ach, q_cond, q_vent, q_total])

        messagebox.showinfo("Export", f"Wrote {out}", parent=self)

    def _export_report(self) -> None:
        proj = self._selected_project()
        if not proj:
            return
        path = filedialog.asksaveasfilename(
            title="Export Report",
            defaultextension=".txt",
            filetypes=[("Text", "*.txt")],
        )
        if not path:
            return

        lines: list[str] = []
        lines.append(f"Heat Loss Report")
        lines.append(f"Project: {proj.name}")
        lines.append(f"ΔT: {proj.delta_t_k} K")
        lines.append("")
        lines.append("Assumptions / units")
        lines.append("  - Steady-state heat loss at constant ΔT (K)")
        lines.append("  - Conduction per surface: Q = U (W/m²K) × A (m²) × ΔT (K)")
        lines.append("  - Ventilation (rule of thumb): Q ≈ 0.33 × ACH × V (m³) × ΔT (K)")
        lines.append("  - Results are in Watts (W)")
        lines.append("")

        q_cond_all = 0.0
        q_vent_all = 0.0
        q_total_all = 0.0

        for room in self.rooms:
            surfaces = db.list_surfaces(self.conn, room.id)
            q_cond, q_vent, q_total = self._room_totals(room, surfaces, proj.delta_t_k)
            q_cond_all += q_cond
            q_vent_all += q_vent
            q_total_all += q_total

            lines.append("=" * 72)
            lines.append(f"Room: {room.name}")
            lines.append(f"  Volume: {room.volume_m3:.2f} m³")
            lines.append(f"  ACH:    {room.ach:.2f}")
            lines.append("")
            lines.append("  Surfaces:")

            if not surfaces:
                lines.append("    (none)")
            else:
                for s in surfaces:
                    q_s = s.u_value_w_m2k * s.area_m2 * proj.delta_t_k
                    lines.append(
                        f"    - {s.kind:7s}  {s.name:24.24s}  area={s.area_m2:7.3f} m²  "
                        f"U={s.u_value_w_m2k:6.3f}  Q={q_s:8.1f} W"
                    )

            lines.append("")
            lines.append(f"  Conduction:   {q_cond:8.1f} W")
            lines.append(f"  Ventilation:  {q_vent:8.1f} W")
            lines.append(f"  Total:        {q_total:8.1f} W")
            lines.append("")

        lines.append("=" * 72)
        lines.append(f"Project totals")
        lines.append(f"  Conduction:   {q_cond_all:8.1f} W")
        lines.append(f"  Ventilation:  {q_vent_all:8.1f} W")
        lines.append(f"  Grand total:  {q_total_all:8.1f} W")
        lines.append("")

        Path(path).write_text("\n".join(lines), encoding="utf-8")
        messagebox.showinfo("Export", f"Wrote {path}", parent=self)


def run(db_path: Path) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    root = tk.Tk()
    root.option_add("*tearOff", False)
    ttk.Style().theme_use("clam")
    HeatLossApp(root, db_path=db_path)
    root.mainloop()
