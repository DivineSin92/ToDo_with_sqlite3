import sqlite3
from sqlite3 import Error

def create_table():
    with sqlite3.connect('todo.db') as conn:
        sql_create_tasks_table =  '''CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            task text NOT NULL,
            status INTEGER DEFAULT 0
        )'''
        c = conn.cursor()
        c.execute(sql_create_tasks_table)
        print('table created')

def add_task(task):
    with sqlite3.connect('todo.db') as conn:
        sql = ' INSERT INTO tasks(task) VALUES(?)'
        cur = conn.cursor()
        cur.execute(sql, (task,))
        return cur.lastrowid

def view_tasks():
    with sqlite3.connect('todo.db') as conn:
        sql = 'SELECT * FROM tasks'
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Task: {row[1]}, Status: {row[2]}')

def update_task(task_id):
    with sqlite3.connect('todo.db') as conn:
        sql = 'UPDATE tasks SET status = 1 WHERE id = ?'
        cur = conn.cursor()
        cur.execute(sql, (task_id,))
        conn.commit()


def main():
    create_table()
    print('(1) Add new Task')
    print('(2) View Tasks')
    print('(3) Done Task (by ID)')
    do = int(input('Select what to do: '))
    if do == 1:
        task = input('Insert task name: ')
        add_task(task)
    elif do == 2:
        view_tasks()
    elif do == 3:
        task_id = int(input('Insert Id of done Task '))
        update_task(task_id)


if __name__ == 'main':
  main()
