# Attendee data

Current attendee records belong in the local operational SQLite database at:

`local/attendees.db`

That database is machine-local runtime state and is intentionally not committed to the repository.

The reusable database schema belongs in source control, but it is not pre-created for this exercise. When operational attendee records are first supplied, the on-disk worker should create both the reusable schema and `local/attendees.db`, while keeping current attendee names, confirmation states, and meal choices only in the local database unless a later task explicitly requires a different approved output.
