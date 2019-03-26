class TypeHelper:

    @staticmethod
    def is_digit(arg, none=False):
        if (isinstance(arg, int) or isinstance(arg, float)) or (none and arg is None):
            return True
        else:
            raise TypeError
