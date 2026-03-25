from typing import Any

from api.client import request_json


async def get_user_by_discord_id(discord_user_id: str) -> dict[str, Any] | None:
    """Fetch a user from the API by Discord user id."""
    return await request_json("GET", f"/users/discord/{discord_user_id}")


async def create_user(discord_user_id: str) -> dict[str, Any] | None:
    """Create a user through the API."""
    payload = {"discord_user_id": discord_user_id}
    return await request_json("POST", "/users", json=payload)
