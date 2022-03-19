from time import sleep
from enum import Enum
from utils.helpers import date_format
from models.task_model import Task
from repositories.tag_repository import list_all as all_tags
from repositories.task_repository import clear_all, complete, create, delete, list_all, update
import typer
from rich.console import Console
from rich.prompt import Confirm
from rich.table import Table
from rich.padding import Padding

console = Console()
app = typer.Typer()

tag_options = {tag.name: tag.name for tag in all_tags()}
tags = Enum('Tags', tag_options)

@app.command(short_help='Add an task')
def add(title: str, description: str = '', tag: tags = None):
    with console.status(f'[green] :floppy_disk: Adding [bold]tag {title}[/]...[/]'):
        try:
            tag_value = tag.value if tag else ''
            task = Task(id=None, title=title, description=description, tag=tag_value)
            create(task)
            show()
        except Exception:
            console.print_exception(show_locals=True)

@app.command(short_help='Update an task')
def up(key: int, title: str = None, description: str = '', tag: tags = None):
    with console.status(f'[cyan] :recycle: Updating [bold]tag {key}[/]...[/]'):
        try:
            tag_value = tag.value if tag else ''
            update(key=key, title=title, description=description, tag=tag_value)
            show()
        except Exception:
            console.print_exception(show_locals=True)

@app.command(short_help='Complete an task')
def done(key: int, done: bool = True):
    with console.status(f'[cyan] :recycle: Completing [bold]tag {key}[/]...[/]'):
        try:
            complete(key=key, done=done)
            show()
        except Exception:
            console.print_exception(show_locals=True)

@app.command(short_help='Remove an task')
def rm(key: int):
    confirm = Confirm.ask(f'[red] :warning: Do you want to remove task [bold]{key}[/] :question:[/]')
    if confirm:
        with console.status(f'[red]:wastebasket: Removing [bold]tag {key}[/]...[/]'):
            try:
                delete(key=key)
                show()
            except Exception:
                console.print_exception(show_locals=True)

@app.command(short_help='Remove all tasks')
def clear():
    confirm = Confirm.ask(f'[white on red] :warning: Do you want to remove [bold]all[/] tasks :question:[/]')
    if confirm:
        with console.status(f'[red] :wastebasket: Removing [bold]all tags[/]...[/]'):
            try:
                clear_all()
                show()
            except Exception:
                console.print_exception(show_locals=True)

@app.command(short_help='List all tasks')
def show():
    sleep(1)
    try:
        tasks = list_all()
        table = Table(title='My Tasks', title_justify='center', show_header=True, header_style='bold blue')
        table.add_column('#', style='dim')
        table.add_column('Title', min_width=20, justify='left')
        table.add_column('Tag', justify='center')
        table.add_column('Created', justify='center')
        table.add_column('Completed', justify='center')
        table.add_column('Done', justify='center')

        colors = {tag.name: tag.color for tag in all_tags()}

        for task in tasks:
            pk = f'{task.id}'
            title = f'[strike]{task.title}[/]' if task.done else task.title
            tag = Padding(
                f'{task.tag}',
                (0,1),
                style=f'black on {colors[task.tag]}',
                expand=True
            ) if task.tag else '-----'
            created = date_format(task.created_at)
            completed = date_format(task.completed_at) if task.done else '-----'
            done = '[green]✅[/]' if task.done else '[red]:negative_squared_cross_mark:[/]'

            table.add_row(pk, title, tag, created, completed, done)
        console.clear()
        console.print(table)
    except Exception:
        console.print_exception(show_locals=True)
