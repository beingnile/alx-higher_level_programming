#!/usr/bin/python3
"""Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def model_state_my_get(user, passwd, db, search):
    """
    Connects to a mysql database to fetch data

    Arguments:
    user (str): The mysql user to connect with
    passwd (str): The password to the mysql database
    db (str): The database name
    search (str): The state to search
    """
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session.query(State).filter(State.name == search).first()

    if (state):
        print(state.id)
    else:
        print("Not found")


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    search = argv[4]

    model_state_my_get(user, passwd, db, search)
