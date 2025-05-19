from sqlalchemy import create_engine

from app.orm.models._base import Base

engine = create_engine(url="sqlite:///db/data.db", echo=True)

Base.metadata.create_all(engine)
