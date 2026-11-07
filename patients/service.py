"""Бизнес-логика пациентов (FR-01)."""

from core.exceptions import Conflict, NotFound
from patients import repository


def register(full_name, birth_date, phone, policy):
    if repository.by_policy(policy):
        raise Conflict("пациент с таким полисом уже есть")
    return repository.add(full_name, birth_date, phone, policy)


def get(pid):
    p = repository.get(pid)
    if not p:
        raise NotFound("пациент не найден")
    return p
