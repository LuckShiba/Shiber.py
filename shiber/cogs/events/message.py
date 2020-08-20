from discord.ext.commands import Cog
from discord import Message as DiscordMessage, Embed

from ...utils.prefix import get_prefix


class Message(Cog):
    def __init__(self, shiber):
        self.shiber = shiber

    @Cog.listener()
    async def on_message(self, message: DiscordMessage):
        if message.author.bot:
            return
        if len(message.content) in (21, 22) and self.shiber.user in message.mentions:
            await message.channel.send(embed=Embed(
                color=self.shiber.color,
                description=f'**Hello, {message.author.mention}.'
                            f'Use `{get_prefix(message.guild)}help` to see my commands.**'
            ))
        return


def setup(shiber):
    shiber.add_cog(Message(shiber))
