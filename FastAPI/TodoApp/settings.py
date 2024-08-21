#Production Database using  free cloud instane of PostgrsQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHMEY_DATABASE_URL = 'postgresql://TodoApplicationDatabase_owner:0x6kcKrDqItB@ep-cold-grass-a26skx67.eu-central-1.aws.neon.tech/TodoApplicationDatabase?sslmode=require'


engine = create_engine(SQLALCHMEY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 

Base = declarative_base()

