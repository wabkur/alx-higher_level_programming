-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT r.`title`, w.`genre_id`
  FROM `tv_shows` AS r
        INNER JOIN `tv_show_genres` AS w
	ON r.`id` = w.`show_id`
 ORDER BY r.`title`, w.`genre_id`;
