import discord
from discord import app_commands
from discord.ext import commands

BOT_VERSION = "0.1.0"
BOT_AUTHOR = "akshara-devs"

# Semua command dikelompokkan per kategori
# Tambahkan command baru di sini saat fitur baru dibuat
COMMANDS = [
    {
        "category": "🔧 General",
        "items": [
            ("/ping", "Cek apakah bot online dan lihat latency"),
            ("/help", "Tampilkan pesan bantuan ini"),
            ("/register", "Daftarkan dirimu ke CODY Bot"),
        ],
    },
    {
        "category": "🗂️ Project",
        "items": [
            ("/project new", "Buat proyek baru *(coming soon)*"),
            ("/project list", "Lihat semua proyekmu *(coming soon)*"),
            ("/project delete", "Hapus proyek *(coming soon)*"),
        ],
    },
    {
        "category": "⏱️ Coworking",
        "items": [
            ("/cowork start", "Mulai sesi coworking *(coming soon)*"),
            ("/cowork stop", "Selesaikan sesi coworking *(coming soon)*"),
        ],
    },
    {
        "category": "🔥 Streak & 🪙 Currency",
        "items": [
            ("/streak", "Lihat streak harianmu *(coming soon)*"),
            ("/wallet", "Lihat jumlah koin kamu *(coming soon)*"),
        ],
    },
    {
        "category": "📊 Statistik",
        "items": [
            ("/stats", "Lihat statistik coworking kamu *(coming soon)*"),
        ],
    },
]


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="help", description="Tampilkan semua command CODY Bot")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="📖 CODY Bot — Command List",
            description=(
                "CODY adalah coworking space bot untuk membantu kamu "
                "tetap produktif dan konsisten di Discord.\n\u200b"
            ),
            color=0x3498DB,
        )

        # Tambahkan tiap kategori sebagai field
        for group in COMMANDS:
            command_list = "\n".join(
                f"`{cmd}` — {desc}" for cmd, desc in group["items"]
            )
            embed.add_field(
                name=group["category"],
                value=command_list,
                inline=False,
            )

        embed.add_field(
            name="\u200b",  # spacer
            value=(
                f"**Versi:** `{BOT_VERSION}`\n"
                f"**Developer:** {BOT_AUTHOR}\n"
                f"**Prefix:** Semua command menggunakan `/` (slash command)"
            ),
            inline=False,
        )

        embed.set_footer(text="CODY Bot • Coworking Space")
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
