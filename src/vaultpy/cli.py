
from vaultpy.env_manager import env_manager
env_manager.load()
from rich.console import Console
from vaultpy.auth import login as login_user, whoami as whoami_user
from vaultpy import __version__
from vaultpy.vault import reset_vault
import typer

from vaultpy.vault import (
    add_password,
    list_passwords,
    remove_password,
    get_password,
)

app = typer.Typer(
    help="PyVault - CLI Secure Password Manager",
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)

console = Console()

@app.callback()
def callback():
    """PyVault CLI."""
    pass

@app.command("version", help="Show the current version. [v]")
@app.command("v", hidden=True)
def version():
    console.print(f"[bold green]PyVault[/bold green] v{__version__}")

@app.command("login", help="Login to your PyVault account. [li]")
@app.command("li", hidden=True)
def login():
    login_user()

@app.command("whoami", help="Show current user. [w]")
@app.command("w", hidden=True)
def whoami():
    whoami_user()

@app.command("logout", help="Logout from your PyVault account. [lo]")
@app.command("lo", hidden=True)
def logout():
    from vaultpy.session import session_manager
    session_manager.clear()
    console.print("[green]✓ Logged out successfully![/green]")

@app.command("source", help="Show the source via github. [s]")
@app.command("s", hidden=True)
def source():
    console.print("[bold green]Github:[/bold green] https://github.com/pawanhirumina/PyVault")

@app.command("ping", help="Test the Supabase connection. [p]")
@app.command("p", hidden=True)
def ping():
    from vaultpy.database import  get_client
    console.print("[green]✓ Connected to Supabase[/green]")


# CRUD Commands

@app.command("add", help="Save a new password. [a]")
@app.command("a", hidden=True)
def add():
    add_password()


@app.command("list", help="List saved passwords. [ls]")
@app.command("ls", hidden=True)
def list():
    list_passwords()


@app.command("remove", help="Remove a password. [rm]")
@app.command("rm", hidden=True)
def remove():
    remove_password()


@app.command("get", help="Show a saved password.")
def get():
    get_password()


@app.command(
    "reset",
    help="Delete all vault data and start fresh."
)
def reset():
    reset_vault()

if __name__ == "__main__":
    app()