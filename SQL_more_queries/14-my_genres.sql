-- This is a script that Import the database dump of hbtn_0d_tvshows to my MySQL server
SELECT 
    genres.name
FROM 
    tv_shows
JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN 
    genres ON tv_show_genres.genre_id = genres.id
WHERE 
    tv_shows.title = 'Dexter'
ORDER BY 
    genres.name ASC