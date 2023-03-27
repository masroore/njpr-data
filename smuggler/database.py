from sqlmodel import SQLModel, create_engine, Session

db_filename = "njpr.db"
sqlite_url = f"sqlite:///{db_filename}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
