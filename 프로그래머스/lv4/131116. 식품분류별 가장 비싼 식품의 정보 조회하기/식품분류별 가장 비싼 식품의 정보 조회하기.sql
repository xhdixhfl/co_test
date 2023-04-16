-- 코드를 입력하세요
SELECT P.CATEGORY, MAX(P.PRICE) AS MAX_PRICE, (SELECT PRODUCT_NAME
                                               FROM FOOD_PRODUCT 
                                               WHERE P.CATEGORY = CATEGORY
                                              ORDER BY PRICE DESC LIMIT 1)
                                               AS PRODUCT_NAME
FROM FOOD_PRODUCT P
WHERE CATEGORY IN ('과자','국','김치','식용유')
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC