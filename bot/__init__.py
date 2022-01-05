""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)

.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "SessionMakerBot.log")


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)



AKTIFPERINTAH = {}

AVAILABLE_CODE_RECVING_OPTIONS = {
    "app": "Telegram app",
    "sms": "SMS",
    "call": "Phone Call",
    "flash_call": "Phone Flash Call"
}
# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        "Hi. ☺️\n"
        "Thank you for using me 😬\n\n"
        "This is an Open Source Project available on "
        "https://github.com/SUKHPAL443/MAMBA_STRINGSESSION_GENERATOR\n"
        "ℹ️ Subscribe @MAMBA_NETWORK if you 😍 using this bot❗️❣️"
    )
)
INPUT_PHONE_NUMBER = get_config("INPUT_PHONE_NUMBER", (
    "Enter the Phone Number that you want to make awesome."
))
RECVD_PHONE_NUMBER_DBP = get_config("RECVD_PHONE_NUMBER_DBP", (
    "checking received phone number \n\n"
    ">> the Process Takes a Long Time,\n"
    ">>> Please be Patient,\n\n"
    "<b>Never Submit Again</b> \n"
    "<b><i><u>It'll ruin the System</u></i></b>"
))
ALREADY_REGISTERED_PHONE = get_config("ALREADY_REGISTERED_PHONE", (
    "This number is registered on Telegram. "
    "Please input the verification code that you receive "
    "from <a href='tg://user?id=777000'>Telegram</a> "
    "seperated by space, "
    "else a PhoneCodeInvalidError would be raised."
))
CONFIRM_SENT_VIA = get_config("CONFIRM_SENT_VIA", (
    "The confirmation code has been sent via {}"
))
RECVD_PHONE_CODE = get_config("RECVD_PHONE_CODE", (
    "checking received phone code \n\n"
    ">> the Process Takes a Long Time,\n"
    ">>> Please be Patient,\n\n"
    "<b>Never Submit Again</b> \n"
    "<b><i><u>It'll ruin the System</u></i></b>"
))
NOT_REGISTERED_PHONE = get_config("NOT_REGISTERED_PHONE", (
    "This number is not registered on Telegram. "
    "Please check your #karma by reading https://t.me/c/1220993104/28753"
))
PHONE_CODE_IN_VALID_ERR_TEXT = get_config(
    "PHONE_CODE_IN_VALID_ERR_TEXT",
    "Invalid Code Received. Please re /start"
)
TFA_CODE_IN_VALID_ERR_TEXT = get_config(
    "TFA_CODE_IN_VALID_ERR_TEXT",
    "Invalid Two Factor Code Received. Please re /start"
)
ACC_PROK_WITH_TFA = get_config("ACC_PROK_WITH_TFA", (
    "The entered Telegram Number is protected with 2FA. "
    "Please enter your second factor authentication code.\n"
    "<i>This message will only be used for generating your "
    "string session, and will never be used for any other purposes "
    "than for which it is asked.</i>\n\n"
    "It is recommended to use "
    "https://github.com/SUKHPAL443/MAMBA_STRINGSESSION_GENERATOR and not "
    "use this hosted version"
))
SESSION_GENERATED_USING = get_config("SESSION_GENERATED_USING", (
    "Thank you for using me 😬\n\n"
    "This is an Open Source Project available on "
    "https://github.com/SUKHPAL443/MAMBA_STRINGSESSION_GENERATOR\n\n\n"
    "👆👆👆 String Session successfully generated 👆👆👆"
