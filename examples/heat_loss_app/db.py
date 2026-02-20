from __future__ import annotations

import sqlite3
from pathlib import Path

from .model import Project, Room, Surface


SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS project (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  delta_t_k REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS room (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  project_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  volume_m3 REAL NOT NULL,
  ach REAL NOT NULL,
  FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS surface (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  room_id INTEGER NOT NULL,
  kind TEXT NOT NULL,
  name TEXT NOT NULL,
  area_m2 REAL NOT NULL,
  u_value_w_m2k REAL NOT NULL,
  FOREIGN KEY (room_id) REFERENCES room(id) ON DELETE CASCADE
);
"""


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


# ---- Project ----

def list_projects(conn: sqlite3.Connection) -> list[Project]:
    rows = conn.execute("SELECT id, name, delta_t_k FROM project ORDER BY name").fetchall()
    return [Project(id=r["id"], name=r["name"], delta_t_k=float(r["delta_t_k"])) for r in rows]


def create_project(conn: sqlite3.Connection, name: str, delta_t_k: float) -> int:
    cur = conn.execute("INSERT INTO project(name, delta_t_k) VALUES (?, ?)", (name, delta_t_k))
    conn.commit()
    return int(cur.lastrowid)


def update_project_delta_t(conn: sqlite3.Connection, project_id: int, delta_t_k: float) -> None:
    conn.execute("UPDATE project SET delta_t_k = ? WHERE id = ?", (delta_t_k, project_id))
    conn.commit()


def delete_project(conn: sqlite3.Connection, project_id: int) -> None:
    conn.execute("DELETE FROM project WHERE id = ?", (project_id,))
    conn.commit()


# ---- Rooms ----

def list_rooms(conn: sqlite3.Connection, project_id: int) -> list[Room]:
    rows = conn.execute(
        "SELECT id, project_id, name, volume_m3, ach FROM room WHERE project_id = ? ORDER BY name",
        (project_id,),
    ).fetchall()
    return [
        Room(
            id=r["id"],
            project_id=r["project_id"],
            name=r["name"],
            volume_m3=float(r["volume_m3"]),
            ach=float(r["ach"]),
        )
        for r in rows
    ]


def create_room(conn: sqlite3.Connection, project_id: int, name: str, volume_m3: float, ach: float) -> int:
    cur = conn.execute(
        "INSERT INTO room(project_id, name, volume_m3, ach) VALUES (?,?,?,?)",
        (project_id, name, volume_m3, ach),
    )
    conn.commit()
    return int(cur.lastrowid)


def update_room(conn: sqlite3.Connection, room_id: int, name: str, volume_m3: float, ach: float) -> None:
    conn.execute(
        "UPDATE room SET name = ?, volume_m3 = ?, ach = ? WHERE id = ?",
        (name, volume_m3, ach, room_id),
    )
    conn.commit()


def delete_room(conn: sqlite3.Connection, room_id: int) -> None:
    conn.execute("DELETE FROM room WHERE id = ?", (room_id,))
    conn.commit()


# ---- Surfaces ----

def list_surfaces(conn: sqlite3.Connection, room_id: int) -> list[Surface]:
    rows = conn.execute(
        "SELECT id, room_id, kind, name, area_m2, u_value_w_m2k FROM surface WHERE room_id = ? ORDER BY id",
        (room_id,),
    ).fetchall()
    return [
        Surface(
            id=r["id"],
            room_id=r["room_id"],
            kind=r["kind"],
            name=r["name"],
            area_m2=float(r["area_m2"]),
            u_value_w_m2k=float(r["u_value_w_m2k"]),
        )
        for r in rows
    ]


def create_surface(
    conn: sqlite3.Connection,
    room_id: int,
    kind: str,
    name: str,
    area_m2: float,
    u_value_w_m2k: float,
) -> int:
    cur = conn.execute(
        "INSERT INTO surface(room_id, kind, name, area_m2, u_value_w_m2k) VALUES (?,?,?,?,?)",
        (room_id, kind, name, area_m2, u_value_w_m2k),
    )
    conn.commit()
    return int(cur.lastrowid)


def update_surface(conn: sqlite3.Connection, surface_id: int, kind: str, name: str, area_m2: float, u_value_w_m2k: float) -> None:
    conn.execute(
        "UPDATE surface SET kind = ?, name = ?, area_m2 = ?, u_value_w_m2k = ? WHERE id = ?",
        (kind, name, area_m2, u_value_w_m2k, surface_id),
    )
    conn.commit()


def delete_surface(conn: sqlite3.Connection, surface_id: int) -> None:
    conn.execute("DELETE FROM surface WHERE id = ?", (surface_id,))
    conn.commit()
