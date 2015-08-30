from ..log import reference
# fixme: оделать декораторы логирования

def debug(*args, **kwargs):

    class log(object):
        def __init__(self, fnc):
            self.fnc = fnc

        def __get__(self, instance, owner):
            result = self.fnc(instance, *args, **kwargs)
            instance.logger.info(result)
            return self.fnc(instance)

    return log


class info(object):
    def __init__(self, fnc):
        self.fnc = fnc

    def __get__(self, instance, owner=None):
        func_name = self.fnc.__name__.upper()
        if hasattr(reference, func_name):
            instance.logger.info(getattr(reference, func_name).format(instance))
        return self.fnc
