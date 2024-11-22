-- lists all cities contained in the database Each record should display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id=states.id;
