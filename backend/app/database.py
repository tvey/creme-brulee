from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

DATABASE_URL = settings.DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(bind=engine, expire_on_commit=False)
