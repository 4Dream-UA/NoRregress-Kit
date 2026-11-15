from importlib.metadata import PackageNotFoundError, version

import typer


def get_version() -> str:
    try:
        return version("noregress-kit")
    except PackageNotFoundError:
        return "Package not found. Please ensure 'noregress-kit' is installed."


app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        typer.echo(get_version())
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the version of the application.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """
    noregress-kit: A CLI tool for managing regression tests.
    """
    pass
