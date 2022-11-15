-- genres of show dexter
-- uses of different joins
USE hbtn_0d_tvshows;
SELECT tv_genres.name FROM tv_genres 
INNER JOIN tv_show_genres INNER JOIN tv_shows 
WHERE tv_genres.id = tv_show_genres.genre_id AND show_id = 8 AND tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC; 