-- A script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT r.`title`, g.`genre_id`
  FROM `tv_shows` AS r
       LEFT JOIN `tv_show_genres` AS w
       ON r.`id` = w.`show_id`
 ORDER BY r.`title`, w.`genre_id`;
