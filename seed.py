import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 5
NUMBER_TASKS = 30
STATUS = ['new', 'in progress', 'completed']


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []
    fake_emails = []
    fake_tasks = []
    fake_desc = []

    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append(fake_data.first_name() + ' ' + fake_data.last_name())
        fake_emails.append(fake_data.email())

    for _ in range(number_tasks):
        fake_tasks.append(fake_data.sentence())
        fake_desc.append(fake_data.paragraph())

    return fake_users, fake_emails, fake_tasks, fake_desc


def prepare_data(users, emails, tasks, descriptions) -> tuple():
    for_users = []
    i=0
    for user in users:
        for_users.append((user, emails[i]))
        i += 1
    for_tasks = []
    for task in tasks:
        for_tasks.append((task, choice(descriptions), randint(1, len(STATUS)), randint(1, NUMBER_USERS)))

    return for_users, for_tasks


def insert_data_to_db(users, tasks) -> None:
    with sqlite3.connect('project.db') as con:
        cur = con.cursor()

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)

        sql_to_status = """INSERT INTO status(name)
                              VALUES (?)"""
        status = [(name,) for name in STATUS]
        cur.executemany(sql_to_status, status)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                          VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)

        con.commit()


if __name__ == "__main__":
    users, tasks = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(users, tasks)
