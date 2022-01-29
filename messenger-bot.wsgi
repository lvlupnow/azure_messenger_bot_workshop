import sys
import os

os.environ['VERIFY_TOKEN'] = "levelupmessengerbottoken"
os.environ['PAGE_ACCESS_TOKEN'] = "EAAjcTjJa6EkBAOdZCTC3L8Em08TkQaCLtHoI6AJj1ta0O86pAnXw3udOaO3dJMyd9gihzYPaZBzzYmxrTgv4fyXQBd2tovPNfgrU1OxJgukus6wQKo7lFbiOqMpKXWZAtz4mOLO3fvBY5PXrSwnLzXaJ5Ab4jn0nfKyn4y2GjpKdjDiyWAh"
sys.path.insert(0, "/var/www/html/messenger-bot")
from messenger_bot import app as application
