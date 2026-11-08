import pytest

from core.exceptions import Conflict
from patients import service


def test_register_and_duplicate(app):
    pid = service.register("Иванов Иван", "1990-01-01", "+79990000000", "123")
    assert service.get(pid)["full_name"] == "Иванов Иван"
    with pytest.raises(Conflict):
        service.register("Другой", "1991-01-01", None, "123")
