from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os

# load_dotenv()

# USERNAME = os.getenv("DB_USER")
# PASSWORD = os.getenv("DB_PASSWORD")
# DB = os.getenv("DB_NAME")
# HOST = os.getenv("DB_HOST")

#DATABASE_URL = f"mysql+pymysql://predrag:predrag@192.168.104.11/predrag"
DATABASE_URL="mysql+pymysql://root:@localhost/predrag"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()