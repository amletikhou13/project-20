"""Доступ к записям медицинской карты."""

from core.db import connect


def add(appointment_id, complaints, diagnosis, prescriptions):
    with connect() as c:
        return c.execute(
            "INSERT INTO record_entries(appointment_id,complaints,diagnosis,prescriptions) VALUES(?,?,?,?)",
            (appointment_id, complaints, diagnosis, prescriptions),
        ).lastrowid


def by_patient(patient_id):
    with connect() as c:
        rows = c.execute(
            """SELECT r.* FROM record_entries r JOIN appointments a ON a.id=r.appointment_id
                            WHERE a.patient_id=?""",
            (patient_id,),
        ).fetchall()
        return [dict(r) for r in rows]


def count_all():
    with connect() as c:
        return c.execute("SELECT COUNT(*) FROM record_entries").fetchone()[0]
