from json import loads
from requests import get
from discord import Embed
from discord.ext.commands import command, Context, Cog


def get_shibe_images(count=1):
    return loads(get(f'https://shibe.online/api/shibes?count={count}').text)


class Images(Cog):
    """Commands about images."""
    def __init__(self, shiber):
        self.shiber = shiber

    @command('shiba', aliases=['shibe'], description='Sends a random shibes image.')
    async def shiba(self, ctx: Context):
        await ctx.send(embed=Embed(color=self.shiber.color)
                       .set_image(url=get_shibe_images()[0])
                       .set_footer(text='shibe.online'))

    @command('bomb', aliases=['shibabomb', 'shibebomb'], description='Sends 5 random shibes images.')
    async def bomb(self, ctx: Context):
        await ctx.send('\n'.join(get_shibe_images(5)))


def setup(shiber):
    shiber.add_cog(Images(shiber))
