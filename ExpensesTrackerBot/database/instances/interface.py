#Abstract class for database object. Default behaviour can be overwritten in the concrete implementation

class AbstractDatabase():

    def addUser(self, name, admin=False):
        raise NotImplementedError

    def deleteUser(self, name):
        raise NotImplementedError

    def chageUser(self, name, admin=False):
        raise NotImplementedError