from peewee import Model
from . import settings


class BaseModel(Model):
    class Meta:
        database = settings.DATABASES['default']
