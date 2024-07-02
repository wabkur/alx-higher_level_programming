-- Script that lists all genres of the show Dexter in the database hbtn_0d_tvshows.
SELECT r.`name`
  FROM `tv_genres` AS r
       INNER JOIN `tv_show_genres` AS w
       ON r.`id` = w.`genre_id`

       INNER JOIN `tv_shows` AS a
       ON a.`id` = w.`show_id`
       WHERE a.`title` = "Dexter"
 ORDER BY r.`name`;
