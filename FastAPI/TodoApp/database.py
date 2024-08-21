# Local Database using Sqlite3 for minimum performance
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHMEY_DATABASE_URL = 'sqlite:///./todosapp.db'


engine = create_engine(SQLALCHMEY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 

Base = declarative_base()

