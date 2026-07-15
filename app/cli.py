from rich.console import Console
import typer

app = typer.Typer(
    help="🔐 VaultPy - Secure Password Manager"
)

console = Console()


@app.callback()
def callback():
    """VaultPy CLI."""
    pass


@app.command()
def version():
    """Show the current version."""
    console.print("[bold green]VaultPy[/bold green] v0.1.0")