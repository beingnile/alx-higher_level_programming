#!/usr/bin/python3
"""Changes the name of a State object frm the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def model_state_update_id_2(user, passwd, db):
    """Connects to the mysql server to update the content

    Arguments:
    user (str): A mysql server user
    passwd (str): Password to mysql user
    db (str): The database name
    """
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session.begin() as session:
        old_state = session.query(State).filter(State.id == 2)
        old_state.name = "New Mexico"


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    model_state_update_id_2(user, passwd, db)
