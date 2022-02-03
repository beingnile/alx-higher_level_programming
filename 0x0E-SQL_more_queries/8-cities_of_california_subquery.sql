-- List all cities of California that can be found in the hbtn_0d_usa database
SELECT id, name FROM hbtn_0d_usa.cities WHERE state_id = 1 ORDER BY id ASC;
