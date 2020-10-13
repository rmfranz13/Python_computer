class Pin:
    def __init__(self):
        self.__val = 0

    @property
    def val(self):
        return(self.__val)

    @val.setter
    def val(self, _val):
        self.__val = _val
