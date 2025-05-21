from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = 'sqlite:///budget.db'
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)