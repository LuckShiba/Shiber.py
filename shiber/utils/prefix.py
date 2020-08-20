from os import environ
from shiber.database import Guild

DEFAULT_PREFIX = environ['DEFAULT_PREFIX']


def get_prefix(guild):
    if guild:
        if guild_db := Guild.objects(id=guild.id).first():
            if p := guild_db.prefix:
                return p
    return DEFAULT_PREFIX


def prefix_callable(shiber, message):
    return get_prefix(message.guild)
