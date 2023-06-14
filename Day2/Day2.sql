/* Запрос на добавление данных в таблицу */
INSERT INTO cars (brand, model, vin, power, color, price, quantity) 
VALUES
("KIA", "Ceed", "ZFA22300005556899", 240, "red", 2600000, 4),
("KIA", "Rio", "ZFA22300456556899", 260, "gray", 2200000, 3),
("FORD", "Focus", "ZFA25600456556899", 270, "gray", 2900000, 6),
("FORD", "C-max", "ZFA22333456556899", 230, "red", 3200000, 1)

/*
Когда можно опускать значения:
    - Также мы можем опускать при добавлении такие столбцы, 
      которые поддерживают значение NULL 
      (которые не имеют ограничения NOT NULL).
    - Также подобным столбцам, которые поддерживают NULL, 
      можно явным образом передать NULL.
    - Если для столбца задано ограничение DEFAULT, 
      то есть значение по умолчанию, 
      то для него тоже можно не передавать значение.
*/
 
/*
При вставке данных может нарушаются ограничения UNIQUE, 
например, когда мы пытаемся добавить для столбца, 
который должен иметь уникальные значения, данные, 
которые уже есть в таблице. 

Этот конфликт ограничений призвана разрешить команда REPLACE.

       1. Эта команда сначала удаляет строку, которая вызвала конфликт 
       на уникальность данных, и затем вместо нее вставляет 
       новую строку. То есть фактически все выглядит как замена строки.
       
       2. Если происходит конфликт с ограничением NOT NULL 
       (в столбец, для которого задано ограничение NOT NULL, 
       вставляется значение NULL), команда REPLACE заменяется 
       вставляемое значение NULL значением по умолчанию, 
       которое принято для этого столбца. 
       Если для столбца не установлено значение по умолчанию, 
       то выполнение запроса отменяется.

       3. Если конфликтов с ограничениями не происходит, 
       то команда REPLACE по сути действует аналогично команде INSERT.

Допустим vin - UNIQUE */

REPLACE INTO cars (brand, model, vin, power, color, price, quantity) 
VALUES
("LADA", "GRANTA", "ZFA22311115556899", 260, "red", 6600000, 10)


/* Запросы */

SELECT *
FROM cars

SELECT brand, model, price, quantity
FROM cars

SELECT brand, model, price * quantity
FROM cars

CREATE TABLE copy_cars AS 
       	SELECT *
       	FROM cars
    
/* Синтаксис SELECT */
SELECT
expressions
FROM tables
[WHERE conditions]
[GROUP BY expressions]
[HAVING condition]
[ORDER BY expression [ ASC | DESC ]]
[LIMIT number_rows OFFSET offset_value];

SELECT *
FROM cars
WHERE color = "red"

SELECT brand, model, color, quantity
FROM cars
WHERE (color = "red" AND quantity > 0) or color = "black"

UPDATE cars
SET price = price * 0.8
WHERE brand = "LADA" AND model = "GRANTA" 

DELETE FROM copy_cars
WHERE quantity = 0

/* Выборка уникальных брендов*/
SELECT DISTINCT brand FROM cars


SELECT *
FROM cars
WHERE price > 2000000
LIMIT 2 OFFSET 2