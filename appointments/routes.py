"""HTTP-маршруты записи на приём."""

from flask import Blueprint, jsonify, request

from appointments import service

bp = Blueprint("appointments", __name__, url_prefix="/appointments")


@bp.post("")
def create():
    d = request.get_json()
    return jsonify(id=service.book(d["patient_id"], d["slot_id"])), 201
