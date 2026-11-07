"""Модели предметной области: врач и слот расписания."""
from dataclasses import dataclass


@dataclass
class Doctor:
    id: int
    full_name: str
    specialty_id: int


@dataclass
class Slot:
    id: int
    doctor_id: int
    start: str
    status: str = "free"
