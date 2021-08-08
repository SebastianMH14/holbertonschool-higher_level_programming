#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py
that prints all City objects from
the database hbtn_0e_14_usa"""

from sqlalchemy.sql.expression import null
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    city_query = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    for states, cities in city_query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
