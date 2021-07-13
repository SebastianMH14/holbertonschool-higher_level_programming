-- script that lists all the cities of California
SELECT id, name FROM cities WHERE state_id = (
        SELECT ID
        FROM states
        WHERE name = 'California'
)
