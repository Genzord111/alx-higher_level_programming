-- script that lists all genres from hbtn_0d_tvshows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT tv_genres.name, COUNT(*) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
