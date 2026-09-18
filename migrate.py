import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
database = Path(os.getenv("DATABASE_PATH", ROOT / "data" / "student_custody.sqlite3"))
database.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(database) as connection:
    for migration in sorted((ROOT / "migrations").glob("*.sql")):
        connection.executescript(migration.read_text(encoding="utf-8"))
print(database)