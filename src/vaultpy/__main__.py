from .cli import app
from .env_manager import env_manager

env_manager.load()

if __name__ == "__main__":
    app()