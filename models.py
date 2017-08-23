from peewee import *
import datetime

db = SqliteDatabase("new.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    email = CharField(unique=True)
    name = CharField(max_length=35)
    password = CharField(max_length=35)
    tag = CharField(max_length=50, default="Hi, Aroxbit is awesome !", null = True)
    time_stamp = DateTimeField(default=datetime.datetime.now)








def initialize():
    db.connect()
    db.create_tables([User], safe=True)
