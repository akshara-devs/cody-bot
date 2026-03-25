# CODY Bot

Discord bot project built with `discord.py`.

## Requirements

- Python 3.11+ recommended
- A Discord bot token
- An API base URL for the backend used by the bot

## Clone The Project

```bash
git clone <your-repository-url>
cd cody-bot
```

## Create A Virtual Environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root:

```env
TOKEN_BOT=your_discord_bot_token
API_BASE_URL=http://localhost:8000
```

Environment variables used by the bot:

- `TOKEN_BOT`: token for your Discord application bot
- `API_BASE_URL`: base URL for the backend API the bot will call

## Run The Bot

```bash
python main.py
```

If the setup is correct, the terminal should show logs that the API client is ready, the cogs are loaded, and the slash commands are synced.

## Available Commands

- `/ping`: check whether the bot is online
- `/help`: show the help message
- `/register`: currently shows a temporary "already registered" onboarding message

## Project Structure

```text
cody-bot/
├── api/        # Shared API client and endpoint wrappers
├── cogs/       # Discord bot features / slash commands
├── utils/      # Embed helpers and shared utilities
├── main.py     # Application entrypoint
└── requirements.txt
```

## Troubleshooting

If the bot exits immediately:

- Make sure `.env` exists in the project root
- Make sure `TOKEN_BOT` is filled in
- Make sure `API_BASE_URL` is filled in

If slash commands do not appear:

- Make sure the bot was invited with the `applications.commands` scope
- Restart the bot and wait for command sync to finish
- Re-invite the bot if the original invite link did not include the correct scopes

If the bot starts but some features fail:

- Make sure the backend API is running
- Make sure `API_BASE_URL` points to the correct backend