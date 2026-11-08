# Журнал изменений

Формат: Keep a Changelog, версии по SemVer.

## [0.2.0] - 2026-11-07

### Added
- Настройка репозитория: .gitattributes, обновлённый .gitignore, pyproject.toml, requirements-dev.txt.
- Локальные хуки pre-commit и commit-msg (Conventional Commits), .pre-commit-config.yaml.
- CONTRIBUTING.md, шаблоны Pull Request и issue, CODEOWNERS, перечень меток.
- В CI: линтеры (ruff, black, isort), mypy, матрица Python 3.10 и 3.11.

### Changed
- Код отформатирован black и ruff, строки не длиннее 120 символов.

### Fixed
- appointments.cancel: понятная ошибка NotFound, если слот записи не найден.

## [0.1.0] - 2026-11-07

### Added
- Каркас проекта и модули core, patients, schedule, appointments, records.
- Регистрация пациента (FR-01), запись на приём и отмена (FR-03, FR-04).
- Скрипт проверки зависимостей tools/check_deps.py.
- Рабочий процесс CI и перечень артефактов docs/artifacts.md.
