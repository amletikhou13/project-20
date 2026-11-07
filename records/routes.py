"""HTTP-маршруты медкарты."""

from flask import Blueprint, jsonify, request

from records import service

bp = Blueprint("records", __name__, url_prefix="/records")


@bp.post("")
def create():
    d = request.get_json()
    return (
        jsonify(id=service.add_entry(d["appointment_id"], d.get("complaints"), d["diagnosis"], d.get("prescriptions"))),
        201,
    )


@bp.get("/<int:patient_id>")
def card(patient_id):
    return jsonify(service.card(patient_id))
