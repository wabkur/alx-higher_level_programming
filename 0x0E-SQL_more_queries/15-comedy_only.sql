-- Script that lists all comedy shows in the database hbtn_0d_tvshows.
SELECT r.`title`
  FROM `tv_shows` AS r
       INNER JOIN `tv_show_genres` AS s
       ON r.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS w
       ON w.`id` = s.`genre_id`
       WHERE w.`name` = "Comedy"
 ORDER BY r.`title`;
