from mongoengine import Document, IntField, StringField

__all__ = ['Guild']


class Guild(Document):
    meta = {'collection': 'guilds'}
    id = IntField(db_field='id', primary_key=True)
    prefix = StringField(min_length=1, max_length=10)
