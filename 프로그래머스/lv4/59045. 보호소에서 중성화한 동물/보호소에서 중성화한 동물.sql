-- 코드를 입력하세요
SELECT b.animal_id, b.animal_type, b.name
FROM (
SELECT a.*
FROM ANIMAL_OUTS as a
WHERE SEX_UPON_OUTCOME LIKE("%Spayed%") or SEX_UPON_OUTCOME LIKE("%Neutered%")) as b
INNER JOIN
(SELECT *
FROM ANIMAL_INS as c
WHERE NOT (SEX_UPON_INTAKE LIKE("%Spayed%") or SEX_UPON_INTAKE LIKE("%Neutered%"))) as d
ON b.ANIMAL_ID = d.ANIMAL_ID
ORDER BY b.ANIMAL_ID