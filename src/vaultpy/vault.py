from rich.console import Console
from rich.table import Table

from vaultpy.database import get_client
from vaultpy.session import session_manager
from vaultpy.crypto import encrypt, decrypt, derive_key
from vaultpy.utils import get_salt

import questionary
import typer

from vaultpy.utils import (
    get_salt,
    CONFIG_DIR,
)
console = Console()


def get_authenticated_client():
    """
    Return Supabase client with the current user session attached.
    """

    session = session_manager.load()

    if not session:
        console.print("[red]Please login first.[/red]")
        raise typer.Exit()

    client = get_client()

    client.auth.set_session(
        session["access_token"],
        session["refresh_token"],
    )

    return client


def get_current_user_id():
    """
    Get current logged-in user's UUID.
    """

    client = get_authenticated_client()

    user = client.auth.get_user()

    if not user or not user.user:
        console.print("[red]Invalid session.[/red]")
        session_manager.clear()
        raise typer.Exit()

    return user.user.id


def add_password():
    """
    Save a new password.
    """

    name = typer.prompt("Service name")

    username = typer.prompt(
        "Username"
    )

    password = typer.prompt(
        "Password",
        hide_input=True
    )

    master_password = typer.prompt(
        "Master password",
        hide_input=True
    )


    # Create encryption key
    salt = get_salt()

    key = derive_key(
        master_password,
        salt
    )


    # Encrypt password before saving
    encrypted_password = encrypt(
        password,
        key
    )


    client = get_authenticated_client()


    client.table("passwords").insert(
        {
            "user_id": get_current_user_id(),
            "name": name,
            "username": username,
            "password": encrypted_password,
        }
    ).execute()


    console.print(
        "[green]✓ Password saved[/green]"
    )


def list_passwords():

    client = get_authenticated_client()

    result = (
        client
        .table("passwords")
        .select("id,name,username")
        .eq(
            "user_id",
            get_current_user_id()
        )
        .execute()
    )

    table = Table()

    table.add_column("#")
    table.add_column("Service")
    table.add_column("Username")

    for index, item in enumerate(result.data, start=1):
        table.add_row(
            str(index),
            item["name"],
            item["username"]
        )

    console.print(table)


def get_password():

    client = get_authenticated_client()

    result = (
        client
        .table("passwords")
        .select("*")
        .eq(
            "user_id",
            get_current_user_id()
        )
        .execute()
    )

    passwords = result.data

    if not passwords:
        console.print("[yellow]No passwords saved.[/yellow]")
        return

    selected_name = questionary.select(
        "Select password:",
        choices=[
            item["name"]
            for item in passwords
        ]
    ).ask()

    item = next(
        item for item in passwords
        if item["name"] == selected_name
    )

    master_password = typer.prompt(
        "Master password",
        hide_input=True
    )

    key = derive_key(
        master_password,
        get_salt()
    )

    try:
        decrypted = decrypt(
            item["password"],
            key
        )

    except ValueError as e:
        console.print(
            f"[red]✗ {e}[/red]"
        )
        return

    console.print(
        f"""
[green]Service:[/green] {item['name']}
[green]Username:[/green] {item['username']}
[green]Password:[/green] {decrypted}
"""
    )




def remove_password():

    """
    Delete a password.
    """

    password_id = typer.prompt(
        "Password ID"
    )


    client = get_authenticated_client()


    (
        client
        .table("passwords")
        .delete()
        .eq(
            "id",
            password_id
        )
        .eq(
            "user_id",
            get_current_user_id()
        )
        .execute()
    )


    console.print(
        "[green]✓ Password removed[/green]"
    )


def reset_vault():

    confirm = typer.confirm(
        "⚠️ This will permanently delete your vault. Continue?"
    )

    if not confirm:
        console.print(
            "[yellow]Reset cancelled.[/yellow]"
        )
        return


    client = get_authenticated_client()


    (
        client
        .table("passwords")
        .delete()
        .eq(
            "user_id",
            get_current_user_id()
        )
        .execute()
    )


    if CONFIG_DIR.exists():
        import shutil
        shutil.rmtree(CONFIG_DIR)


    console.print(
        "[green]✓ Vault reset successfully.[/green]"
    )

    confirm = typer.confirm(
        "⚠️ This will permanently delete your vault. Continue?"
    )

    if not confirm:
        console.print(
            "[yellow]Reset cancelled.[/yellow]"
        )
        return


    client = get_authenticated_client()


    (
        client
        .table("passwords")
        .delete()
        .eq(
            "user_id",
            get_current_user_id()
        )
        .execute()
    )


    # Remove local encryption files
    if CONFIG_DIR.exists():
        import shutil
        shutil.rmtree(CONFIG_DIR)


    console.print(
        "[green]✓ Vault reset successfully.[/green]"
    )