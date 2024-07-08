# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz


import sys
import glob
import importlib
from pathlib import Path
from pyrogram import idle
import logging
import logging.config

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz


from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Var, LOG_CHANNEL
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from aiohttp import web
from TonyStark.server import web_server

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz

import asyncio
from pyrogram import idle
from plugins.clone import restart_bots
from TonyStark.bot import StreamBot
from TonyStark.utils.keepalive import ping_server
from TonyStark.bot.clients import initialize_clients

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz


ppath = "plugins/*.py"
files = glob.glob(ppath)
StreamBot.start()
loop = asyncio.get_event_loop()

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz


async def start():
    print('\n')
    print('Initalizing Tony Stark Bot')
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Tech VJ Imported => " + plugin_name)
    if Var.ON_HEROKU:
        asyncio.create_task(ping_server())
    me = await StreamBot.get_me()
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    app = web.AppRunner(await web_server())
    await StreamBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, Var.PORT).start()
    await restart_bots()
    print("Bot Started Powered By @TonyStark_Botz")
    await idle()

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')


# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz
