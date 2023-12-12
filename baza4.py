from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)
user1 = User(name="John", age=25)
session.add(user1)
session.commit()

users = session.query(User).all()
for user in users:
    print(user)
    print(user.name, user.age)

user1.age = 45
session.commit()
users = session.query(User).all()
for user in users:
    print(user)
    print(user.id, user.name, user.age)

session.delete(user1)
session.commit()
