import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
from enum import Enum

from models.tag_model import Tag
from repositories.tag_repository import clear_all, create, delete, list_all, update

from time import sleep

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
    with console.status(f'[green] :floppy_disk: Adding [bold]tag {name}[/]...[/]'):
        try:
            tag = Tag(id=None, name=name, color=color)
            create(tag)
            show()
        except Exception:
            console.print_exception(show_locals=True)

@app.command(short_help='Remove an tag')
def rm(key: int):
    confirm = Confirm.ask(f'[red] :warning: Do you want to remove tag [bold]{key}[/] :question:[/]')
    if confirm:
        with console.status(f'[red]:wastebasket: Removing [bold]tag {key}[/]...[/]'):
            try:
                delete(key=key)
                show()
            except Exception:
                console.print_exception(show_locals=True)


@app.command(short_help='Update an tag')
def up(key: int, name: str = None, color: ColorsTag = None):
    with console.status(f'[cyan] :recycle: Updating [bold]tag {key}[/]...[/]'):
        try:
            update(key=key, name=name, color=color)
            show()
        except Exception:
            console.print_exception(show_locals=True)

@app.command(short_help='Remove all tags')
def clear():
    confirm = Confirm.ask(f'[white on red] :warning: Do you want to remove [bold]all[/] tags :question:[/]')
    if confirm:
        with console.status(f'[red] :wastebasket: Removing [bold]all tags[/]...[/]'):
            try:
                clear_all()
                show()
            except Exception:
                console.print_exception(show_locals=True)

@app.command(short_help='List all tags')
def show():
    sleep(1)
    try:
        tags = list_all()
        table = Table(title='My Tags', title_justify='center', show_header=True, header_style='bold blue')
        table.add_column('#', style='dim', width=4)
        table.add_column('Tag', min_width=20, justify='center')
        table.add_column('Color', min_width=10, justify='center')

        for tag in tags:
            table.add_row(str(tag.id), tag.name, f'[{tag.color}]{tag.color}[/{tag.color}]')
        console.clear()
        console.print(table)
    except Exception:
        console.print_exception(show_locals=True)

