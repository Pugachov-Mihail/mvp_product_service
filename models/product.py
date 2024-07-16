import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cdate = Column(DateTime, default=datetime.datetime.now)
    mdate = Column(DateTime)


class Count(Base):
    __tablename__ = 'count'

    id = Column(ForeignKey('product.id', ondelete='CASCADE'), primary_key=True)
    count = Column(Integer)
    cdate = Column(DateTime, default=datetime.datetime.now)
    mdate = Column(DateTime)


class Cost(Base):
    __tablename__ = 'cost'

    id = Column(ForeignKey('product.id', ondelete='CASCADE'), primary_key=True)
    cost = Column(Float)
    cdate = Column(DateTime, default=datetime.datetime.now)
    mdate = Column(DateTime)
