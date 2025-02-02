from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://fastapi_test_db_user:s67q79Z1voUKxsxb7kxvww5ly0ySqnnb@dpg-cufidvdds78s73fljgj0-a.oregon-postgres.render.com/fastapi_test_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():  # This is for getting the Database
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
