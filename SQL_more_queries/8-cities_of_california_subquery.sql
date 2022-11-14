-- script to list cities of california
-- first join
SELECT id, name FROM cities WHERE state_id = 1 ORDER BY cities.id ASC;