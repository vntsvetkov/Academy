/* Деканы */
CREATE TABLE "deans" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

/* Кафедры */
CREATE TABLE "departments" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"financing"	REAL DEFAULT 0 CHECK("financing" >= 0),
	"id_head_department"	INTEGER UNIQUE,
	"id_facultie"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
    FOREIGN KEY("id_head_department") REFERENCES teachers("id"),
    FOREIGN KEY("id_facultie") REFERENCES faculties("id")
);

/* Факультеты */
CREATE TABLE "faculties" (
	"id"	INTEGER,
	"facultie_name"	TEXT NOT NULL UNIQUE,
    "financing"	REAL DEFAULT 0 CHECK("financing" >= 0),
	"id_dean"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("id_dean") REFERENCES deans("id")
);

/* Группы */
CREATE TABLE "groups" (
	"name"	TEXT UNIQUE,
	"rating"	INTEGER DEFAULT 0 CHECK("rating" >= 0 AND "rating" <= 5),
	"course"	INTEGER NOT NULL DEFAULT 1,
	"id_facultie"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("name"),
    FOREIGN KEY("id_facultie") REFERENCES faculties("id")
);

/* Преподаватели */
CREATE TABLE "teachers" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"employment_date"	TEXT NOT NULL,
	"position"	TEXT NOT NULL,
	"salary"	REAL DEFAULT 20000.0 CHECK("salary" > 0),
	"allowance"	REAL DEFAULT 0 CHECK("allowance" >= 0),
	"id_department"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_department") REFERENCES "departments"("id")
);

/* Дисциплины */
CREATE TABLE "disciplines" (
    "code" TEXT UNIQUE,
    "name"	TEXT NOT NULL,
    PRIMARY KEY("code")
);


/* Создать таблицу Группы и дисциплины */

/* Создать таблицу Преподаватели и группы */

/* Создать таблицу Преподаватели и дисциплины */

/* Создать таблицу Студенты и группы */

/* Добавление в таблицу "Учителя"*/

INSERT INTO teachers (name, surname, employment_date, position, salary, id_department)
VALUES
("Иван", "Петров", "2022-05-15", "Проффесор", 45000, (SELECT id FROM departments WHERE name = "Высшая математика")),
("Петр", "Иванов", "2019-12-12", "Доцент", 39000, (SELECT id FROM departments WHERE name = "Управление финансами")),
("Антон", "Сидоров", "2015-10-06", "Преподаватель", 32000, (SELECT id FROM departments WHERE name = "Ядерная физика")),
("Иван", "Иванов", "2012-05-15", "Проффесор", 45000, (SELECT id FROM departments WHERE name = "Банковское дело")),
("Петр", "Сидоров", "2017-12-12", "Профессор", 39000, (SELECT id FROM departments WHERE name = "Высшая математика")),
("Антон", "Петров", "2010-10-06", "Доцент", 32000, (SELECT id FROM departments WHERE name = "Управление финансами")),
("Петр", "Петров", "2003-12-12", "Профессор", 39000, (SELECT id FROM departments WHERE name = "Ядерная физика")),
("Антон", "Иванов", "2007-10-06", "Преподаватель", 32000, (SELECT id FROM departments WHERE name = "Банковское дело"))

/* Добавление в таблицу "Деканы" */
INSERT INTO deans (name, surname, email)
VALUES
("Иван", "Петров", "ia.petrov@education.ru"),
("Петр", "Иванов", "po.ivanov@education.ru");

/* Добавление в таблицу "Факультеты "*/
INSERT INTO faculties (facultie_name, id_dean)
VALUES
("Физико-математический", (SELECT SUM(financing) FROM departments WHERE departments.id_facultie = 1), 1),
("Экономический", (SELECT SUM(financing) FROM departments WHERE departments.id_facultie = 2), 2);

/* Добавление в таблицу "Кафедры" */
INSERT INTO departments (name, financing, id_head_department, id_facultie)
VALUES
("Высшая математика", 100000, 1, (SELECT id FROM faculties WHERE facultie_name = "Физико-математический")),
("Управление финансами", 150000, 2, (SELECT id FROM faculties WHERE facultie_name = "Экономический")),
("Банковское дело", 150000, 3, (SELECT id FROM faculties WHERE facultie_name = "Экономический")),
("Ядерная физика", 150000, 4, (SELECT id FROM faculties WHERE facultie_name = "Физико-математический"))

/* Добавление в таблицу "Группы" */
INSERT INTO groups (name, id_facultie)
VALUES
("P01", 1),
("P02", 2),
("P03", 1),
("P04", 2),
("P05", 1),
("P06", 2)

/* Добавление в таблицу "Дисциплины" */
INSERT INTO disciplines (code, name)
VALUES
("001", "Математика"),
("002", "Алгебра и геометрия"),
("003", "Бухгалтерия и учет"),
("004", "Экономика"),

