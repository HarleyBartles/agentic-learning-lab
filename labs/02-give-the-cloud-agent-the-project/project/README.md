# Riverside Hall event setup

This folder is the shared working project for Lab 2.

The project contains the current setup information for a small event at Riverside Hall.

Use the material in this project to answer operational questions about the event. Some state is versioned in the repository, while some operational state may exist only in the local working environment.

## Project areas

- `source/` contains tracked project information.
- `local-setup/` is available for reusable setup material created during the exercise.
- `local/` is intentionally ignored by Git and may contain machine-local runtime state such as the current attendee database.
- `scratch/` contains disposable files used for a safe deletion exercise.

The attendee database is not pre-created. When operational attendee records are first supplied, the on-disk worker should create the reusable database schema in `local-setup/` and create `local/attendees.db`, keeping the record contents local.

Do not assume that every project surface exposes every one of these areas in the same way.
