import os

from supabase import Client, create_client

from vaultpy.config import settings

def get_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url:
        raise RuntimeError("SUPABASE_URL is missing.")

    return create_client(url, key)