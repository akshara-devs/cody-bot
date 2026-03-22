import asyncio
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

from database.connection import close_pool, create_pool

load_dotenv()

# ── Validasi env variables sebelum bot nyala ──────────────────────────────────
REQUIRED_ENV = ["TOKEN_BOT", "DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"]

missing = [key for key in REQUIRED_ENV if not os.getenv(key)]
if missing:
    print(f"[❌] Environment variable berikut belum diisi di .env: {', '.join(missing)}")
    sys.exit(1)

TOKEN = os.getenv("TOKEN_BOT")

# ── Daftar semua cog yang akan di-load ────────────────────────────────────────
# Tambahkan cog baru di sini saat fitur baru dibuat
COGS = [
    "cogs.onboarding",
    "cogs.help",
]

# ── Setup intents ─────────────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"[✅] {bot.user} berhasil login!")
    print(f"[✅] Terhubung ke {len(bot.guilds)} server")
    try:
        synced = await bot.tree.sync()
        print(f"[✅] {len(synced)} slash command berhasil di-sync")
    except Exception as e:
        print(f"[❌] Gagal sync commands: {e}")


@bot.tree.command(name="ping", description="Cek apakah bot online")
async def ping(interaction: discord.Interaction) -> None:
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(
        f"🏓 Pong! Latency: **{latency}ms**", ephemeral=True
    )


async def main() -> None:
    async with bot:
        # Koneksi ke database sebelum bot start
        print("[⏳] Menghubungkan ke database...")
        await create_pool()
        print("[✅] Koneksi database berhasil!")

        # Load semua cog
        for cog in COGS:
            await bot.load_extension(cog)
            print(f"[✅] Cog '{cog}' berhasil di-load")

        try:
            await bot.start(TOKEN)
        finally:
            # Cleanup saat bot shutdown
            await close_pool()
            print("[👋] Bot shutdown, koneksi database ditutup.")


asyncio.run(main())