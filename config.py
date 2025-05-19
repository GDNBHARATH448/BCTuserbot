import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27639080")) #optional
API_HASH = getenv("API_HASH", "5c10faa5b68227793d5f9084106c6f24") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7928209707").split()))
OWNER_ID = int(getenv("OWNER_ID", "7928209707"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "7500951257:AAHBI0QU0AlnM8q413Xx0nIruyqgpRYblaY")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/5badd2112e1e0cdf03a1f.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1002679649519")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GDNBharat/BCT-userbot-")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGlvSgANgNrYILuKeDEVdAJVCRke8RvdVhzF8PUenm-7aGjA5L81SJP-vrcAOha7DAWltexHW0Jwa3U2z5kro32IT7f_ScNwI2gSvvcf_iTZZzd_xOYmDA0-8Td1FO1ctI3w15mMz5_mxRoIpEqkLDR9OhIVsu9EdrP6zsgiuQdo880pSCmmsrcc9Qc2rB8qria6zI9fbZRrG1Lcvg3xf0tsx59BNaJ_kGTnPi-9KfxDnUXujzBpxQiCPQOTc9Dtla3yPMIMvNrVNfNcCUIPFTmI5iZXWavOznQn66tLvO89NFzUCU0GbL_HO3-8GI1GIJrQhNdHSYPoT7vyCCwdUt1l9I0nQAAAAHoAeY6AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
