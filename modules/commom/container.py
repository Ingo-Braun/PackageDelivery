

class container():
    _args = {}

    @staticmethod
    def set_arg(key,data):
        container._args[key] = data
        # print(container._args)

    @staticmethod
    def get_arg(key):
        # print(container._args)
        return container._args[key]
    
    @staticmethod
    def has_arg(name):
        # print(container._args)
        return name in container._args

    def __init__(self) -> None:
        raise Exception('static class')
    
    
