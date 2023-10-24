# Write your MySQL query statement below
SELECT DISTINCT contest_id, ROUND(COUNT(DISTINCT register.user_id)/(select count(*) from users)*100,2) AS percentage
FROM users
LEFT JOIN Register
    ON Register.user_id = Users.user_id
WHERE contest_ID IS NOT NULL
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;