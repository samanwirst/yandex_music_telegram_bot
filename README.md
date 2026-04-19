# Yandex Music Telegram Bot

A Telegram bot for searching and downloading tracks from Yandex Music using the unofficial Python client:

- PyPI package: `yandex-music`
- https://pypi.org/project/yandex-music/

## What the Bot Does

- Accepts a text query from a user (track name, optionally with artist).
- Searches Yandex Music and takes the **best match**.
- Downloads the audio file from the direct link.
- Sends the track back to Telegram as an audio message with title and performer.

## Commands and Usage

- `/start` - sends a short help message.
- Any other text - treated as a music search query.

Example:

```text
Blinding Lights The Weeknd
```

If the search is successful, the bot replies with found track info and then sends audio.

## Project Structure

- `main.py` - bot handlers, search flow, and sending audio
- `ya_music.py` - wrapper around Yandex Music search logic
- `config.py` - environment variable config
- `Dockerfile`, `docker-compose.yml` - containerized run

## Requirements

- Python 3.11+
- Telegram Bot Token
- Yandex Music user token

Dependencies (`requirements.txt`):

- `aiogram==2.25`
- `yandex_music`

## Environment Variables

Create a `.env` file in the project root:

```dotenv
BOT_TOKEN=your_telegram_bot_token
YANDEX_USER_TOKEN=your_yandex_music_user_token
```

## Local Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Docker Run

```bash
docker compose up --build -d
```

`docker-compose.yml` loads variables from `.env`:

```yaml
services:
  bot:
    build: .
    env_file:
      - .env
    restart: always
```

## Notes

- The project relies on an unofficial Yandex Music API client.
- Search currently returns one best result and sends that track.
- If no suitable track is found, the bot returns an error message.
