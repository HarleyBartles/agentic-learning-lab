import csv
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCHEDULE = PROJECT_ROOT / "work" / "volunteer-schedule.csv"

REQUIRED_PER_STATION = 2
RESTRICTED_STATION = {"Lee": "Repair"}
CANNOT_WORK_SHIFT = {"Sam": "20:00-22:00"}
ONLY_SHIFT = {"Priya": "20:00-22:00"}

with SCHEDULE.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

errors = []
coverage = Counter((row["shift"], row["station"]) for row in rows)

for shift in ("18:00-20:00", "20:00-22:00"):
    for station in ("Welcome", "Repair"):
        count = coverage[(shift, station)]
        if count < REQUIRED_PER_STATION:
            errors.append(
                f"{shift} {station} has {count} volunteer(s); needs {REQUIRED_PER_STATION}."
            )

assignments = defaultdict(list)
for row in rows:
    volunteer = row["volunteer"]
    shift = row["shift"]
    station = row["station"]
    assignments[(volunteer, shift)].append(station)

    if RESTRICTED_STATION.get(volunteer) == station:
        errors.append(
            f"{volunteer} is assigned to {station} at {shift} but cannot work that station."
        )

    if CANNOT_WORK_SHIFT.get(volunteer) == shift:
        errors.append(f"{volunteer} is assigned at {shift} but cannot work that shift.")

    if volunteer in ONLY_SHIFT and ONLY_SHIFT[volunteer] != shift:
        errors.append(
            f"{volunteer} is assigned at {shift} but is only available {ONLY_SHIFT[volunteer]}."
        )

for (volunteer, shift), stations in assignments.items():
    if len(stations) > 1:
        errors.append(
            f'{volunteer} is double-booked at {shift}: {", ".join(stations)}.'
        )

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("PASS: schedule satisfies the prepared coverage and availability checks.")
