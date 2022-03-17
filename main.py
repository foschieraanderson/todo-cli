import typer
from typing import Optional
from configs import __app_name__, __version__
from app import tasks, tags

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f'{__app_name__} v{__version__}')
        raise typer.exit()

app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        '--version',
        '-v',
        help='Show the application version and exit.',
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


app.add_typer(tasks.app, name='tasks')
app.add_typer(tags.app, name='tags')

if __name__ == '__main__':
    app()
