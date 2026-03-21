import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
CSV_FILE_PATH = os.getenv("CSV_FILE_PATH")
MAX_EMAILS = os.getenv("MAX_EMAILS")

if not all([SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, CSV_FILE_PATH, MAX_EMAILS]):
    raise RuntimeError("Make sure to add the secrets in .env")