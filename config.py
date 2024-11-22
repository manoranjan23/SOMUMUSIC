import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21546320"))
API_HASH = getenv("API_HASH", "c16805d6f2393d35e7c49527daa317c7")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8124266415:AAEH0plorlXk-9YinZy9hBUMs-dti-hTf0Y")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Ishuxd:ishusomuxd@ishuxd.78ljc.mongodb.net/?retryWrites=true&w=majority&appName=Ishuxd")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002100433415"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7070591202"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/manoranjan23/SOMUMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/somueditingzone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+mqT4hMn7-4BmYzk1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "false"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from
STRING1 = getenv("STRING_SESSION", "BQFIxVAAIPxdEXVSMpODMCca_Uqhh-8DN0SPpylJt-Iz8AGIJORKPI_Ot5guZp4FvO7Jx8Pn2inVV-JCHYGESGIrtR_fBGYUe5r6oX6-ta4-31-Gh3thEjJ1M0R6jrRAUs6sLmXIX7e6JoKerW7uKCwQkZNobWbjP_Y6Oo_oLusyIsGFPEUIDXWZa5aV4KG-yYtcD3DolUCppFFqkV5hnLtjQiBhsCHIkkJ_vypuBvgyn0jFsDsz4vP8UtE3PxGHKfQOkEuODOw6cLU6YvVTaIA02MoJezw2RBJrPIHXXLyreuACBF5Qpi00ycm2a73kfQ-m_gsSi5Q4qIK10RJ61YEkXj_GCAAAAAHRUWCBAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/ba50dffd30e2629b65c71.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/6eeadeaa8e8c075fd7aa4.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/4dfd906e8406443b5bfde.jpg"
STATS_IMG_URL = "https://telegra.ph/file/6eb615c167fc8218f2247.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/b2f85290f664661e1ba4a.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/fcb8d9e2df742aea6a51f.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/a23eb1ecae45b2d9098af.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b921f8fc21b9d57eb473e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/33eac2fd4f37dc054f399.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/a5ef6f7d45dc7b80e2b76.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/959e57d56c5259ad75d10.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/a34f1e0b17a398f68ecd2.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
