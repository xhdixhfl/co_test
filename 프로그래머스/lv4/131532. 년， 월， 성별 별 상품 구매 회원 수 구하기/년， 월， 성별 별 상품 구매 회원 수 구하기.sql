-- 코드를 입력하세요
SELECT YEAR(OS.SALES_DATE) YEAR, MONTH(OS.SALES_DATE) MONTH, UI.GENDER, 
COUNT(DISTINCT(OS.USER_ID)) USERS
FROM USER_INFO UI
JOIN ONLINE_SALE OS
ON OS.USER_ID = UI.USER_ID
WHERE UI.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, UI.GENDER
ORDER BY YEAR, MONTH, UI.GENDER