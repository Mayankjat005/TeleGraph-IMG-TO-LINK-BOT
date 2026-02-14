import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "23159366"))
    API_HASH = os.getenv("API_HASH", "4623dd30dd1303bddb729eb0862262d9")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # Database
    MONGO_URL = os.getenv("MONGO_URL", "")
    
    # Admin
    ADMIN_STR = os.getenv("ADMINS", "5222155765")
    ADMINS = [int(x) for x in ADMIN_STR.split()] if ADMIN_STR else []
    
    # Channel
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "-1002023786492") # username or ID
    
    # UI
    START_PIC = os.getenv("START_PIC", "https://ibb.co/qYSZKVt1") # Default image
    
    # Log Channel
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", "") # Channel ID (e.g. -100xxxx)

