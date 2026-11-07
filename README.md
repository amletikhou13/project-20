# clinic-project

ИС медицинской клиники (Python, Flask, SQLite).

## Запуск
pip install -r requirements.txt
python app.py

## Тесты
pytest

## Модульная структура
Проект разделён на модули core, patients, schedule, appointments, records (внутри каждого: models, repository, service, routes, tests).
Проверка зависимостей и циклов: python tools/check_deps.py
Тесты одного модуля: pytest appointments/tests/ -v
