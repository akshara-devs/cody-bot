import os
from typing import Any

import aiohttp
from dotenv import load_dotenv

load_dotenv()

_session: aiohttp.ClientSession | None = None


async def create_api_session() -> aiohttp.ClientSession:
    """Create a shared API session for the bot."""
    global _session
    if _session is None or _session.closed:
        timeout = aiohttp.ClientTimeout(total=30)
        _session = aiohttp.ClientSession(
            base_url=os.getenv("API_BASE_URL", "").rstrip("/"),
            timeout=timeout,
        )
    return _session


async def close_api_session() -> None:
    """Close the shared API session during shutdown."""
    global _session
    if _session and not _session.closed:
        await _session.close()
    _session = None


def get_api_session() -> aiohttp.ClientSession:
    """Return the initialized API session."""
    if _session is None or _session.closed:
        raise RuntimeError("API session belum diinisialisasi. Panggil create_api_session() dulu.")
    return _session


async def request_json(method: str, path: str, **kwargs: Any) -> Any:
    """Send an HTTP request and decode the JSON response when present."""
    session = get_api_session()
    async with session.request(method, path, **kwargs) as response:
        if response.status == 404:
            return None

        response.raise_for_status()

        if response.content_type == "application/json":
            return await response.json()

        text = await response.text()
        return text or None
