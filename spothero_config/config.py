import sys

ROOT_DIR = sys.path[1]

SQLALCHEMY_DATABASE_PATH = "/spothero_alembic"
SQLALCHEMY_DATABASE_URL = f'sqlite:///{ROOT_DIR}{SQLALCHEMY_DATABASE_PATH}/spothero.db?check_same_thread=False'

SWAGGER_URL = '/swagger'
API_URL = f'{ROOT_DIR}/resources/swagger.json'

SEED_DATA_PATH = f"{ROOT_DIR}/resources/data/rates.json"
