-- select and group
-- join tables
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows 
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id AND tv_show_genres.show_id = 8 AND tv_shows.name ="Dexter"
GROUP BY genre_id ORDER  BY number_of_shows DESC;