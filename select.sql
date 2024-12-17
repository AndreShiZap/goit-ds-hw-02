SELECT * FROM tasks t WHERE user_id = 2

SELECT t.id, t.title, t.status_id, s.name
FROM tasks t
JOIN status s on t.status_id = s.id
WHERE s.name = 'new'

UPDATE tasks SET status_id = 2 WHERE id = 29

SELECT *
FROM users u
WHERE u.id NOT IN (SELECT t.user_id FROM tasks t WHERE t.user_id = u.id)

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ("problem", "description of problem", 1, 4)

SELECT *
FROM tasks t
JOIN status s on t.status_id = s.id
WHERE s.name != 'completed'

DELETE FROM tasks WHERE id=32

SELECT * FROM users u WHERE email LIKE '%.org'

UPDATE users SET fullname = "John Snow" WHERE id = 1

SELECT s.name, COUNT(t.id) FROM tasks t JOIN status s on t.status_id = s.id
GROUP BY t.status_id

SELECT * FROM tasks t
JOIN users u on t.user_id = u.id
WHERE u.email LIKE '%@example.net'

SELECT * FROM tasks t WHERE description = "" OR description ISNULL

SELECT u.fullname, t.id as id_task, t.title, t.status_id
FROM users u
INNER JOIN tasks t on u.id = t.user_id
INNER JOIN status s on t.status_id = s.id
WHERE s.name = 'in progress'
ORDER BY u.id

SELECT u.fullname, COUNT(t.id) as tasks FROM users u
LEFT JOIN tasks t on u.id = t.user_id
GROUP BY u.id