#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def model_state_fetch_all(user, passwd, db):
    """Connects to a MySQL database to list state objects

    Arguments:
    user (str): The MySQL user to connect to
    passwd (str): The password of the user
    db (str): The database name
    """
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    model_state_fetch_all(user, passwd, db)
