"""Запись на приём и отмена (FR-03, FR-04; BR-01, BR-04)."""

from datetime import datetime, timedelta

from appointments import repository
from core.contracts import PatientDirectory, SlotCalendar
from core.exceptions import Conflict, NotFound
from patients import service as patients_service
from schedule import service as schedule_service


def book(patient_id, slot_id, patients: PatientDirectory = patients_service, schedule: SlotCalendar = schedule_service):
    """Записать пациента на слот. Соседние модули передаются по контракту (по умолчанию настоящие)."""
    patients.get(patient_id)
    slot = schedule.get_slot(slot_id)
    if not slot:
        raise NotFound("слот не найден")
    if slot["status"] != "free":
        raise Conflict("слот уже занят")
    aid = repository.add(patient_id, slot_id)
    schedule.occupy(slot_id)
    return aid


def cancel(aid, now=None, hours=2, schedule: SlotCalendar = schedule_service):
    a = repository.get(aid)
    if not a:
        raise NotFound("запись не найдена")
    slot = schedule.get_slot(a["slot_id"])
    if slot is None:
        raise NotFound("слот не найден")
    now = now or datetime.now()
    if datetime.fromisoformat(slot["start"]) - now < timedelta(hours=hours):
        raise Conflict("отмена возможна не позднее чем за 2 часа")
    repository.set_status(aid, "cancelled")
    schedule.release(a["slot_id"])
