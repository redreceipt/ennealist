import os

from peewee import (CharField, ForeignKeyField, Model, PostgresDatabase,
                    SmallIntegerField, TextField)

database = PostgresDatabase(os.getenv("DATABASE_URL"))


class BaseModel(Model):
    class Meta:
        database = database


class PersonalityType(BaseModel):
    number = SmallIntegerField(unique=True)
    name = CharField()
    description = TextField()


class User(BaseModel):
    email = CharField(unique=True)
    token = CharField()
    personality_type = ForeignKeyField(PersonalityType, backref='type')


def create_tables():
    with database:
        database.create_tables([User, PersonalityType])
