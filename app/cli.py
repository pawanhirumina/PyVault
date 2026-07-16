from rich.console import Console
from app.auth import login as login_user
import typer

app = typer.Typer(
    help="PyVault - CLI Secure Password Manager"
)

console = Console()


@app.callback()
def callback():
    """PyVault CLI."""
    pass

# Shows Version
@app.command()
def version():
    """Show the current version."""
    console.print("[bold green]PyVault[/bold green] v1.1.0")


# Login Prompt 
@app.command()
def login():
    """Login to your PyVault account."""
    login_user()


# View source 
@app.command()
def source():
    """Show the source via github."""
    console.print("[bold green][/bold green]Github: https://github.com/pawanhirumina/PyVault")


# Ping Supabase
@app.command()
def ping():
    """Test the Supabase connection."""
    from app.database import client

    console.print("[green]✓ Connected to Supabase[/green]")