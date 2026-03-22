import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

# Load token dari file .env
load_dotenv()
TOKEN = os.getenv("TOKEN_BOT")

# Intents = izin apa saja yang dimiliki bot
intents = discord.Intents.default()
intents.message_content = True  # Izin baca isi pesan
intents.members = True          # Izin akses data member server

# Buat instance bot
# command_prefix = prefix untuk text command (jarang dipakai, kita fokus ke slash command)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Berhasil Login!")
    print(f"Terhubung ke {len(bot.guilds)} server")
    try:
        synced = await bot.tree.sync()
        print(f"[ V ] {len(synced)} slash command berhasil di-sync")
    except Exception as e:
        print(f"[ X ] Gagal sync commands: {e}")

# TEST BOT ONLINE
@bot.tree.command(name="ping", description="Cek apakah bot online")
async def ping(interaction: discord.Interaction):
    """Slash command pertama kita — untuk test bot online."""
    latency = round(bot.latency * 1000)  # Konversi ke millisecond
    await interaction.response.send_message(
        f"Pong! Bot online dengan latency {latency}ms"
    )

async def main():
    async with bot:
        await bot.load_extension("cogs.project")
        await bot.start(TOKEN)

asyncio.run(main())