from SomuX.core.bot import Somu
from SomuX.core.dir import dirr
from SomuX.core.git import git
from SomuX.core.userbot import Userbot
from SomuX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Somu()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
