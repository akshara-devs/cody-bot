import discord
from discord import app_commands
from discord.ext import commands

from utils.embeds import error_embed


class Onboarding(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="register", description="Daftarkan dirimu ke CODY Bot")
    async def register(self, interaction: discord.Interaction) -> None:
        """
        Flow:
        1. Defer response
        2. Tampilkan pesan bahwa user sudah terdaftar
        """
        # Defer dulu supaya response tetap aman dari timeout Discord
        await interaction.response.defer(ephemeral=True)

        embed = error_embed(
            title="Sudah Terdaftar",
            description=(
                "Kamu sudah terdaftar di CODY Bot sebelumnya.\n"
                "Ketik `/help` untuk melihat semua command yang tersedia."
            ),
        )
        await interaction.followup.send(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Onboarding(bot))
