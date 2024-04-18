#!/usr/bin/python3
"""Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def model_state_filter_a(user, passwd, db):
    """Connects to a database to fetch data

    Arguments:
    user (str): The username for the mysql server
    passwd (str): The password to the mysql user
    db (str): The database name
    """
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        states = session.query(State).filter(State.name.like("%a%")).all()

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    model_state_filter_a(user, passwd, db)
