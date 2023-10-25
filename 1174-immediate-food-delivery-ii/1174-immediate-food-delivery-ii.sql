# Write your MySQL query statement below
with base_table as (
select *, rank() over(partition by customer_id order by order_date) as ranking 
from delivery )

select round(avg(case when order_date = customer_pref_delivery_date then 1.00 else 0.00 end)*100, 2) as immediate_percentage 
from base_table
where ranking = 1 
