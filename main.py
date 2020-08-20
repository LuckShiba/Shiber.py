from mongoengine import connect
from discord.ext.commands import Bot
from os import environ, walk
from shiber.utils.prefix import prefix_callable
from pathlib import PurePath

EMBED_COLOR = 0xf3c478


class Shiber(Bot):
    color = EMBED_COLOR

    def __init__(self):
        super().__init__(prefix_callable, None, case_insensitive=True)

    def load_extensions(self, extensions_path):
        for path, subdir, files in walk(extensions_path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    ext = '.'.join((*filter(None, PurePath(path).parts), file[:-3]))
                    try:
                        self.load_extension(ext)
                        print(f'Loaded extension {ext}.')
                    except Exception as exception:
                        print(f'Failed to load {ext}: {exception}')
        return


if __name__ == '__main__':
    shiber = Shiber()
    connect('shiber', host=environ['MONGO_CONNECTION_STRING'])
    shiber.load_extensions('shiber/cogs')
    shiber.run(environ['TOKEN'])