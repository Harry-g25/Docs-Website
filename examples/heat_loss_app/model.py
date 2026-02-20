from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    id: int
    name: str
    delta_t_k: float


@dataclass(frozen=True)
class Room:
    id: int
    project_id: int
    name: str
    volume_m3: float
    ach: float


@dataclass(frozen=True)
class Surface:
    id: int
    room_id: int
    kind: str
    name: str
    area_m2: float
    u_value_w_m2k: float
