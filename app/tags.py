import typer
from rich.console import Console
from rich.table import Table
from enum import Enum
from typing import List

from models.tag_model import Tag
from repositories.tag_repository import create, delete, list_all

console = Console()
app = typer.Typer()

class ColorsTag(str, Enum):
    white   = 'white'
    green   = 'green'
    blue    = 'blue'
    red     = 'red'
    yellow  = 'yellow'
    cyan    = 'cyan'
    magenta = 'magenta'

@app.command(short_help='Add an tag')
def add(name: str, color: ColorsTag = ColorsTag.white):
    tag = Tag(id=None, name=name, color=color)
    create(tag)
    show()

@app.command(short_help='Remove an tag')
def rm(key: int):
    console.print("KEY: ", key)
    delete(key=key)
    show()

@app.command(short_help='List all tags')
def show():
    tags = list_all()
    table = Table(title='My Tags', title_justify='center', show_header=True, header_style='bold blue')
    table.add_column('#', style='dim', width=4)
    table.add_column('Tag', min_width=20, justify='center')
    table.add_column('Color', min_width=10, justify='center')

    for tag in tags:
        table.add_row(str(tag.id), tag.name, f'[{tag.color}]{tag.color}[/{tag.color}]')
    console.print(table)

