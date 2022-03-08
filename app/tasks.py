from enum import Enum
from datetime import datetime 
from models.task_model import Task
from repositories.task_repository import clear_all, complete, create, delete, list_all
import typer
from rich.console import Console
from rich.prompt import Confirm
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command(short_help='Add an task')
def add(title: str, description: str = '', tag: str = ''):
    task = Task(id=None, title=title, description=description, tag=tag)
    create(task)
    show()

@app.command(short_help='Complete an task')
def done(key: int, done: bool = True):
    complete(key=key, done=done)
    show()

@app.command(short_help='Remove an task')
def rm(key: int):
    confirm = Confirm.ask(f'[red] :warning: Do you want to remove task [bold]{key}[/] :question:[/]')
    if confirm:
        delete(key=key)
        show()

@app.command(short_help='Remove all tasks')
def clear():
    confirm = Confirm.ask(f'[white on red] :warning: Do you want to remove [bold]all[/] tasks :question:[/]')
    if confirm:
        clear_all()
        show()

@app.command(short_help='List all tasks')
def show():
    tasks = list_all()
    table = Table(title='My Tasks', title_justify='center', show_header=True, header_style='bold blue')
    table.add_column('#', style='dim')
    table.add_column('Title', min_width=20, justify='left')
    table.add_column('Tag', min_width=15, justify='left')
    table.add_column('Created', justify='left')
    table.add_column('Completed', justify='left')
    table.add_column('Done', justify='center')

    for task in tasks:
        done = '[green]✅[/]' if task.done else '[red]:negative_squared_cross_mark:[/]'
        created = datetime.fromisoformat(task.created_at).strftime('%d/%m/%Y')
        completed = datetime.fromisoformat(task.completed_at).strftime('%d/%m/%Y') if task.completed_at else None
        table.add_row(str(task.id), task.title, task.tag, created, completed, done)
    console.print(table)
