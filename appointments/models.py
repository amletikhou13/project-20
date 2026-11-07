"""Модель предметной области: запись на приём."""
from dataclasses import dataclass


@dataclass
class Appointment:
    id: int
    patient_id: int
    slot_id: int
    status: str = "active"
