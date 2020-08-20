from discord.ext.commands import Cog


class Ready(Cog):
    def __init__(self, shiber):
        self.shiber = shiber

    @Cog.listener()
    async def on_ready(self):
        print('Ready!')


def setup(shiber):
    shiber.add_cog(Ready(shiber))