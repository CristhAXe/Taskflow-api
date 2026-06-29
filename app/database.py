from sqlalchemy import   create_engine
from sqlalchemy.orm import  sessionmaker, DeclarativeBase
from app.config import settings

# creacion del motor conectadoa  nuestra url de .env
engine= create_engine(settings.database_url)

SessionLLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

def get_db():
    db= SessionLLocal()
    try:
        yield db
    finally:
        db.close()


