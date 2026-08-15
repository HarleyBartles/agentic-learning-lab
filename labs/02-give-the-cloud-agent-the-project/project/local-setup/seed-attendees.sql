DROP TABLE IF EXISTS attendees;

CREATE TABLE attendees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    confirmed INTEGER NOT NULL CHECK (confirmed IN (0, 1)),
    meal TEXT NOT NULL CHECK (meal IN ('standard', 'vegetarian', 'vegan'))
);

INSERT INTO attendees (id, name, confirmed, meal) VALUES
    (1, 'Amelia Hart', 1, 'vegetarian'),
    (2, 'Ben Carter', 1, 'standard'),
    (3, 'Cara Singh', 1, 'vegetarian'),
    (4, 'Daniel Price', 0, 'vegetarian'),
    (5, 'Elena Rossi', 1, 'vegan'),
    (6, 'Farah Khan', 1, 'vegetarian'),
    (7, 'George Wells', 1, 'standard'),
    (8, 'Hannah Cole', 0, 'standard'),
    (9, 'Isaac Green', 1, 'vegetarian'),
    (10, 'Jade Morgan', 1, 'standard');
