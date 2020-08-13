from discord import Embed
from discord.ext.commands import command, Cog, Context, has_guild_permissions
from shiber.database import Guild

MAX_PREFIX_LENGTH = 10


class Configurations(Cog):
    """My server configurations."""

    def __init__(self, shiber):
        self.shiber = shiber

    @has_guild_permissions(manage_guild=True)
    @command(description='Sets my prefix in a guild.', aliases=['prefix'], usage='[prefix]')
    async def setprefix(self, ctx: Context, prefix):
        embed = Embed(color=self.shiber.color)
        if len(prefix) < MAX_PREFIX_LENGTH:
            Guild(id=ctx.guild.id, prefix=prefix).save()
            embed.title = f'The prefix has been changed to `{prefix}` successfully'
        else:
            embed.title = f"The prefix can't have more than {MAX_PREFIX_LENGTH} characters."

        return await ctx.send(embed=embed)


def setup(shiber):
    shiber.add_cog(Configurations(shiber))
