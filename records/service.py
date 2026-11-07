"""Медицинская карта и отчёт (FR-06, FR-07; BR-05)."""

from core.exceptions import Conflict
from records import repository


def add_entry(appointment_id, complaints, diagnosis, prescriptions):
    if not diagnosis:
        raise Conflict("диагноз обязателен")
    return repository.add(appointment_id, complaints, diagnosis, prescriptions)


def card(patient_id):
    return repository.by_patient(patient_id)


def report():
    return {"приёмов проведено": repository.count_all()}
