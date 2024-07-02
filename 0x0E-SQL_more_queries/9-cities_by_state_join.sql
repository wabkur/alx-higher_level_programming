-- Script that lists all cities contain in the database hbtn_0d_usa.
  FROM cities
       INNER JOIN states
       ON cities.state_id = state.id;
