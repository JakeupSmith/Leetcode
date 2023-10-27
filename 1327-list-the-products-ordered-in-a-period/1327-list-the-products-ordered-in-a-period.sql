# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM Products 
LEFT JOIN Orders
    USING(product_id)
WHERE MONTH(Orders.order_date) = '02' and YEAR(Orders.order_date) = '2020'
GROUP BY product_name
HAVING SUM(unit) >= 100;