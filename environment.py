import os

from dotenv import load_dotenv

# Loading data from the .env file
load_dotenv()

# Loading the unique bot token
token = os.environ.get('TOKEN')
