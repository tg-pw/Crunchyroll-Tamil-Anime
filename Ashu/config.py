from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "29917436"))
    API_HASH = str(env.get("API_HASH", "4a926822b076a086a167fe8f2701d3e9"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "7444756177:AAGsT75UInjo5gZNatUEDw4IZDUqubJ0nEI"))
    OWNER_ID = int(env.get('OWNER_ID', '7062828064'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', "mongodb+srv://botzashu:LjkXI1JoztDQiQlr@cluster0.38ague0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "BotzPW"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'Ashu'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', "-1002036620217")
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', "True")
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://raw.githubusercontent.com/AshutoshGoswami24/Me/refs/heads/main/img/img%20to%20joine.png")
    START_PIC = env.get('START_PIC', "https://raw.githubusercontent.com/AshutoshGoswami24/Me/refs/heads/main/img/img%20to%20joine.png")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://raw.githubusercontent.com/AshutoshGoswami24/Me/refs/heads/main/img/welcome.png")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002186333363"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002186333363"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))


class Server:
    PORT = int(env.get("PORT", 80))
    API_URL = str(env.get("API_URL", ""))
    API_VERSONI = str(env.get("API_VERSONI", "1.1"))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    # HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    # NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", "0.0.0.0"))
    URL = "https://stream.movies4uu.workers.dev/".format( #http://{}{}/
    # "s" if HAS_SSL else "",
    FQDN,
    # "" if NO_PORT else 
    ":" + str(PORT)
    )


  
