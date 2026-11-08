"""Модуль records: медицинская карта (FR-06) и отчёт (FR-07)."""

from records import service
from records.models import RecordEntry

__all__ = ["RecordEntry", "service"]
