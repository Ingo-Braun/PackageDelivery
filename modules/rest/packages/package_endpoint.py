from flask_restful import reqparse, abort, Resource
from flask.helpers import make_response
from flask import jsonify, request, send_from_directory, redirect, session
import modules.commom.mongo_db as mongo_db
from modules.commom.db import db
from modules.rest.commom.decorators import auth_endpoint
import os
from modules.rest.templates import packages_builder
import requests

logger = db.getLogger("HiveMindRESTServer")
packages_dir = os.path.join(os.getcwd(),"packages")



class package_index(Resource):
    @auth_endpoint
    def get(self):
        logger.info("[package_index] [GET]")
        return make_response(self.build_packages_index_page(), 200)

    @auth_endpoint
    def post(self):
        data = dict(request.form)
        if "version" in data and "device_id" in data:
            pass

    @staticmethod
    def build_packages_index_page():
        packages = mongo_db.get_packages()
        html = packages_builder.build_index(packages)
        return make_response(html, 200)


class package_page(Resource):

    @auth_endpoint
    def get(self,name):
        logger.info(f"[package_page] [GET] {name}")
        return make_response(self.build_package_page(name), 200)

    @staticmethod
    def build_package_page(package_name):
        package = list(mongo_db.find_package_by_name(package_name))
        if len(package) == 0:
            return package_page.get_from_public_repo(package_name,request)

        html = packages_builder.build_package_page(package[0])
        return make_response(html, 200)
    
    @staticmethod
    def get_from_public_repo(name,request):
        logger.info(f"{name}")
        repo_url = "https://pypi.org/simple/{}/"
        resp = requests.get(repo_url.format(name))
        logger.info(f"{repo_url.format(name)} {resp.status_code}")
        respo = make_response(resp.content,resp.status_code)
        return respo

class package_file(Resource):

    @auth_endpoint
    def get(self,name,file):
        logger.info(f"[package_file] [GET] {name} {file}")
        
        file_path = os.path.join(*[packages_dir,name,file])
        if os.path.exists(file_path):
            return send_from_directory(os.path.dirname(file_path),file,as_attachment=False)
        return make_response("not found",404)

paths = {
    "/package/": package_index,
    "/package/<string:name>/": package_page,
    "/package/<string:name>/<string:file>": package_file
    }
