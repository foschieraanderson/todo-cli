import typer
from rich.console import Console
from rich.table import Table
from enum import Enum
from typing import List

from models.tag_model import Tag
from repositories.tag_repository import insert_tag, list_all

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
    console.print(f'[{color}]{name}[/{color}]')
    tag = Tag(id=None, name=name, color=color)
    insert_tag(tag)
    show()

@app.command(short_help='List all tags')
def show():
    tags = list_all()
    table = Table(title='Tags', title_justify='center', show_header=True, header_style='bold blue')
    table.add_column('#', style='dim', width=4)
    table.add_column('Tag', min_width=20, justify='center')
    table.add_column('Color', min_width=10, justify='center')

    for tag in tags:
        table.add_row(str(tag.id), tag.name, f'[{tag.color}]{tag.color}[/{tag.color}]')
    console.print(table)

