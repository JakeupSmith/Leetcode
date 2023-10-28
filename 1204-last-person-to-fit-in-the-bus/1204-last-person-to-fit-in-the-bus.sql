# Write your MySQL query statement below
SELECT person_name 
FROM Queue q
WHERE 1000 >= (
    SELECT SUM(weight) 
    FROM Queue 
    WHERE q.turn >= turn
)
ORDER BY turn DESC 
LIMIT 1;