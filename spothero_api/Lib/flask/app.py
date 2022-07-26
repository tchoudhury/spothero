from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from spothero_api.Lib.api.ratesApi import RatesApi
from spothero_api.Lib.api.priceApi import PriceApi
from spothero_database.lib.seed_data import seed
import spothero_config.config as app_config


app = Flask(__name__)
api = Api(app)

api.add_resource(RatesApi, "/rates")
api.add_resource(PriceApi, "/price")


swagger_ui_blueprint = get_swaggerui_blueprint(
    app_config.SWAGGER_URL,
    app_config.API_URL,
    config={
        'app_name': "Tahmid-Spothero-rest-api"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=app_config.SWAGGER_URL)

if __name__ == '__main__':
    seed.seed_data()
    app.run(debug=False)
