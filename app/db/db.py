from app.config import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.postgres_url.unicode_string()
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models"
            ],
            "default_connection": "default",
        }
    },
}