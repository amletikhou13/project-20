"""HTTP-маршруты расписания."""

from flask import Blueprint, jsonify

from schedule import service

bp = Blueprint("schedule", __name__, url_prefix="/schedule")


@bp.get("/free/<int:specialty_id>")
def free(specialty_id):
    return jsonify(service.free_slots(specialty_id))
