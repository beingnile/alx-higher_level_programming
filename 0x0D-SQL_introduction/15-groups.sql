-- Lists all records with the same score
SELECT score, COUNT(*) AS number
GROUP BY score
ORDER BY score DESC;
