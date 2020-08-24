from discord import Embed
from discord.ext.commands import command, Context, Cog
from shiber.utils.help import help_embed


class Info(Cog):
    """Information about me."""
    def __init__(self, shiber):
        self.shiber = shiber

    @command(description='Show my commands and information about them.', usage='[command name]')
    async def help(self, ctx: Context, *, command_name=''):
        embed = Embed(color=self.shiber.color)
        if cmd := self.shiber.get_command(command_name):
            embed = help_embed(ctx.prefix, cmd, embed)
        else:
            for cog in self.shiber.cogs.values():
                if commands := [c.name for c in cog.get_commands() if not c.hidden]:
                    embed.title = f'Use `{ctx.prefix}help [command name]` to view more information about a' \
                                        ' command.'
                    embed.add_field(name=f'{cog.qualified_name}: `{cog.description}`',
                                    value=f'`{"`, `".join(commands)}`', inline=False)

        return await ctx.send(embed=embed)
    

def setup(shiber):
    shiber.add_cog(Info(shiber))
