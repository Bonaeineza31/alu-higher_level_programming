-- This is a script that Import the database dump from hbtn_0d_tvshows to your MySQL server:
SELECT tv_genres.name, COUNT(tv_shows.id) AS show_count
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY show_count DESC, tv_genres.name ASC;