from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Surface:
    name: str
    kind: str  # e.g. wall/window/roof/floor
    area_m2: float
    u_value_w_m2k: float


@dataclass(frozen=True)
class Room:
    name: str
    volume_m3: float
    ach: float


def conduction_heat_loss_w(surfaces: list[Surface], delta_t_k: float) -> float:
    return sum(s.u_value_w_m2k * s.area_m2 * delta_t_k for s in surfaces)


def ventilation_heat_loss_w(volume_m3: float, ach: float, delta_t_k: float) -> float:
    # Rule-of-thumb constant:
    # Q(W) ≈ 0.33 * ACH * V(m³) * ΔT(K)
    return 0.33 * ach * volume_m3 * delta_t_k


def room_heat_loss_w(room: Room, surfaces: list[Surface], delta_t_k: float) -> tuple[float, float, float]:
    q_cond = conduction_heat_loss_w(surfaces, delta_t_k)
    q_vent = ventilation_heat_loss_w(room.volume_m3, room.ach, delta_t_k)
    return q_cond, q_vent, q_cond + q_vent
