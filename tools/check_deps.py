"""Проверка модульной структуры: граф зависимостей, циклы, публичный API, правила слоёв.

Запуск: python tools/check_deps.py [--dot graph.dot]
Код возврата 0 - нарушений нет, 1 - найдены нарушения.
"""
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ["core", "patients", "schedule", "appointments", "records"]
# Разрешённые зависимости между модулями (таблица контрактов из отчёта)
ALLOWED = {
    "core": set(),
    "patients": {"core"},
    "schedule": {"core"},
    "appointments": {"core", "patients", "schedule"},
    "records": {"core"},
}
PRIVATE_FILES = {"repository", "routes"}  # чужие модули не должны импортировать эти файлы


def imports_of(path):
    """Вернуть список (пакет, подмодуль или None) для каждого импорта проекта в файле."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names = [node.module]
            names += [node.module + "." + a.name for a in node.names]
        else:
            continue
        for n in names:
            parts = n.split(".")
            if parts[0] in MODULES:
                found.append((parts[0], parts[1] if len(parts) > 1 else None))
    return found


def collect():
    edges, file_edges, bad_api = set(), set(), []
    for mod in MODULES:
        for f in sorted((ROOT / mod).glob("*.py")):
            for pkg, sub in imports_of(f):
                if pkg == mod:
                    if sub and sub != f.stem:
                        file_edges.add((mod + "." + f.stem, mod + "." + sub))
                    continue
                edges.add((mod, pkg))
                file_edges.add((mod + "." + f.stem, pkg + (("." + sub) if sub else "")))
                if sub in PRIVATE_FILES:
                    bad_api.append(f"{mod}/{f.name} импортирует внутренний файл {pkg}.{sub}")
    return edges, file_edges, bad_api


def find_cycle(edges):
    graph = {m: sorted(b for a, b in edges if a == m) for m in MODULES}
    state, stack = {}, []

    def dfs(v):
        state[v] = 1
        stack.append(v)
        for w in graph[v]:
            if state.get(w) == 1:
                return stack[stack.index(w):] + [w]
            if w not in state:
                c = dfs(w)
                if c:
                    return c
        stack.pop()
        state[v] = 2
        return None

    for m in MODULES:
        if m not in state:
            c = dfs(m)
            if c:
                return c
    return None


def check_all(root=ROOT):
    edges, file_edges, bad_api = collect()
    errors = list(bad_api)
    for a, b in sorted(edges):
        if b not in ALLOWED[a]:
            errors.append(f"запрещённая зависимость {a} -> {b}")
    cycle = find_cycle(edges)
    if cycle:
        errors.append("цикл: " + " -> ".join(cycle))
    for mod in MODULES:
        init = (ROOT / mod / "__init__.py").read_text(encoding="utf-8")
        if "__all__" not in init:
            errors.append(f"{mod}/__init__.py: нет __all__")
    return edges, file_edges, errors


def to_dot(edges):
    lines = ["digraph deps {", "  rankdir=BT;", '  node [shape=box];']
    lines += [f"  {a} -> {b};" for a, b in sorted(edges)]
    return "\n".join(lines + ["}"])


def main():
    edges, file_edges, errors = check_all()
    print("Зависимости между модулями:")
    for a, b in sorted(edges):
        print(f"  {a} -> {b}")
    if "--dot" in sys.argv:
        Path(sys.argv[sys.argv.index("--dot") + 1]).write_text(to_dot(edges), encoding="utf-8")
    if errors:
        print("НАРУШЕНИЯ:")
        for e in errors:
            print("  " + e)
        return 1
    print("Циклов нет, запрещённых зависимостей нет, __all__ во всех модулях есть.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
