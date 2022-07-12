from flask import session
from flask.helpers import make_response
from flask import request
from modules.commom.db import db

logger = db.getLogger("HiveMindRESTServer")

def auth_endpoint(f, level="device", *args, **kwargs):
    def d(*args, **kwargs):
        # if 'auth' not in session and "Token" not in dict(request.headers):
        #     print(dict(request.headers))
        #     print('no auth')
        #     return make_response("fail", 403)
        # else:
        logger.info("[auth_endpoint_decorator]")
        return f(*args, **kwargs)
    return d
