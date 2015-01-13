from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class entries(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText)
    created = Column(DateTime, default=None)
    edited = Column(DateTime, default=None)

    def createdtime(created=None):
        if created is None:
	    created = datetime.datetime.now()
    def editedtime(edited=None):
        if edited is None:
	    edited = datetime.datetime.now()



    @classmethod
    def all(rows):
        q1 = session.query(rows).all()
        return q1

    @classmethod
    def by_id(rows,id_number):
        q2 = session.query(rows).filter_by(id=id_number)
        return q2

