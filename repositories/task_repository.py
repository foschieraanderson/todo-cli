from datetime import datetime
from typing import List
from configs.database import conn, cursor
from models.task_model import Task

def create_table_task():
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id integer primary key autoincrement,
        title text not null,
        description text,
        tag text,
        done boolean,
        created_at datetime,
        completed_at datetime
    )''')

create_table_task()

def create(task: Task):
    with conn:
        cursor.execute('INSERT INTO tasks VALUES (NULL, :title, :description, :tag, :done, :created_at, :completed_at)', {
            'title': task.title,
            'description': task.description,
            'tag': task.tag,
            'done': task.done,
            'created_at': task.created_at,
            'completed_at': task.completed_at
        })

def update(key: int, **kwargs):
    with conn:
        args = {key: value for (key, value) in kwargs.items() if value }
        count = 1
        values = ''
        for arg in args.keys():
            values += f'{arg} = :{arg}, ' if count < len(args.keys()) else f'{arg} = :{arg}'
            count += 1
        query = f'UPDATE tasks SET {values} WHERE id = :key'
        args.update({'key': key})
        cursor.execute(query, args)

def complete(key: int, done: bool):
    completed = datetime.now() if done else None
    with conn:
        cursor.execute('UPDATE tasks SET done = :done, completed_at = :completed  WHERE id = :key', {
            'key': key, 'done': done, 'completed': completed
        })

def delete(key: int):
    with conn:
        conn.execute('DELETE FROM tasks WHERE id = :key', {'key': key})

def clear_all():
    with conn:
        cursor.execute('DROP TABLE tasks')
        create_table_task()

def list_all() -> List[Task]:
    with conn:
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        results = cursor.fetchall()

        tasks = [Task(*result) for result in results]

        return tasks
