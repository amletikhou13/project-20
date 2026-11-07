"""Работа с SQLite: соединение и создание таблиц."""
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY, full_name TEXT NOT NULL,
  birth_date TEXT NOT NULL, phone TEXT, policy TEXT UNIQUE NOT NULL);
CREATE TABLE IF NOT EXISTS specialties(id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
CREATE TABLE IF NOT EXISTS doctors(id INTEGER PRIMARY KEY, full_name TEXT NOT NULL,
  specialty_id INTEGER NOT NULL REFERENCES specialties(id));
CREATE TABLE IF NOT EXISTS slots(id INTEGER PRIMARY KEY, doctor_id INTEGER NOT NULL REFERENCES doctors(id),
  start TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'free');
CREATE TABLE IF NOT EXISTS appointments(id INTEGER PRIMARY KEY, patient_id INTEGER NOT NULL REFERENCES patients(id),
  slot_id INTEGER UNIQUE NOT NULL REFERENCES slots(id), status TEXT NOT NULL DEFAULT 'active');
CREATE TABLE IF NOT EXISTS record_entries(id INTEGER PRIMARY KEY, appointment_id INTEGER UNIQUE NOT NULL REFERENCES appointments(id),
  complaints TEXT, diagnosis TEXT NOT NULL, prescriptions TEXT);
"""
_path = {"p": "clinic.db"}


def init_db(path):
    _path["p"] = path
    with connect() as c:
        c.executescript(SCHEMA)


def connect():
    c = sqlite3.connect(_path["p"])
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    return c
