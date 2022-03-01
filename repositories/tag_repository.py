from typing import List
from configs.database import conn, cursor
from models.tag_model import Tag

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS tags (
        id integer primary key autoincrement,
        name text not null,
        color text not null unique
        )""")

create_table()

def insert_tag(tag: Tag):
    with conn:
        cursor.execute('INSERT INTO tags VALUES (NULL, :name, :color)', {
            'name': tag.name, 'color': tag.color
         })

def list_all() -> List[Tag]:
    cursor.execute('SELECT * FROM tags')
    results = cursor.fetchall()

    tags = [Tag(*result) for result in results]

    return tags
