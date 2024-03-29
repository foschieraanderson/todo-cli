from typing import List, Optional
from configs.database import connection
from todo.models.tag_model import Tag

def create_table_tag():
    """Create table tags if not exists"""
    with connection() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS tags (
            id integer primary key autoincrement,
            name text not null unique,
            color text not null 
            )""")

create_table_tag()

def create(tag: Tag):
    """Add a tag"""
    with connection() as cursor:
        cursor.execute('INSERT INTO tags VALUES (NULL, :name, :color)', {
            'name': tag.name, 'color': tag.color
         })

def delete(key: int):
    """Delete a tag"""
    with connection() as cursor:
        cursor.execute('DELETE FROM tags WHERE id = :key', {'key': key})

def update(key: int, name: str, color: str):
    """Update a tag"""
    with connection() as cursor:
        if name and color:
            cursor.execute('UPDATE tags SET name = :name, color = :color WHERE id = :key', {
                'key':key, 'name': name, 'color': color
            })
        elif name:
            cursor.execute('UPDATE tags SET name = :name WHERE id = :key', {
                'key':key, 'name': name
            })
        elif color:
            cursor.execute('UPDATE tags SET color = :color WHERE id = :key', {
                'key':key, 'color': color
            })

def clear_all():
    """Delete all tags"""
    with connection() as cursor:
        cursor.execute('DROP TABLE tags')
        create_table_tag()

def list_all() -> List[Tag]:
    """List all tags"""
    with connection() as cursor:
        cursor.execute('SELECT * FROM tags')
        results = cursor.fetchall()

        tags = [Tag(*result) for result in results]

        return tags
