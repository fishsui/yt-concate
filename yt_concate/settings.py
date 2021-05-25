import os  # os為作業系統的意思
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
