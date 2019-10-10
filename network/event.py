from functools import wraps


class Event(object):

    instance = None
    callbacks = dict()

    def _new_(cls, **kwargs):
        if cls.callbacks.get(kwargs.get("name")) is None:
            cls.callbacks[kwargs["name"]] = set()
            if kwargs.get("callbacks"):
                cls.callbacks[kwargs["name"]].add(kwargs["callbacks"])
            if cls.instance is None:
                cls.instance = object._new_(cls)
            return cls.instance

    @classmethod
    def occurence(cls, name, *args, **kwargs):
        try:
            for callback in cls.callbacks[name]:
                callback(*args, **kwargs)
        except KeyError:
            pass

    @classmethod
    def origin(cls, name, post=False):

        def _wrapper(func):
            @wraps(func)
            def _executer(self, *args, **kwargs):
                if post:
                    result = func(self, *args, **kwargs)
                    cls.occurence(name, *args, **kwargs)
                    return result
                else:
                    cls.occurence(name, *args, **kwargs)
                    return func(self, *args, **kwargs)

            return _executer
        return _wrapper

    def register(self, name, callback):
        if self.callbacks.get(name) is None:
            self.callbacks[name] = set()
        self.callbacks[name].add(callback)



