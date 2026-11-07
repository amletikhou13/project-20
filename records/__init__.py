"""Модуль records: медицинская карта (FR-06) и отчёт (FR-07)."""
from records.models import RecordEntry
from records import service

__all__ = ["RecordEntry", "service"]
