"""Конфигурация приложения (значения берутся из переменных окружения)."""

import os


class Config:
    DATABASE = os.environ.get("CLINIC_DB", "clinic.db")
    SLOT_MINUTES = 20
    CANCEL_BEFORE_HOURS = 2
