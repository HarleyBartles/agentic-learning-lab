DROP TABLE IF EXISTS attendees;

CREATE TABLE attendees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    confirmed INTEGER NOT NULL CHECK (confirmed IN (0, 1)),
    meal TEXT NOT NULL CHECK (meal IN ('standard', 'vegetarian', 'vegan'))
);
