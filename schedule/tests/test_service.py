from schedule import service


def test_free_slots_by_specialty(app):
    sp = service.add_specialty("Терапевт")
    d = service.add_doctor("Петрова А.А.", sp)
    service.add_slot(d, "2026-11-10T09:00")
    assert len(service.free_slots(sp)) == 1
