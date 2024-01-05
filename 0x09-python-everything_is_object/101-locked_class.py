class LockedClass:
    """Locked class: can't set instance attributes except 'first_name'
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
