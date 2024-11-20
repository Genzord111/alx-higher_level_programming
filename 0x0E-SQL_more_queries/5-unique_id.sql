-- creates the table unique_id with a unique value for in
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE(id)
);
