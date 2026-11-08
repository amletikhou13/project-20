"""Исключения предметной области."""


class ClinicError(Exception):
    """Базовая ошибка клиники."""


class NotFound(ClinicError):
    """Объект не найден."""


class Conflict(ClinicError):
    """Нарушено бизнес-правило (например, слот занят)."""


class Forbidden(ClinicError):
    """Действие запрещено правилами доступа."""
