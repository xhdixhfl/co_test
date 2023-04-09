-- 코드를 입력하세요
SELECT GU.user_id, GU.nickname, sum(price) as total_sales
from (
    SELECT writer_id, price
    FROM used_goods_board
    WHERE STATUS = 'DONE') as GB
    INNER JOIN used_goods_user as GU
    ON GB.writer_id = GU.user_id
GROUP BY GU.user_id
HAVING SUM(price) >= 700000
ORDER BY total_sales