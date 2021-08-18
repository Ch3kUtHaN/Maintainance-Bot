import os

class Config(object):

    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")

    # Info
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")

    # Text
    MAINTAINANCE_TEXT = """👋 Hi {} Unkil,\n\nI'm Admin Of <a href="https://t.me/Ch3kUtHaNbotz"><i>Ch3kUtHaNbotz</i></a> \nTell me what You need to know...."""
