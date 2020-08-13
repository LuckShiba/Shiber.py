from discord import Embed
from discord.ext.commands import Cog, Context, CommandError, CommandNotFound, MissingPermissions, NoPrivateMessage, \
    ArgumentParsingError, BadArgument, MissingRequiredArgument
from shiber.utils.help import help_embed


class Events(Cog):
    def __init__(self, shiber):
        self.shiber = shiber

    @Cog.listener()
    async def on_ready(self):
        print('Ready!')

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        if isinstance(error, CommandNotFound):
            return

        embed = Embed(color=self.shiber.color)
        embed.set_footer(text=f'For more information use {ctx.prefix}help {ctx.command}.')

        if isinstance(error, MissingPermissions):
            embed.title = f'You need the `{error.missing_perms[0]}` permission to use this command.'
        elif isinstance(error, NoPrivateMessage):
            embed.title = 'This command only can be used in a server.'
        elif isinstance(error, (MissingRequiredArgument, BadArgument, ArgumentParsingError)):
            embed = help_embed(ctx.prefix, ctx.command, embed)
            embed.description = embed.title
            embed.title = 'You used this command incorrectly.'
        else:
            raise error

        return await ctx.send(embed=embed)


def setup(shiber):
    shiber.add_cog(Events(shiber))
