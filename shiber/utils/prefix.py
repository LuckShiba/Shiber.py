from os import environ
from shiber.database import Guild

DEFAULT_PREFIX = environ['DEFAULT_PREFIX']


def get_prefix(shiber, message):
    if message.guild:
        if guild := Guild.objects(id=message.guild.id).first():
            if guild.prefix:
                return guild.prefix
    return DEFAULT_PREFIX
