from functools import wraps

# TODO: fix this decorator
def name(value):
    class named(object):

        def __init__(self, fnc):
            self.fnc = fnc

        def __get__(self, instance, owner):
            print(dir(self.fnc))
            print(self.fnc.fnc)
            setattr(self.fnc, 'name', value)
            return self.fnc
    return named