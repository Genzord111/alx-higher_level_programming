-- creates the table id_not_null with a default value for in
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
