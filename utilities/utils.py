class TypeHelper:

    @staticmethod
    def is_digit(arg, none=False):
        if isinstance(arg, int) or isinstance(arg, float):
            return True
        if none and arg is None:
            return False
        raise TypeError
