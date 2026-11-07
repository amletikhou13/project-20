"""Модуль appointments: запись на приём и отмена (FR-03, FR-04)."""
from appointments.models import Appointment
from appointments import service

__all__ = ["Appointment", "service"]
