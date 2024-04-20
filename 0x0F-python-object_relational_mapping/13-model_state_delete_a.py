#!/usr/bin/python3
"""Deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def model_state_delete_a(user, passwd, db):
    """Connects to mysql server to delete records

    Argument:
    user (str): A mysql user
    passwd (str): Password for the mysql user
    db (str): The database name
    """
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session.begin() as session:
        to_delete = session.query(State).filter(State.name.like("%a%"))
        for state in to_delete:
            session.delete(state)


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    model_state_delete_a(user, passwd, db)
