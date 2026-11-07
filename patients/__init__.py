"""Модуль patients: регистрация и поиск пациентов (FR-01)."""
from patients.models import Patient
from patients import service

__all__ = ["Patient", "service"]
