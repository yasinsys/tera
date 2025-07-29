import os

class BOT:
    # Make sure this key matches your Render Environment Variables
    TOKEN = os.environ.get("BOT_TOKEN", "")

class API:
    ID = int(os.environ.get("API_ID", 0))
    HASH = os.environ.get("API_HASH", "")

class OWNER:
    ID = int(os.environ.get("ADMIN", 0))  # ADMIN variable in Render

class CHANNEL:
    ID = int(os.environ.get("CHANNEL_ID", 0))  # Optional

class WEB:
    PORT = int(os.environ.get("PORT", 8000))  # Default Flask port

class DATABASE:
    URI = os.environ.get("DB_URI", "")  # MongoDB URI
    NAME = os.environ.get("DB_NAME", "MN_Bot_DB")
