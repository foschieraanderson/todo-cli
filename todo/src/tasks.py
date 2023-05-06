import typer
from rich.console import Console
from rich.prompt import Confirm

from todo.models.task_model import Task
from todo.repositories.task_repository import clear_all, complete, create, delete, list_all, list_one, update
from todo.utils.helpers import get_tags, show_table_tasks

console = Console()
app = typer.Typer()

@app.command(short_help='Add an task')
def add(title: str, description: str = '', tag: get_tags() = None):
    with console.status(f'[green] :floppy_disk: Adding [bold]tag {title}[/]...[/]'):
        try:
            tag_value = tag.value if tag else ''
            task = Task(id=None, title=title, description=description, tag=tag_value)
            create(task)
            show()
        except Exception:
            console.print_exception(show_locals=True)

@app.command(short_help='Update an task')
def up(key: int, title: str = None, description: str = '', tag: get_tags() = None):
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
        with console.status(f'[red] :wastebasket: Removing [bold]all tasks[/]...[/]'):
            try:
                clear_all()
                show()
            except Exception:
                console.print_exception(show_locals=True)

@app.command(short_help='List tasks')
def show():
    try:
        tasks = list_all()
        show_table_tasks(tasks = tasks)
    except:
        console.print_exception(show_locals=True)
