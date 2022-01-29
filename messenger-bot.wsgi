import os
import sys

os.environ['VERIFY_TOKEN'] = "INSERT_TOKEN"
os.environ['PAGE_ACCESS_TOKEN'] = "INSERT_TOKEN"
sys.path.insert(0, "/var/www/html/messenger-bot")
from messenger_bot import app as application
