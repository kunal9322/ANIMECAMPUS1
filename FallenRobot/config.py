class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 16743442
    API_HASH = "12bbd720f4097ba7713c5e40a11dfd2a"

    CASH_API_KEY = "PRPSG4AY3Q3H0QG0"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://rjwtydbs:aorANU6vTR3pwL8TIB9wy78UGxT9qJFt@balarama.db.elephantsql.com/rjwtydbs"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001935950378)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/d596a410761b8782f53f7.jpg"

    SUPPORT_CHAT = "Anime_Krew"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5892491831:AAFlCixZHZw-qLHvJuzH2pgluU8t6aZ1VRI"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "S3J6EISOC17L"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6091170475  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [1045939902, 5885920877]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = [5885920877]  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
