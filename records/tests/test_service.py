import pytest
from records import service
from core.exceptions import Conflict


def test_diagnosis_required(app):
    with pytest.raises(Conflict):
        service.add_entry(1, "жалобы", "", None)
