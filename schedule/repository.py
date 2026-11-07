"""Доступ к врачам, специальностям и слотам."""
from core.db import connect


def add_specialty(name):
    with connect() as c:
        return c.execute("INSERT INTO specialties(name) VALUES(?)", (name,)).lastrowid


def add_doctor(full_name, specialty_id):
    with connect() as c:
        return c.execute("INSERT INTO doctors(full_name,specialty_id) VALUES(?,?)", (full_name, specialty_id)).lastrowid


def add_slot(doctor_id, start):
    with connect() as c:
        return c.execute("INSERT INTO slots(doctor_id,start) VALUES(?,?)", (doctor_id, start)).lastrowid


def free_slots(specialty_id):
    with connect() as c:
        rows = c.execute("""SELECT s.id, s.start, d.full_name AS doctor FROM slots s JOIN doctors d ON d.id=s.doctor_id
                            WHERE d.specialty_id=? AND s.status='free' ORDER BY s.start""", (specialty_id,)).fetchall()
        return [dict(r) for r in rows]


def get_slot(sid):
    with connect() as c:
        r = c.execute("SELECT * FROM slots WHERE id=?", (sid,)).fetchone()
        return dict(r) if r else None


def set_status(sid, status):
    with connect() as c:
        c.execute("UPDATE slots SET status=? WHERE id=?", (status, sid))


def day_schedule(doctor_id, day):
    with connect() as c:
        rows = c.execute("SELECT * FROM slots WHERE doctor_id=? AND start LIKE ? ORDER BY start", (doctor_id, day + "%")).fetchall()
        return [dict(r) for r in rows]
