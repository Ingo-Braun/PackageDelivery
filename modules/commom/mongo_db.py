import pymongo
import json
import os

CONFIG = {}
with open(os.path.join(os.getcwd(),'config.json'),'r') as f:
    CONFIG = json.loads(f.read())


class conn():
    def __init__(self):
        self.conn = pymongo.MongoClient(CONFIG['mongo'])
    def __enter__(self,*args,**kwars):
        return self.conn['hivemind']
    def __exit__(self,*args,**kwargs):
        self.conn.close()


def set_package(data):
    with conn() as db:
        query = {"package_id":data["package_id"]}
        if len([i for i in db['packages'].find(query)]) == 0:
            db['packages'].insert_one(data)

def get_package(package_id):
    # return data
    with conn() as db:
        data = {"package_id":package_id}
        return db['packages'].find(data)

def find_package_by_name(name):
    # return [i for i in data if i["name"] == name]
    with conn() as db:
        data = {"name":name}
        return [i for i in db["packages"].find(data)]

def get_packages():
    # return data
    with conn() as db:
        query = {"active":True}
        return iter(db['packages'].find(query))
