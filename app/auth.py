import typer
from rich.console import Console

from app.database import client

console = Console()


def login() -> None:
    """Authenticate with Supabase."""

    email = typer.prompt("Email")
    password = typer.prompt(
        "Password",
        hide_input=True,
    )

    try:
        response = client.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        )

        console.print(
            f"[green]✓ Logged in successfully![/green] "
            f"Welcome [bold]{response.user.email}[/bold]"
        )

    except Exception as e:
        console.print(f"[bold red]Login failed[/bold red]")
        console.print(str(e))