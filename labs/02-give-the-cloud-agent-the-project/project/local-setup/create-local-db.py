from pathlib import Path
import random
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / "local"
DB = LOCAL / "attendees.db"
SCHEMA = Path(__file__).with_name("seed-attendees.sql")

NAMES = [
    "Amelia Hart", "Ben Carter", "Cara Singh", "Daniel Price", "Elena Rossi",
    "Farah Khan", "George Wells", "Hannah Cole", "Isaac Green", "Jade Morgan",
    "Kieran Bell", "Leila Shah", "Marcus Reed", "Nina Evans", "Owen Brooks",
    "Priya Patel", "Quinn Foster", "Rosa Martin", "Sam Lewis", "Tara Young",
]
MEALS = ["standard", "vegetarian", "vegan"]

LOCAL.mkdir(parents=True, exist_ok=True)
if DB.exists():
    DB.unlink()

rng = random.SystemRandom()

with sqlite3.connect(DB) as conn:
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))
    rows = []
    for idx, name in enumerate(NAMES, start=1):
        confirmed = 1 if rng.random() < 0.8 else 0
        meal = rng.choices(MEALS, weights=[6, 3, 1], k=1)[0]
        rows.append((idx, name, confirmed, meal))
    conn.executemany(
        "INSERT INTO attendees (id, name, confirmed, meal) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()

print(f"Created {DB}")
