
from modules.commom.container import container
import json


class db():
    def __init__(self) -> None:
        pass

    @staticmethod
    def register_device(dv):
        container.get_arg('devices')[dv.device_id] = dv

    @staticmethod
    def get_device(device_id):
        if device_id in container.get_arg('devices'):
            return container.get_arg('devices')[id]
        else:
            return None

    @staticmethod
    def init_db():
        with open('E:\\Desktop\\HiveMind\\server\\tokens.json', 'r') as f:
            container.set_arg("tokens", json.loads(f.read()))
        container.set_arg("devices", {})
        container.set_arg("bundle",{})
        container.set_arg("logger",{})

    @staticmethod
    def auth(token, type):
        types = {
            "device": "devices_tokens",
            "admin": "admin_tokens"
        }
        # print(container.get_arg())
        return token in container.get_arg("tokens")[types.get(type, "devices_tokens")]

    @staticmethod
    def get_devices():
        return container.get_arg("devices")

    @staticmethod
    def setLogger(logger,name):
        if container.has_arg("logger"):
            container.get_arg("logger")[name] = logger
        else:
            container.set_arg("logger",{name,logger})
    
    @staticmethod
    def getLogger(name):
        if name in container.get_arg("logger"):
            return container.get_arg("logger")[name]

    @staticmethod
    def get_bundle(id):
        return container.get_arg("bundle")[id]
    
    @staticmethod
    def set_bundle(data):
        container.get_arg("bundle")[data["bundle_id"]] = data