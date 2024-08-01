from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, registry

mapper_registry = registry()
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:root@localhost:3306/pizzadelivery", echo=True)
Session = sessionmaker()
