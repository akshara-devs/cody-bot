import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

# Pool koneksi global — dibuat sekali, dipakai semua cog
_pool: asyncpg.Pool | None = None


async def create_pool() -> asyncpg.Pool:
    """Buat connection pool ke PostgreSQL."""
    global _pool
    _pool = await asyncpg.create_pool(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 5432)),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        min_size=2,
        max_size=10,
    )
    return _pool


async def close_pool() -> None:
    """Tutup pool saat bot shutdown."""
    global _pool
    if _pool:
        await _pool.close()
        _pool = None


def get_pool() -> asyncpg.Pool:
    """Ambil pool yang sudah dibuat. Raise error kalau belum diinisialisasi."""
    if _pool is None:
        raise RuntimeError("Database pool belum diinisialisasi. Panggil create_pool() dulu.")
    return _pool
