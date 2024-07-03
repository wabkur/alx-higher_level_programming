-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT r.`id`, r.`name`, s.`name`
  FROM `cities` AS r
       INNER JOIN `states` AS s
       ON r.`state_id` = s.`id`
 ORDER BY r.`id`;
