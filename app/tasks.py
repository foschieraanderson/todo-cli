from enum import Enum
from datetime import datetime 
from models.task_model import Task
from repositories.tag_repository import list_all as all_tags
from repositories.task_repository import clear_all, complete, create, delete, list_all
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
    task = Task(id=None, title=title, description=description, tag=tag.value)
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
    table.add_column('Tag', justify='center')
    table.add_column('Created', justify='center')
    table.add_column('Completed', justify='center')
    table.add_column('Done', justify='center')

    colors = {tag.name: tag.color for tag in all_tags() if tag}

    for task in tasks:
        pk = f'{task.id}'
        title = f'[strike]{task.title}[/]' if task.done else task.title
        tag = Padding(f'{task.tag}', (0,1), style=f'black on {colors[task.tag]}', expand=True)
        created = datetime.fromisoformat(task.created_at).strftime('%d/%m/%Y')
        completed = datetime.fromisoformat(task.completed_at).strftime('%d/%m/%Y') if task.done else '-----'
        done = '[green]✅[/]' if task.done else '[red]:negative_squared_cross_mark:[/]'

        table.add_row(pk, title, tag, created, completed, done)
    console.print(table)
