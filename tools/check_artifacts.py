"""Проверка перечня артефактов docs/artifacts.md: число, уникальность ID, существование путей в Git."""

import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED = {"Готов", "В работе", "План", "Архив"}


def main():
    text = open(os.path.join(ROOT, "docs", "artifacts.md"), encoding="utf-8").read()
    section = text.split("## Матрица артефактов")[1].split("##")[0]
    rows = [
        [c.strip() for c in line.strip().strip("|").split("|")]
        for line in section.splitlines()
        if line.startswith("| A-")
    ]
    errors, ids = [], set()
    for r in rows:
        aid, place, status = r[0], r[5], r[7]
        if aid in ids:
            errors.append(f"{aid}: повторяющийся ID")
        ids.add(aid)
        if not all(r):
            errors.append(f"{aid}: пустая ячейка")
        if status not in ALLOWED:
            errors.append(f"{aid}: неизвестный статус {status}")
        if place.startswith("Git: ") and status != "План":
            for path in place[5:].split(", "):
                if not glob.glob(os.path.join(ROOT, path)):
                    errors.append(f"{aid}: путь {path} не найден")
    if len(rows) < 15:
        errors.append(f"артефактов {len(rows)}, нужно не менее 15")
    for e in errors:
        print("ОШИБКА:", e)
    if errors:
        return 1
    print(f"OK: {len(rows)} артефактов, пути проверены")
    return 0


if __name__ == "__main__":
    sys.exit(main())
