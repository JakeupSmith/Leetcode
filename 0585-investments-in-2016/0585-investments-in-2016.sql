# Write your MySQL query statement below
select ROUND(sum(TIV_2016),2) TIV_2016
from insurance a
where 1 = (select count(*) from insurance b where a.LAT=b.LAT and a.LON=b.LON) 
and 1 < (select count(*) from insurance c where a.TIV_2015=c.TIV_2015)  ;