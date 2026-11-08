"""Точка входа clinic-project: создаёт Flask-приложение и подключает модули."""
from flask import Flask

from core.config import Config
from core.db import init_db
from patients.routes import bp as patients_bp
from schedule.routes import bp as schedule_bp
from appointments.routes import bp as appointments_bp
from records.routes import bp as records_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config)
    init_db(app.config["DATABASE"])
    for bp in (patients_bp, schedule_bp, appointments_bp, records_bp):
        app.register_blueprint(bp)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    create_app().run(debug=False)
