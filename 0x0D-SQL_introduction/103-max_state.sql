-- Displays the max temperatureof each state
-- ordered by State name
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;
