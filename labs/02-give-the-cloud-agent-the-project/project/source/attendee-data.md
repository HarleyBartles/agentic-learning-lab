# Attendee data

Current confirmed attendee and meal requirements are held in the local operational SQLite database at:

`local/attendees.db`

That database is machine-local runtime state and is intentionally not committed to the repository.

The repository contains setup material in `local-setup/` so the local lab environment can be prepared consistently, but current operational answers should come from the database itself when it is available.
