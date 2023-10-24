# Write your MySQL query statement below
SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus
    USING(empID)
WHERE bonus < 1000 OR Bonus.bonus IS NULL;