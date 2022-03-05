import typer
from app import tasks, tags

app = typer.Typer()

app.add_typer(tasks.app, name='tasks')
app.add_typer(tags.app, name='tags')

if __name__ == '__main__':
    app()
