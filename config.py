from os import environ

class Config(object):
    API_ID = int(environ.get("API_ID", 21541476))
    API_HASH = environ.get("API_HASH", "a32789925b6d6d4f9c2661a2d98b78af")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5550245504:AAGLNB1XkFfm0dkA54sULMv3Onrbc15VkjE")
    #The bot will work only with following users
    AUTH_USERS = list(int(x) for x in environ.get("AUTH_USERS", "2023056811").split(" "))
    #Owner ID is the user id of your telegram account
    OWNER_ID = int(environ.get("OWNER_ID", "2023056811"))
    #keep default unless you know what you are doing
    DOWNLOAD_DIRECTORY = environ.get("DOWNLOAD_DIRECTORY","./downloads")
   
