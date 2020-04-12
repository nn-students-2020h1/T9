import warnings


class PseudoClass:
    def __init__(self):
        self.data_list = []
        self.data_str = ''
        self.child_class = None

    def add(self, a):
        if type(a) == dict:
            raise TypeError("Doesn't support dict")
        self.data_list.append(a)

    def edit_str(self, new_str):
        self.data_str = new_str
        warnings.warn("deprecated, use the field directly", DeprecationWarning)
