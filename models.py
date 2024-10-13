from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'  # Name of the table
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    degree = Column(String(100), nullable=True)
    specialization = Column(String(100), nullable=True)
    certificates = Column(String(200), nullable=True)
    languages = Column(String(200), nullable=True)

# Create an SQLite database
engine = create_engine('sqlite:///users.db')

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample user data


# Query the database and display the data
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Degree: {user.degree}, "
          f"Specialization: {user.specialization}, Certificates: {user.certificates}, "
          f"Languages: {user.languages}")

# Close the session
session.close()
