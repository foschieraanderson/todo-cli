import typer
from app import tags

app = typer.Typer()

app.add_typer(tags.app, name='tags')

if __name__ == "__main__":
    app()
