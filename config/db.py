import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MariaDB Database connection and pool configuration
engine = create_engine(
    os.getenv("DATABASE_URL"),
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=1800,
    pool_timeout=30
)

# Create a session factory
SessionFactory = sessionmaker(bind=engine)

# Create a scoped_session to manage sessions by context/thread
Session = scoped_session(SessionFactory)
