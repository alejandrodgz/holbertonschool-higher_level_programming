-- genres of show dexter
-- uses of different joins
SELECT tv_genres.name FROM tv_genres 
INNER JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id and show_id = 8
ORDER BY tv_genres.name ASC; 