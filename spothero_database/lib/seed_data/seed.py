import json

from spothero_config.config import SEED_DATA_PATH
from spothero_database.lib.meta import session
from spothero_database.lib.model import Rates
from spothero_api.Lib.api import utils
from sqlalchemy import exc
import logging as logger


def seed_data():
    file = open(SEED_DATA_PATH)
    data = json.load(file)

    for rate in data['rates']:

        logger.info("normalizing seed data")
        days = utils.normalize_date(rate['days'])
        times, tz = utils.normalize_times(rate['times'], rate['tz'])

        for day in days:
            rates = Rates(
                days=day,
                start_time=times[0],
                end_time=times[1],
                timezone=tz,
                price=rate["price"]
            )

            try:
                # Should be changed to bulk_save_objects for optimization but there was a bug I did not fix.
                logger.info("Attempting to add record")
                session.add(rates)
                session.commit()
            except exc.SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                logger.error(error)
                session.rollback()
