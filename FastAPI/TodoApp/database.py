# Local Database using Sqlite3 for minimum performance
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

SQLALCHMEY_DATABASE_URL = 'sqlite:///./todosapp.db'


engine = create_engine(os.getenv('POSTRGRES_URL'),connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 

Base = declarative_base()

