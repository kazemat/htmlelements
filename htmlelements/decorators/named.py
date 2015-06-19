from functools import wraps


def name(value):
    def decorator(fnc):
        @wraps(fnc)
        def named(self):
            self.name = value
        return named
    return decorator