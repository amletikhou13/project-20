"""Модуль schedule: врачи, специальности, слоты расписания (FR-02, FR-05)."""
from schedule.models import Doctor, Slot
from schedule import service

__all__ = ["Doctor", "Slot", "service"]
