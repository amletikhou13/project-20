"""Модель предметной области: запись в медицинской карте."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class RecordEntry:
    id: int
    appointment_id: int
    diagnosis: str
    complaints: Optional[str] = None
    prescriptions: Optional[str] = None
