-- Script that lists all cities contain in the database hbtn_0d_usa.
SELECT cities.`id`, cities.`name`, state.`name`
  FROM `cities`
       INNER JOIN `states`
       ON cities.`state_id` = state.`id`
 ORDER BY cities.`id`;
