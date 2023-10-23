import sqlite3

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

def update_task_by_name(task_name):
    with sqlite3.connect('todo.db') as conn:
        sql = 'UPDATE tasks SET status = 1 WHERE Task = ?'
        cur = conn.cursor()
        cur.execute(sql, (task_name,))
        conn.commit()

def delete_task(task_id):
    with sqlite3.connect('todo.db') as conn:
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (task_id,))
        conn.commit()
    
def delete_task_by_name(task_name):
    with sqlite3.connect('todo.db') as conn:
        sql = 'DELETE FROM tasks WHERE task=?'
        cur = conn.cursor()
        cur.execute(sql, (task_name,))
        conn.commit()

def delete_all_done():
    with sqlite3.connect('todo.db') as conn:
        sql = 'DELETE FROM tasks WHERE status = 1'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

def main():
    create_table()
    print('(1) Add new Task')
    print('(2) View Tasks')
    print('(3) Done Task (by ID)')
    print('(4) Done Task (by Name)')
    print('(5) Delete Task (by ID)')
    print('(6) Delete Task (by Name)')
    print('(7) Delete all done Tasks')
    do = int(input('Select what to do: '))
    if do == 1:
        task = input('Insert task name: ')
        add_task(task)
    elif do == 2:
        view_tasks()
    elif do == 3:
        task_id = int(input('Insert Id of done Task '))
        update_task(task_id)
    elif do == 4:
        task_name = input('Insert Name of done Task ')
        update_task_by_name(task_name)
    elif do == 5:
        task_id = int(input('Insert Id of Task to delete '))
        delete_task(task_id)
    elif do == 6:
        task_name = input('Insert Name of Task to delete ')
        delete_task_by_name(task_name)
    elif do == 7:
        delete_all_done()


if __name__ == 'main':
  main()
