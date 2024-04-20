#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def model_state_insert(user, passwd, db):
    """Connects to a mysql database to add a new object

    Arguments:
    user (str): The mysql user to connect to
    passwd (str): The password to the mysql user
    db (str): The database name
    """
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session.begin() as session:
        louisiana = State(name="Louisiana")
        session.add(louisiana)


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    model_state_insert(user, passwd, db)
