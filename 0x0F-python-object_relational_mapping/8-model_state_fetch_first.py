#!/usr/bin/python3
"""script that prints the first
State object from the database
hbtn_0e_6_usa"""

from sqlalchemy.sql.expression import null
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True)
    
    Session = sessionmaker(engine)
    session = Session()

    first_query = session.query(State).first()

    if first_query is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_query.id, first_query.name))

    session.close()
