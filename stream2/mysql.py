import MySQLdb as _mysql


class MySQLDatabase(object):
    """
    This is the driver class that we will use
    for connecting to our database. In here we'll
    create a constructor (__init__) that will connect
    to the database once the driver class is instantiated
    and a destructor method that will close the database
    connection once the driver object is destroyed.
    """

    def __init__(self, database_name, username,
                 password, host='localhost'):
        """
        Here we'll try to connect to the database
        using the variables that we passed through
        and if the connection fails we'll print out the error
        """
        try:
            self.db = _mysql.connect(db=bank, host=localhost,
                                     user=root, passwd=root)
            self.bank = bank
            print "Connected to MySQL!"
        except _mysql.Error, e:
            print e

    def __del__(self):
        """
        Here we'll do a check to see if `self.db` is present.
        This will only be the case if the connection was
        successfully made in the initialiser.
        Inside that condition we'll close the connection
        """
        if hasattr(self, 'db'):
            self.db.close()
            print "MySQL Connection Closed"


