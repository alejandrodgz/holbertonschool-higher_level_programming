-- listing everything 
-- that is not null
SELECT score, name FROM second_table WHERE score IS NOT NULL AND name IS NOT NULL ORDER BY score DESC;