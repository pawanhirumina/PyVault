import typer
from rich.console import Console

from vaultpy.database import get_client
from vaultpy.session import session_manager

console = Console()


def login() -> None:
    """Authenticate with Supabase."""

    email = typer.prompt("Email")
    password = typer.prompt(
        "Password",
        hide_input=True
    )

    try:
        client = get_client()

        response = client.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        )

        session_manager.save(
            response.session.model_dump(mode="json")
        )

        console.print(
            f"[green]✓ Logged in successfully![/green] "
            f"Welcome [bold]{response.user.email}[/bold]"
        )

    except Exception as e:
        console.print("[bold red]Login failed[/bold red]")
        console.print(str(e))


def whoami() -> None:
    """Show the current logged-in user."""

    session = session_manager.load()

    if not session:
        console.print("[yellow]You are not logged in.[/yellow]")
        return

    try:
        client = get_client()

        client.auth.set_session(
            session["access_token"],
            session["refresh_token"],
        )

        user = client.auth.get_user()

        if not user or not user.user:
            console.print("[red]Session expired or invalid.[/red]")
            session_manager.clear()
            return

        console.print(
            f"[green]✓ Logged in as:[/green] "
            f"[bold]{user.user.email}[/bold]"
        )

    except Exception as e:
        console.print("[red]Session expired or invalid.[/red]")
        console.print(str(e))
        session_manager.clear()


def logout() -> None:
    """Logout the current user."""

    session = session_manager.load()

    if not session:
        console.print("[yellow]You are not logged in.[/yellow]")
        return

    try:
        client = get_client()

        client.auth.sign_out()

        session_manager.clear()

        console.print("[green]✓ Logged out successfully![/green]")

    except Exception as e:
        console.print("[red]Logout failed.[/red]")
        console.print(str(e))