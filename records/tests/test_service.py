import pytest

from core.exceptions import Conflict
from records import service


def test_diagnosis_required(app):
    with pytest.raises(Conflict):
        service.add_entry(1, "жалобы", "", None)
