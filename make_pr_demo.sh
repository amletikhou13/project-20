
set -e
cd "$(dirname "$0")/clinic-project"
git checkout -q main
git checkout -q -b feature/patients
cat >> patients/service.py <<'P'


def find_by_policy(policy):
    """Найти пациента по номеру полиса (FR-01)."""
    return repository.by_policy(policy)
P
git add -A && git commit -q -m "feat(patients): add search by policy number"
git push -u origin feature/patients
git checkout -q main
git checkout -q -b feature/appointments
cat >> appointments/service.py <<'P'


def is_cancellable(start_iso, now=None, hours=2):
    """Можно ли отменить запись (BR-04): до начала приёма не меньше hours часов."""
    now = now or datetime.now()
    return datetime.fromisoformat(start_iso) - now >= timedelta(hours=hours)
P
git add -A && git commit -q -m "feat(appointments): add cancellation check (BR-04)"
git push -u origin feature/appointments
git checkout -q main
echo "Теперь на GitHub нажмите Compare & pull request для обеих веток."
