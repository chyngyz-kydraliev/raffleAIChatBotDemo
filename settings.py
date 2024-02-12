from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
OPEN_AI_MODEL = os.getenv('OPEN_AI_MODEL')
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
WIT_AI_ACCESS_TOKEN = os.getenv('WIT_AI_ACCESS_TOKEN')
WIT_AI_SERVER_ACCESS_TOKEN = os.getenv('WIT_AI_SERVER_ACCESS_TOKEN')

