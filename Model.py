from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
conn = "sqlite:///projeto2.db"

engine = create_engine(conn, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class Pessoa(Base):
	__tablename__ = "Pessoa"
	id = Column(Integer, primary_key=True)
	nome = Column(String(50))
	email = Column(String(200))
	senha = Column(String(100))
Base.metadata.create_all(engine)