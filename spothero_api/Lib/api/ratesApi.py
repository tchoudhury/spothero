from flask import abort
from flask_restful import Resource, marshal_with
from sqlalchemy import exc
from spothero_database.lib import meta, model
from spothero_api.Lib.api.utils import normalize_times, normalize_date
from .constants import rates_resource_fields, rates_put_args
import logging as logger


class RatesApi(Resource):
    @marshal_with(rates_resource_fields)  # serialization
    def get(self):
        result = meta.session.query(model.Rates).all()

        if not result:
            logger.info("No rates were found")
            abort(404, "No rates found")

        return result

    @marshal_with(rates_resource_fields)
    def put(self):
        logger.info("Normalizing payload")
        args = rates_put_args.parse_args()
        days = normalize_date(args['days'])
        times, tz = normalize_times(args['times'], args['tz'])

        results = []

        for day in days:
            result = model.Rates(days=day, start_time=times[0], end_time=times[1], timezone=tz, price=args['price'])

            try:
                logger.info("Attempting to add new record")
                meta.session.add(result)
                meta.session.commit()
                results.append(result)
            except exc.SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                logger.error(error)
                meta.session.rollback()
                abort(409, "Rate cannot be created")

        return results, 201
