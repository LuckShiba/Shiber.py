from mongoengine import connect
from os.path import split
from discord.ext import commands
from os import environ, walk, listdir
from shiber.utils.prefix import get_prefix

EMBED_COLOR = 0xf3c478


class Shiber(commands.Bot):
    color = EMBED_COLOR

    def __init__(self):
        super().__init__(get_prefix, None, case_insensitive=True)

    def load_extensions(self, extensions_path):
        for path, subdir, files in walk(extensions_path):
            for file in files:
                if file.endswith('.py'):
                    self.load_extension('.'.join((*filter(None, split(path)), file[:-3])))
        return


if __name__ == '__main__':
    shiber = Shiber()
    connect('shiber', host=environ['MONGO_CONNECTION_STRING'])
    shiber.load_extensions('cogs')
    shiber.run(environ['TOKEN'])
