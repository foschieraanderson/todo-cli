from enum import Enum
from models.task_model import Task
from repositories.task_repository import clear_all, complete, create, delete, list_all
import typer
from rich.console import Console
from rich.prompt import Confirm

console = Console()
app = typer.Typer()

@app.command(short_help='Add an task')
def add(title: str, description: str = '', tag: str = ''):
    task = Task(id=None, title=title, description=description, tag=tag)
    create(task)
    console.print(f'Task {task}')

@app.command(short_help='Complete an task')
def done(key: int, done: bool = True):
    complete(key=key, done=done)
    console.print(f'KEY: {key} - DONE: {done}')

@app.command(short_help='Remove an task')
def rm(key: int):
    confirm = Confirm.ask(f'[red] :warning: Do you want to remove task [bold]{key}[/] :question:[/]')
    if confirm:
        delete(key=key)
        console.print('KEY: ', key)

@app.command(short_help='Remove all tasks')
def clear():
    confirm = Confirm.ask(f'[white on red] :warning: Do you want to remove [bold]all[/] tasks :question:[/]')
    if confirm:
        clear_all()

@app.command(short_help='List all tasks')
def show():
    tasks = list_all()
    console.print('TASKS: ', tasks)
