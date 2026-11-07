"""HTTP-маршруты пациентов."""

from flask import Blueprint, jsonify, request

from patients import service

bp = Blueprint("patients", __name__, url_prefix="/patients")


@bp.post("")
def create():
    d = request.get_json()
    pid = service.register(d["full_name"], d["birth_date"], d.get("phone"), d["policy"])
    return jsonify(id=pid), 201


@bp.get("/<int:pid>")
def read(pid):
    return jsonify(service.get(pid))
