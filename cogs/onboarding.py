import discord
from discord import app_commands
from discord.ext import commands

from database.connection import get_pool
from database.queries.user import create_user, get_user_by_discord_id
from utils.embeds import error_embed, onboarding_embed


class Onboarding(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="register", description="Daftarkan dirimu ke CODY Bot")
    async def register(self, interaction: discord.Interaction) -> None:
        """
        Flow:
        1. Defer response (proses DB bisa > 3 detik, Discord timeout di 3 detik)
        2. Cek apakah user sudah terdaftar
        3. Kalau belum → buat user baru + inisialisasi streak & currencies
        4. Kirim embed sesuai hasilnya
        """
        # Defer dulu — kasih waktu lebih untuk proses DB
        await interaction.response.defer(ephemeral=True)

        discord_user_id = str(interaction.user.id)
        pool = get_pool()

        # Cek duplikasi
        existing_user = await get_user_by_discord_id(pool, discord_user_id)
        if existing_user:
            embed = error_embed(
                title="Sudah Terdaftar",
                description=(
                    "Kamu sudah terdaftar di CODY Bot sebelumnya.\n"
                    "Ketik `/help` untuk melihat semua command yang tersedia."
                ),
            )
            await interaction.followup.send(embed=embed, ephemeral=True)
            return

        # Buat user baru
        await create_user(pool, discord_user_id)

        embed = onboarding_embed(interaction.user)
        await interaction.followup.send(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Onboarding(bot))
