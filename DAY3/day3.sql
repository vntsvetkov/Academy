/* запрос на создание записей в таблице clients */
INSERT INTO clients (name, surname, birthday, phone, email)
VALUES
("Иван", "Петров", "1980-05-15", "+7(958) 986-65-88", "is.petrov@qmail.com"),
("Петр", "Иванов", "1985-12-12", "+7(943) 956-56-56", "pe.ivanov@qmail.com"),
("Антон", "Сидоров", "1989-10-06", "+7(345) 456-45-22", "ai.sidorov@qmail.com")

/* Заменим пользователя с пересечением UNIQUE поля*/
REPLACE INTO clients (name, surname, birthday, phone, email)
VALUES
("Иван", "Петров", "1980-05-15", "+7(958) 986-65-88", "is.petrov@qmail.com")

/* Заменим пользователя с пересечением NOT NULL поля */

REPLACE INTO clients (name, surname, birthday, phone, email, status)
VALUES
("Сергей", "Васильев", "1982-05-15", "+7(958) 986-65-89", "sv.vasilev@qmail.com", NULL)

/* Сортировка по убыванию возраста клиента */
SELECT name, surname, date('now') - birthday AS age
FROM clients
ORDER BY date('now') - birthday DESC

/* Операторы фильтрации IN и NOT IN, BETWEEN, LIKE, IS NULL.*/

SELECT *
FROM clients
WHERE city NOT IN ('Москва', 'Ярославль')

/* выбрать всех клиентов с возрастом в промежутке от 30 до 40 */
SELECT *, date('now') - birthday AS age
FROM clients
WHERE date('now') - birthday  BETWEEN 30 AND 40

/* Выбрать всех клиентов у которых фамилия начинается на букву В*/
SELECT *, date('now') - birthday AS age
FROM clients
WHERE surname LIKE "В%"

/* Самый возрастной клиент*/
SELECT *, date('now') - birthday AS age
FROM clients
ORDER BY date('now') - birthday DESC
LIMIT 1