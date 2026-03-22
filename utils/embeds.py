import discord


# Warna konsisten untuk semua embed CODY bot
COLOR_SUCCESS = 0x2ECC71  # Hijau
COLOR_ERROR   = 0xE74C3C  # Merah
COLOR_INFO    = 0x3498DB  # Biru


def success_embed(title: str, description: str) -> discord.Embed:
    return discord.Embed(title=f"✅ {title}", description=description, color=COLOR_SUCCESS)


def error_embed(title: str, description: str) -> discord.Embed:
    return discord.Embed(title=f"❌ {title}", description=description, color=COLOR_ERROR)


def info_embed(title: str, description: str) -> discord.Embed:
    return discord.Embed(title=f"ℹ️ {title}", description=description, color=COLOR_INFO)


def onboarding_embed(user: discord.User) -> discord.Embed:
    embed = discord.Embed(
        title="👋 Selamat Datang di CODY Bot!",
        description=(
            f"Halo **{user.display_name}**! CODY adalah coworking space bot yang akan "
            "membantu kamu tetap produktif dan konsisten.\n\n"
            "**Apa yang bisa CODY lakukan?**\n"
            "🗂️ `Project` — Buat dan kelola proyekmu\n"
            "⏱️ `Coworking` — Timer sesi kerja dengan Pomodoro\n"
            "🔥 `Streak` — Jaga konsistensi harianmu\n"
            "🪙 `Currency` — Kumpulkan koin dari sesi kerja\n\n"
            "Kamu sudah terdaftar! Ketik `/help` untuk melihat semua command."
        ),
        color=COLOR_SUCCESS,
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text="CODY Bot • Coworking Space")
    return embed
