"""Доступ к таблице appointments."""

from core.db import connect


def add(patient_id, slot_id):
    with connect() as c:
        return c.execute("INSERT INTO appointments(patient_id,slot_id) VALUES(?,?)", (patient_id, slot_id)).lastrowid


def get(aid):
    with connect() as c:
        r = c.execute("SELECT * FROM appointments WHERE id=?", (aid,)).fetchone()
        return dict(r) if r else None


def set_status(aid, status):
    with connect() as c:
        c.execute("UPDATE appointments SET status=? WHERE id=?", (status, aid))
