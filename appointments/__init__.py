"""Модуль appointments: запись на приём и отмена (FR-03, FR-04)."""

from appointments import service
from appointments.models import Appointment

__all__ = ["Appointment", "service"]
