"""Модель предметной области: пациент."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Patient:
    id: Optional[int]
    full_name: str
    birth_date: str
    phone: Optional[str]
    policy: str
