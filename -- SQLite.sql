-- SQLite
SELECT
  t.id AS trainer_id,
  t.full_name AS treener,
  COUNT(s.id) AS seansse
FROM trainers t
LEFT JOIN sessions s ON s.trainers_id = t.id
GROUP BY t.id;