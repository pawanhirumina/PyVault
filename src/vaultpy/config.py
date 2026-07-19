from dataclasses import dataclass
import os

from os import getenv




@dataclass(frozen=True)
class Settings:
    supabase_url: str
    supabase_key: str


settings = Settings(
    supabase_url = os.getenv("SUPABASE_URL"),
    supabase_key = os.getenv("SUPABASE_KEY")
)