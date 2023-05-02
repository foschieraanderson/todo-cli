from time import sleep
from enum import Enum
from datetime import datetime
from typing import List

import typer
from rich.console import Console
from rich.table import Table
from rich.padding import Padding

from todo.repositories.tag_repository import list_all as all_tags
from todo.models.task_model import Task

console = Console()

def date_format(date: str) -> str:
    """Format datetime to date"""
    date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
    return date

def get_tags() -> Enum:
    """Return tag options"""
    tag_options = {tag.name: tag.name for tag in all_tags()}
    tags = Enum('Tags', tag_options)
    return tags


def show_table_tasks(tasks: List[Task]) -> None:
    """List all tasks in table"""
    sleep(1)
    if tasks:
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
            done = '[green]:heavy_check_mark:[/]' if task.done else '[red]:heavy_multiplication_x:[/]'

            table.add_row(pk, title, tag, created, completed, done)
        console.clear()
        console.print(table)
    else:
        console.print('[i]Nenhuma task encontrada...[/i]')
