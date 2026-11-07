# Участие в разработке clinic-project

## Ветки
Модель GitHub Flow. Ветка main всегда рабочая, прямой push в неё запрещён.
- feature/<модуль> - новая функциональность (feature/patients, feature/appointments);
- fix/<ошибка> - исправление (fix/appointments-cancel);
- docs/<тема> - документация;
- chore/<тема> - служебные изменения (chore/configure-repository).
Одна задача - одна ветка, живёт 1-3 дня, после слияния удаляется. Перед Pull Request: git pull origin main.

## Коммиты (Conventional Commits)
Формат: <type>(<scope>): <описание>. Типы: feat, fix, docs, style, refactor, test, chore, ci.
Scope - модуль: core, patients, schedule, appointments, records.
Примеры: feat(patients): add phone validation; fix(appointments): reject cancel less than 2 hours.
Шаблон сообщения: git config commit.template .gitmessage. Формат проверяет хук commit-msg.

## Подготовка рабочего места
    pip install -r requirements-dev.txt
    pre-commit install            # или: git config core.hooksPath .githooks
    pre-commit run --all-files

## Pull Request
1. Создать ветку от актуального main.
2. Перед push выполнить проверки: pytest, tools/check_deps.py, black, ruff, mypy.
3. Открыть Pull Request по шаблону, привязать задачу (Closes #N).
4. Дождаться зелёного CI и одобрения хотя бы одного ревьюера (владельцы указаны в .github/CODEOWNERS).
5. Слияние - squash merge, ветку удалить.

## Версии и релизы
SemVer: MAJOR.MINOR.PATCH. Каждый релиз - аннотированный тег vX.Y.Z и запись в CHANGELOG.md.

## Секреты
Не коммитить .env, ключи и пароли. В репозитории только .env.example.
Секреты CI хранятся в GitHub Secrets. При утечке секрет отзывается и заменяется.
