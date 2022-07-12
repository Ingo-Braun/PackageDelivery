from uuid import uuid4
from flask_restful import Api
from flask import Flask
import os
import sys
sys.path.append('./modules')
from modules.commom.loglib import get_logger
from modules.commom.db import db
import modules.commom.mongo_db as mongo_db

logsDir = os.path.join(os.path.dirname(__file__), "logs")
logger = get_logger("HiveMindRESTServer", dir=logsDir, debug=True)
db.init_db()
db.setLogger(logger,"HiveMindRESTServer")
app = Flask(__name__)
app.secret_key = str(uuid4())
api = Api(app)

import modules.rest.packages.package_endpoint as pacakage_endpoint

for i in pacakage_endpoint.paths:
    api.add_resource(pacakage_endpoint.paths[i],i)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=9000)
