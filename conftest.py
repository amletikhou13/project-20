"""Общие фикстуры: приложение на временной БД и тестовый клиент."""
import pytest
from app import create_app


@pytest.fixture
def app(tmp_path):
    class Cfg:
        DATABASE = str(tmp_path / "test.db")
        TESTING = True
    return create_app(Cfg)


@pytest.fixture
def client(app):
    return app.test_client()
