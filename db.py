import os
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('URL_DB'), echo=True)
# engine = create_engine('postgresql+psycopg2://san4es:san4es777888@localhost/kafka', echo=True)

Base = declarative_base(metadata=MetaData())


class DataFromKafka(Base):
    __tablename__ = 'data'
    __table_args__ = {"schema": "public"}

    id = Column(Integer, autoincrement=True, primary_key=True)
    data = Column(String(255), nullable=True)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
