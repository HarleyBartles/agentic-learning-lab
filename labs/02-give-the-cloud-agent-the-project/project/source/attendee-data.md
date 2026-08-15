# Attendee data

Current attendee records belong in the local operational SQLite database at:

`local/attendees.db`

That database is machine-local runtime state and is intentionally not committed to the repository.

The repository contains only reusable database structure in `local-setup/schema.sql`. Current attendee names, confirmation states, and meal choices should exist only in the local database unless a later task explicitly requires a different approved output.

If `local/attendees.db` does not exist yet, the on-disk worker may create it from the schema when operational records are first supplied.
