"""Тест модульной структуры: нет циклов, нет запрещённых зависимостей, во всех модулях есть __all__."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import check_deps  # noqa: E402


def test_no_cycles_and_rules_respected():
    edges, _, errors = check_deps.check_all()
    assert errors == []
    assert ("appointments", "patients") in edges
