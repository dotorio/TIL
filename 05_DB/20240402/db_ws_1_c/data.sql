SELECT genre, 
COUNT(*) AS count
FROM songs
GROUP BY
genre;

SELECT *
FROM songs;

SELECT genre, 
COUNT(*) AS count,
AVG(duration) AS average_duration
FROM songs
GROUP BY
genre;