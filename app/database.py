from supabase import Client, create_client

from app.config import settings

if not settings.supabase_url:
    raise RuntimeError("SUPABASE_URL is missing.")

if not settings.supabase_key:
    raise RuntimeError("SUPABASE_KEY is missing.")


client: Client = create_client(
    settings.supabase_url,
    settings.supabase_key,
)