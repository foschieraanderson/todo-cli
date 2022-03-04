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
        conn.execute('INSERT INTO tasks VALUES (NULL, :title,:description, :tag, :done, :created_at,:completed_at)', {
            'title': task.title,
            'description': task.description,
            'tag': task.tag,
            'done': task.done,
            'created_at': task.created_at,
            'completed_at': task.completed_at
        })
