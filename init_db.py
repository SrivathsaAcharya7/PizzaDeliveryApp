from database import Base, engine, mapper_registry
from models import Order, User

mapper_registry.configure()
Base.metadata.create_all(bind=engine)
