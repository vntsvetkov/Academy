CREATE TABLE faculties
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facultie_name TEXT NOT NULL UNIQUE,
    id_dean INTEGER NOT NULL UNIQUE
    
);

CREATE TABLE deans
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE departments
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    financing REAL DEFAULT 0 CHECK(financing >= 0),
    id_teacher INTEGER NOT NULL UNIQUE,
    id_facultie INTEGER NOT NULL UNIQUE
);


INSERT INTO deans (name, surname, email)
VALUES
("Иван", "Петров", "ia.petrov@education.ru"),
("Петр", "Иванов", "po.ivanov@education.ru");

INSERT INTO faculties (facultie_name, id_dean)
VALUES
("Физико-математический", 1),
("Экономический", 2);

INSERT INTO departments (name, financing, id_teacher, id_facultie)
VALUES
("Высшая математика", 100000, 1, 1),
("Управление финансами", 150000, 2, 2);

-- Практическое задание. 
/* Вывести таблицу кафедр  в обратном порядке*/
SELECT *
FROM departments
ORDER BY id DESC

/* Вывести названия групп и их рейтинги с уточнением имен полей*/

SELECT name AS [Название группы], rating AS [Рейтинг]
FROM groups

/* Вывести фамилии преподавателей, которые являются профессорами и зарплата которых превышает 10500*/

SELECT surname AS [Фамилия]
FROM teachers
WHERE position = "Профессор" and salary > 10500

/* Вывести названия кафедр, фонд финансирования которых меньше 110000 или больше 250000 */

SELECT name
from departments
WHERE financing < 110000 or financing > 250000

/* Вывести названия факультетов кроме "Машинное обучение"*/

SELECT facultie_name 
FROM faculties
WHERE facultie_name != "Машинное обучение"

/* Вывести фамилии и должности преподавателей, которые не являются профессорами */

SELECT surname AS [Фамилия], position AS [Должность]
FROM teachers
WHERE position != "Профессор"


/* Вывести фамилии, должности, зарплаты ассистентов, у которых зарплпта в диапазоне от 16000 до 55000 */

SELECT surname AS [Фамилия], position AS [Должность], salary AS [Зарплата]
FROM teachers
WHERE position = "Ассистент" and salary BETWEEN 16000 and 55000

/* Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000 */

SELECT surname AS [Фамилия], position AS [Должность]
FROM teachers
WHERE date('now') - employment_date > 23

/* Вывести названия кафедр, которые по алфавиту идут до кафедры "Управление финансами" */

SELECT name
FROM departments
WHERE name < "Управление финансами"
ORDER BY name

/* Вывести названия групп 5-го курса, имеющих рейтинг в диапазоне от 2 до 4. */

SELECT name
FROM groups
WHERE course = 5 and rating BETWEEN 2 and 4


/* Запросы меджу несколькими таблицами*/

SELECT 
teachers.name AS [Имя], 
teachers.surname AS [Фамилия], 
departments.name AS [Название кафедры]
FROM teachers, departments
WHERE teachers.id_departament = departments.id

SELECT 
departments.name AS [Название кафедры],
deans.name AS [Имя],
deans.surname AS [Фамилия]
FROM departments, deans
WHERE departments.id_teacher = deans.id

SELECT 
departments.name AS [Название кафедры],
faculties.facultie_name AS [Название факультета]
FROM departments,faculties
WHERE departments.id_facultie = faculties.id

/*Сколько кафедр на каждом факультете*/
SELECT 
faculties.facultie_name AS [Название факультета], count(*) AS [Количество кафедр]
FROM departments,faculties
WHERE departments.id_facultie = faculties.id
GROUP BY faculties.facultie_name