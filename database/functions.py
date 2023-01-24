
from database.models import UsersDatabase
from database.database import SessionLocal

session = SessionLocal()

def add_data(name, reps):
    data = UsersDatabase(name=name,reps=reps)
    session.add(data)
    session.commit()