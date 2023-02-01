from os import getenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

engine = create_engine(getenv('DATABASE'), echo=True)
session = sessionmaker(bind=engine)
Base = declarative_base()

class Members(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    username = Column(String)
    name = Column(String)
    graduate_year = Column(Integer)

    def __init__(self, name, user_id, username, graduate_year):
        self.name = name
        self.user_id = user_id
        self.username = username
        self.graduate_year = graduate_year


Base.metadata.create_all(bind=engine)

session = session()
session.close()