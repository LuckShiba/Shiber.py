from inspect import Parameter

from discord import Embed
from discord.ext.commands import Command


def help_embed(prefix: str, command: Command, embed: Embed) -> Embed:
    embed.title = f'`{command.name}`: {command.description}\n\n'
    uses = ''
    params = command.clean_params.values()
    cmd_call = f'{prefix}{command.name}'
    if not params or any(filter(lambda x: x.default is not Parameter.empty, params)):
        uses += f'`{cmd_call}`\n'
    if command.usage:
        uses += f'`{cmd_call} {command.usage}`\n'
    if uses:
        embed.add_field(name='Uses:', value=uses)
    if command.aliases:
        embed.add_field(name='Aliases:', value=f'`{"`, `".join(command.aliases)}`')
    return embed
