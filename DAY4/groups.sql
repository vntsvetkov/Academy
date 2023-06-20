CREATE TABLE groups
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    rating INTEGER DEFAULT 0 CHECK(rating >= 0 and rating <= 5),
    course INTEGER DEFAULT 1 NOT NULL

);

INSERT INTO GROUPS (name, rating, course)
VALUES
("P01"),
("P02"),
("P03"),
("P04"),
("P05"),
("P06"),
("P07")


CREATE TABLE teachers
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    employment_date TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL DEFAULT 20000.0 CHECK(salary > 0),
    allowance REAL DEFAULT 0 CHECK(allowance >= 0)

);

INSERT INTO teachers (name, surname, employment_date, position, salary)
VALUES
("Иван", "Петров", "2022-05-15", "Проффесор", 45000),
("Петр", "Иванов", "2019-12-12", "Доцент", 39000),
("Антон", "Сидоров", "2015-10-06", "Преподаватель", 32000),
("Иван", "Иванов", "2012-05-15", "Проффесор", 45000),
("Петр", "Сидоров", "2017-12-12", "Профессор", 39000),
("Антон", "Петров", "2010-10-06", "Доцент", 32000),
("Петр", "Петров", "2003-12-12", "Профессор", 39000),
("Антон", "Иванов", "2007-10-06", "Преподаватель", 32000),


/* Группировка запросов 
    Оператор GROUP BY

    Агрегатные функции:
    AVG()
    SUM()
    MIN()
    MAX()
    COUNT()

SELECT
expressions
FROM tables
[WHERE conditions]
[GROUP BY expressions]
[HAVING condition]
[ORDER BY expression [ ASC | DESC ]]
[LIMIT number_rows OFFSET offset_value];

*/

/* Статистика по должностям сотрудников, которые работают больше 5 лет*/
SELECT position, COUNT(*) AS [count_position] 
FROM teachers
WHERE (date('now') - employment_date) > 5
GROUP BY position


SELECT position, COUNT(*) AS [count_position], MIN(salary) AS [min_salary]
FROM teachers
WHERE (date('now') - employment_date) > 5
GROUP BY position


position     count_position    min_salary
Доцент	        1	            32000.0
Преподаватель	2	            32000.0
Профессор	    3	            39000.0


/* Запросить должности на которых минимальная ЗП Б 35000*/
SELECT position, COUNT(*) AS [count_position], MIN(salary) AS [min_salary]
FROM teachers
WHERE (date('now') - employment_date) > 5
GROUP BY position
HAVING min_salary < 35000
ORDER BY count_position DESC

/* Увеличить ЗП по итогам выборки сверху*/
UPDATE teachers
SET salary = salary + 5000
WHERE 
position = "Преподаватель" and salary = 32000 or 
position = "Доцент" and salary = 32000

/*Подзапрос*/
SELECT name, surname, salary
FROM teachers
WHERE salary < (SELECT AVG(salary) FROM teachers);