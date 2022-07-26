from flask_restful import reqparse, fields
from marshmallow import Schema, fields as marsh_fields

DEFAULT_TIMEZONE = "America/Chicago"

rates_resource_fields = {
    'id': fields.Integer,
    'days': fields.String,
    'start_time': fields.String,
    'end_time': fields.String,
    'timezone': fields.String,
    'price': fields.Price
}

rates_put_args = reqparse.RequestParser()
rates_put_args.add_argument("days", type=str, help="comma separated list of days")
rates_put_args.add_argument("times", type=str, help="range of time")
rates_put_args.add_argument("tz", type=str, help="timezone used with date")
rates_put_args.add_argument("price", type=int, help="timezone used with date")

price_resource_fields = {
    'price': fields.Price
}


class PriceQuerySchema(Schema):
    start = marsh_fields.DateTime(required=True)
    end = marsh_fields.DateTime(required=True)
