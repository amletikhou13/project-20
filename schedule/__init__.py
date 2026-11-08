"""Модуль schedule: врачи, специальности, слоты расписания (FR-02, FR-05)."""

from schedule import service
from schedule.models import Doctor, Slot

__all__ = ["Doctor", "Slot", "service"]
