from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    supabase_url: str
    supabase_key: str


settings = Settings(
    supabase_url=getenv("SUPABASE_URL", ""),
    supabase_key=getenv("SUPABASE_KEY", ""),
)