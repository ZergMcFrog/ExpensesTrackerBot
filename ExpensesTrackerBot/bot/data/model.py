#Module containing all the model classes

class User():

    def __init__(self, name, admin=False):
        self.name = name
        self.admin = admin


class Good():

    def __init__(self, name):
        self.__name = name