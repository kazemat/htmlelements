from functools import wraps

# TODO: fix this decorator
def name(value):
    def named(self):
        setattr(self, 'name', value)
        # self.name = value
        return self
    return named