from enum import Enum
from models.task_model import Task
from repositories.task_repository import create
import typer
from rich.console import Console

console = Console()
app = typer.Typer()

@app.command(short_help='Add an task')
def add(title: str, description: str = '', tag: str = ''):
    task = Task(id=None, title=title, description=description, tag=tag)
    create(task)
    console.print(f'Task {task}')
