import sqlite3

def execute_query(sql: str, *args) -> list:
    with sqlite3.connect('project.db') as con:
        cur = con.cursor()
        cur.execute(sql, args)
        return cur.fetchall()

sql_1 = """
SELECT * FROM tasks t WHERE user_id = ?;
"""

sql_2 = """
SELECT t.id, t.title, t.status_id, s.name
FROM tasks t
JOIN status s on t.status_id = s.id
WHERE s.name = ?
"""

sql_3 = """
UPDATE tasks SET status_id = 2 WHERE id = ?
"""

sql_4 = """
SELECT *
FROM users u
WHERE u.id NOT IN (SELECT t.user_id FROM tasks t WHERE t.user_id = u.id)
"""

sql_5 = """
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ("problem", "description of problem", 1, ?)
"""

sql_6 = """
SELECT *
FROM tasks t
JOIN status s on t.status_id = s.id
WHERE s.name != ?
"""

sql_7 = """
DELETE FROM tasks WHERE id=?
"""

sql_8 = """
SELECT * FROM users u WHERE email LIKE ?
"""

sql_9 = """
UPDATE users SET fullname = "John Dow" WHERE id = ?
"""

sql_10 = """
SELECT s.name, COUNT(t.id) FROM tasks t JOIN status s on t.status_id = s.id
GROUP BY t.status_id
"""

sql_11 = """
SELECT * FROM tasks t
JOIN users u on t.user_id = u.id
WHERE u.email LIKE ?
"""

sql_12 = """
SELECT * FROM tasks t WHERE description = "" OR description ISNULL
"""

sql_13 = """
SELECT u.fullname, t.id as id_task, t.title, t.status_id
FROM users u
INNER JOIN tasks t on u.id = t.user_id
INNER JOIN status s on t.status_id = s.id
WHERE s.name = 'in progress'
ORDER BY u.id
"""

sql_14 = """
SELECT u.fullname, COUNT(t.id) as tasks FROM users u
LEFT JOIN tasks t on u.id = t.user_id
GROUP BY u.id
"""


if __name__ == "__main__":
    # print(execute_query(sql_1, 4)) # виведе всі завдання для користувача з id = 4
    # print(execute_query(sql_2, 'new')) # виведе всі завдання з статусом 'new'
    # print("OK" if len(execute_query(sql_3, 29)) == 0 else "FAIL") # змінить статус завдання з id = 29 на 'in progress'
    # print(execute_query(sql_4)) # виведе всіх користувачів, які не мають завдань
    # print("OK" if len(execute_query(sql_5, 4)) == 1 else "FAIL") # додати завдання для користувача з id = 4execute_query(sql_5, 4)) # додати завдання для користувача з id = 4
    # print(execute_query(sql_6, 'completed')) # виведе всі завдання, які не мають статусу 'completed'
    # print("OK" if len(execute_query(sql_7, 33)) == 0 else "FAIL") # видалити завдання з id = 33
    # print(execute_query(sql_8, '%.org')) # виведе всіх користувачів, чий email закінчується на .org
    # print("OK" if len(execute_query(sql_9, 1)) == 0 else "FAIL") # змінити повне ім'я користувача з id = 1 на "John Dow"
    # print(execute_query(sql_10)) # виведе кількість завдань для кожного статусу
    # print(execute_query(sql_11, '%@example.net')) # виведе всі завдання користувачів, чий email закінчується на @example.net
    # print(execute_query(sql_12)) # виведе всі завдання без опису
    # print(execute_query(sql_13)) # виведе всі завдання з статусом 'in progress' в порядку зростання id користувача
    print(execute_query(sql_14)) # виведе кількість завдань для кожного користувача


    


