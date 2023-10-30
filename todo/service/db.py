from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from google.protobuf.json_format import MessageToJson
from sqlalchemy.orm import sessionmaker

# SQLAlchemy database URL
DATABASE_URL = "sqlite:///./sql_app.db"


# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()
