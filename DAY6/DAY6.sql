CREATE TABLE teachers
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    employment_date TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL DEFAULT 20000.0 CHECK(salary > 0),
    allowance REAL DEFAULT 0 CHECK(allowance >= 0)
    id_department INTEGER DEFAULT 0,
    FOREIGN KEY(id_department) REFERENCES departments (id) 
)

/* */
ON DELETE CASCADE
ON UPDATE CASCADE

ON DELETE SET NULL
ON UPDATE SET NULL

ON DELETE ON ACTION
ON UPDATE ON ACTION

ON DELETE SET DEFAULT
ON UPDATE SET DEFAULT


INSERT INTO teachers (name, surname, employment_date, position, salary, id_department)
VALUES
("Иван", "Петров", "2022-05-15", "Проффесор", 45000, (SELECT id FROM departments WHERE name = "Высшая математика")),
("Петр", "Иванов", "2019-12-12", "Доцент", 39000, (SELECT id FROM departments WHERE name = "Управление финансами")),
("Антон", "Сидоров", "2015-10-06", "Преподаватель", 32000, (SELECT id FROM departments WHERE name = "Ядерная физика")),
("Иван", "Иванов", "2012-05-15", "Проффесор", 45000, (SELECT id FROM departments WHERE name = "Банковское дело")),
("Петр", "Сидоров", "2017-12-12", "Профессор", 39000, (SELECT id FROM departments WHERE name = "Высшая математика")),
("Антон", "Петров", "2010-10-06", "Доцент", 32000, (SELECT id FROM departments WHERE name = "Управление финансами")),
("Петр", "Петров", "2003-12-12", "Профессор", 39000, (SELECT id FROM departments WHERE name = "Ядерная физика")),
("Антон", "Иванов", "2007-10-06", "Преподаватель", 32000, (SELECT id FROM departments WHERE name = "Банковское дело")),


/* Вывести информацию о всех профессорах на кафедре высшей математики*/

SELECT 
    teachers.name, 
    teachers.surname, 
    teachers.position, 
    departments.name
FROM 
    teachers,
    departments
WHERE
    teachers.id_department = 1 AND 
	teachers.position = "Профессор"


/* Найти всех заведующих кафедрами*/

SELECT 
    teachers.name, 
    teachers.surname, 
    teachers.position, 
    departments.name
FROM 
    teachers,
    departments
WHERE
    departments.id_teacher = teachers.id


Типы связей в БД
    1. Один к одному
        - Кафедра и заведующий кафедрой
    2. Один ко многим
        - Кафедра и преподаватель
        - Кафедра и факультет
        - Группа и факультет
    3. Многие ко многим
        - Преподаватели и группы
    
    Группа groups
    id  name 
    1   P01
    2   P02
    3   P03

    Преподаватели teachers
    id  surname 
    1   Петров
    2   Иванов
    3   Сидоров

    Группы и Преподаватели, где id_... внешние ключи

    groups_and_teachers
    id_group    id_teacher
    1           1
    1           2
    1           3
    2           1
    2           3
    3           1
    3           2

CREATE TABLE groups_and_teachers
(
	id_group INTEGER,
	id_teacher INTEGER,
	FOREIGN KEY(id_group) REFERENCES groups(id),
	FOREIGN KEY(id_teacher) REFERENCES teachers(id)
)

/* У каких групп ведет занятия профессор Петров*/
SELECT 
groups.name, teachers.name, teachers.surname, teachers.position
FROM 
groups, 
groups_and_teachers,
teachers

WHERE 
groups.id = groups_and_teachers.id_group AND
teachers.id = groups_and_teachers.id_teacher AND
teachers.surname = "Петров"
and teachers.position = "Профессор"