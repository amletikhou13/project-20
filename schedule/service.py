"""Бизнес-логика расписания (FR-02, FR-05)."""

from schedule import repository as repo


def add_specialty(name):
    return repo.add_specialty(name)


def add_doctor(full_name, specialty_id):
    return repo.add_doctor(full_name, specialty_id)


def add_slot(doctor_id, start):
    return repo.add_slot(doctor_id, start)


def free_slots(specialty_id):
    return repo.free_slots(specialty_id)


def day_schedule(doctor_id, day):
    return repo.day_schedule(doctor_id, day)


def get_slot(sid):
    return repo.get_slot(sid)


def occupy(sid):
    repo.set_status(sid, "busy")


def release(sid):
    repo.set_status(sid, "free")
