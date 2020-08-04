class InstanceAlreadyExistsException(Exception):
    '''Raised when the database instance should be created but already is'''

    def __init__(self):
        self.message = "There is already an instance of the database"
        super().__init__(self.message)

class NoInstanceException(Exception):
    '''Raised when trying to call a non existant database instance'''

    def __init__(self):
        self.message = "No instance for a database found"
        super().__init__(self.message)