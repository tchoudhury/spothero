from flask import request, abort
from flask_restful import Resource, marshal_with
from spothero_database.lib import meta, model
from .constants import price_resource_fields, PriceQuerySchema
from spothero_api.Lib.api import utils
import logging as logger

schema = PriceQuerySchema()


class PriceApi(Resource):
    @marshal_with(price_resource_fields)
    def get(self):
        errors = schema.validate(request.args)
        if errors:
            logger.error("Request args did not match schema")
            abort(400, str(errors))

        logger.info("Getting days and times from request args")
        day, start_time, end_time = utils.get_days_and_times_from_date(request.args["start"], request.args["end"])

        if not day:
            logger.error("Dates cannot span more than one day")
            abort(400, str("Unavailable"))

        rates = model.Rates

        result = meta.session.query(rates)\
            .filter(rates.days == day)\
            .filter(rates.start_time <= start_time)\
            .filter(rates.end_time >= end_time).all()

        if not result:
            logger.error("Multiple rates were returned for date range")
            abort(400, str("Unavailable"))

        return result
