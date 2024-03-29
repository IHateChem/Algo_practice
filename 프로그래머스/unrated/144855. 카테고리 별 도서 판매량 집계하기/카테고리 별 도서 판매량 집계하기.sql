-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) as TOTAL_SALES
FROM (SELECT * 
FROM BOOK_SALES as a
WHERE LEFT(SALES_DATE, 7) = "2022-01") as b
INNER JOIN
BOOK as c
ON c.BOOK_ID = b.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY ASC
