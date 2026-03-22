from asyncpg import Pool, Record


async def get_user_by_discord_id(pool: Pool, discord_user_id: str) -> Record | None:
    """Cari user berdasarkan discord_user_id. Return None kalau tidak ditemukan."""
    return await pool.fetchrow(
        "SELECT * FROM users WHERE discord_user_id = $1",
        discord_user_id,
    )


async def create_user(pool: Pool, discord_user_id: str) -> Record:
    """
    Insert user baru dan otomatis inisialisasi streak & currencies.
    Semua operasi dalam satu transaksi — kalau salah satu gagal, semua di-rollback.
    """
    async with pool.acquire() as conn:
        async with conn.transaction():
            user = await conn.fetchrow(
                """
                INSERT INTO users (discord_user_id)
                VALUES ($1)
                RETURNING *
                """,
                discord_user_id,
            )

            # Inisialisasi streak kosong
            await conn.execute(
                "INSERT INTO streak (user_id) VALUES ($1)",
                user["id"],
            )

            # Inisialisasi dompet kosong
            await conn.execute(
                "INSERT INTO currencies (user_id) VALUES ($1)",
                user["id"],
            )

    return user
