import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the SERPAPI_API_KEY
serpapi_key = os.getenv("SERPAPI_API_KEY")

if serpapi_key:
    print(f"SERPAPI API Key: {serpapi_key}")
else:
    print("SERPAPI_API_KEY not found in .env file") 