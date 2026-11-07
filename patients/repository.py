"""Доступ к таблице patients."""

from core.db import connect


def add(full_name, birth_date, phone, policy):
    with connect() as c:
        cur = c.execute(
            "INSERT INTO patients(full_name,birth_date,phone,policy) VALUES(?,?,?,?)",
            (full_name, birth_date, phone, policy),
        )
        return cur.lastrowid


def get(pid):
    with connect() as c:
        r = c.execute("SELECT * FROM patients WHERE id=?", (pid,)).fetchone()
        return dict(r) if r else None


def by_policy(policy):
    with connect() as c:
        r = c.execute("SELECT * FROM patients WHERE policy=?", (policy,)).fetchone()
        return dict(r) if r else None
