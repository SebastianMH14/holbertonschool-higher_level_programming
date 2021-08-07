#!/usr/bin/python3
"""script that prints the State
object with the name passed as
argument from the database hbtn_0e_6_usa"""

from sqlalchemy.sql.expression import null
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    namesh = argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    name_argv = session.query(State).filter(
        State.name.like(namesh)).order_by(State.id).first()

    if name_argv is not None:
        print(name_argv.id)
    else:
        print("Not found")
    session.close()
