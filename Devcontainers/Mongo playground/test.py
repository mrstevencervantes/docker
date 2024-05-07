from pymongo import MongoClient
from dotenv import load_dotenv

# Connect to the database
load_dotenv(".env.devcontainer", override=True)
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]
DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]

URI = f"mongodb://{DBUSER}:{DBPASS}@{DBHOST}:27017"
CLIENT = MongoClient(URI)

try:
    print(CLIENT.admin.command("ping"))
    print("Ping successful")
except Exception as e:
    print(e)
