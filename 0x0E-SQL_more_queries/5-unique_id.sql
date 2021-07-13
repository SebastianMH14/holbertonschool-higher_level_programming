-- script that creates the table unique_id
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT UNIQUE 1,
    name VARCHAR(256)
);
