from sqlalchemy import (
    Column,
    Time,
    Integer,
    Numeric,
    Text,
    UniqueConstraint
)
from .meta import base


class Rates(base):
    __tablename__ = 'Rates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    days = Column(Text)
    start_time = Column(Time)
    end_time = Column(Time)
    timezone = Column(Text)
    price = Column(Numeric(10, 2))

    __table_args__ = (UniqueConstraint('days', 'start_time', 'end_time', name='Rates_constraint'),)
