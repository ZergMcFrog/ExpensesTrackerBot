#Wrapper which handles the connection to the database backend
from .sqlite import Database
from .exceptions import InstanceAlreadyExistsException, NoInstanceException

#Variable for singleton
databaseInstance = None

def createDatabase(settings):
    global databaseInstance
    if databaseInstance is None:
        databaseInstance = Database(settings)
    else:
        raise InstanceAlreadyExistsException

def getInstance():
    if databaseInstance is None:
        raise NoInstanceException
    return databaseInstance