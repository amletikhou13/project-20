"""Контракты между модулями: протоколы (PEP 544), по которым модули общаются друг с другом."""
from typing import Optional, Protocol


class PatientDirectory(Protocol):
    """Что модуль appointments требует от модуля patients (реализует patients.service)."""

    def get(self, pid: int) -> dict:
        """Вернуть пациента или выбросить NotFound."""
        ...


class SlotCalendar(Protocol):
    """Что модуль appointments требует от модуля schedule (реализует schedule.service)."""

    def get_slot(self, sid: int) -> Optional[dict]:
        """Вернуть слот или None."""
        ...

    def occupy(self, sid: int) -> None:
        """Пометить слот занятым."""
        ...

    def release(self, sid: int) -> None:
        """Освободить слот."""
        ...
