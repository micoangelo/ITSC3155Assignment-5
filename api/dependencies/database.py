from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import conf
from urllib.parse import quote_plus

# Format the URL for MySQL connection
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{conf.user}:{quote_plus(conf.password)}@{conf.host}:{conf.port}/{conf.database}?charset=utf8mb4"
)

# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# SessionLocal will create new sessions that we can use to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models to inherit from
Base = declarative_base()

# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
