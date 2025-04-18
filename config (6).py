import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28362850")) #optional
API_HASH = getenv("API_HASH", "34f9cb93364db16fc45d003e4c81d97a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7588442909").split()))
OWNER_ID = int(getenv("OWNER_ID", "7635867946"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7660309192:AAHsDRuxVOj1p-55QKPm8bnU6qQ515u0loI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://files.catbox.moe/w04ren.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "1002141779241")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GDNBharat/Toxic-userbot")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGwyGIAuC74P0mFemk1MfPQgizI_snLzYQ1Zsgfs-lbAbGTdo136-Kc9Lcc9rpqdVHQBayg5oiIVUvRDMwNZPsG5zd9aX4MmaEotHpIBZEPgkZii9Q8o0Xx1Vr4rlVPVWwpjNhl8WkH4VfgfHObp6tiTUzTE8mWCmnt3QUpAyMme2vHF2rF_iXWD2GS00Pw6b5j-ywOuRnunlN2LmZO22brvHUY2ciXyeUy2JV3i-QADxHARnDOMf5T9oDbfLU2zRggrCQEXsJ8iTruNT5riD-ogPYcAUB9UZsLmiP1Y40HbJwYKDktG5bmwmQ6RuSjz9tOnm6fZ9W6gQKapjoaXoWP_ngU3QAAAAHETnMdAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
