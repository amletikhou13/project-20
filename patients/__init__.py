"""Модуль patients: регистрация и поиск пациентов (FR-01)."""

from patients import service
from patients.models import Patient

__all__ = ["Patient", "service"]
