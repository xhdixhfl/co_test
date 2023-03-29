-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.price * s.sales_amount)  as sales
from PRODUCT p 
inner join OFFLINE_SALE s
on p.PRODUCT_ID = s.PRODUCT_ID
group by p.PRODUCT_CODE
order by sales desc, p.PRODUCT_CODE ;