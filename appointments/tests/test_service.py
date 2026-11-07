"""Тесты модуля appointments: правила записи и отмены (BR-01, BR-04)."""
from datetime import datetime
import pytest
from appointments import service
from patients import service as patients
from schedule import service as schedule
from core.exceptions import Conflict


def _setup():
    p = patients.register("Иванов Иван", "1990-01-01", None, "1")
    sp = schedule.add_specialty("Терапевт")
    d = schedule.add_doctor("Петрова А.А.", sp)
    return p, schedule.add_slot(d, "2026-11-10T09:00")


def test_book_busy_slot_rejected(app):
    p, s = _setup()
    service.book(p, s)
    with pytest.raises(Conflict):
        service.book(p, s)


def test_cancel_too_late(app):
    p, s = _setup()
    a = service.book(p, s)
    with pytest.raises(Conflict):
        service.cancel(a, now=datetime(2026, 11, 10, 8, 0))


def test_cancel_in_time_frees_slot(app):
    p, s = _setup()
    a = service.book(p, s)
    service.cancel(a, now=datetime(2026, 11, 9, 9, 0))
    assert schedule.get_slot(s)["status"] == "free"


# --- Изолированные тесты по контракту: без базы данных соседних модулей ---
class FakePatients:
    def get(self, pid):
        return {"id": pid}


class FakeSchedule:
    def __init__(self, status="free"):
        self.slots = {1: {"id": 1, "status": status, "start": "2026-11-10T09:00"}}
        self.occupied = []

    def get_slot(self, sid):
        return self.slots.get(sid)

    def occupy(self, sid):
        self.occupied.append(sid)

    def release(self, sid):
        pass


def test_book_uses_contract_fakes(app, monkeypatch):
    monkeypatch.setattr("appointments.repository.add", lambda patient_id, slot_id: 100)
    sched = FakeSchedule()
    aid = service.book(5, 1, patients=FakePatients(), schedule=sched)
    assert aid == 100 and sched.occupied == [1]


def test_book_busy_slot_by_contract(app):
    with pytest.raises(Conflict):
        service.book(5, 1, patients=FakePatients(), schedule=FakeSchedule(status="busy"))
