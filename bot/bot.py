from os import path
from configparser import ConfigParser
from pyrogram import Client


class bot(Client):
    def __init__(self, name):
        config_file = f"{name}.ini"
        config = ConfigParser()
        config.read(config_file)
        name = name.lower()
        plugins = {'root': path.join(__package__, 'plugins')}
        API_ID = config.get('pyrogram', 'api_id')
        API_HASH = config.get('pyrogram', 'api_hash')
        super().__init__(
            name,
            API_ID=api_id,
            API_HASH=api_hash,
            config_file=config_file,
            workers=16,
            plugins=plugins,
            workdir="./",
        )
    async def start(self):
        await super().start()
        print("bot started. Hi.")
    async def stop(self, *args):
        await super().stop()
        print("bot stopped. Bye.")
