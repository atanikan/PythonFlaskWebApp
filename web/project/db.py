from flask_mongoengine import MongoEngine
from pymongo import errors
from project import app
from project.models import WestDocker, WestDockerModel

class MongoDBConnection():
    """Class representing connection to Mongo database

        :param : keywords arguments

    """
    __db = None


    @classmethod
    def getDB(cls):
        if cls.__db is None:
            cls.__db = cls.__connectToDB()
        return cls.__db

    @classmethod
    def __connectToDB(cls):
        """
        Connects to mongo db based on parameters
        :return: Database object
        """
        app.config['MONGODB_HOST'] = 'mongodb' #change to 'localhost' if running mongodb locally
        app.config['MONGODB_PORT'] = int('27017')
        app.config['MONGODB_USERNAME'] = ''
        app.config['MONGODB_PASSWORD'] = ''
        app.config['MONGODB_DB'] = 'westversions'
        try:
            cls.__db = None
            cls.__db = MongoEngine()
            cls.__db.init_app(app)
        except errors.ConnectionFailure as e:
            print(e)
            raise ConnectionError("Could not connect to server: %s" % e)
        return cls.__db

class DBAcessObjects:
    """
    Class to access database objects
    """
    def __init__(self):
        pass

    def insertIntoDB(self,data):
        west = WestDocker(**data)
        west.save()
        return str(west.id)

    def getAllInstances(self):
        """
        fetches all docker west versions
        :return: list: allWestIds
        """
        allWestVersions = []
        for west in WestDocker.objects():
            westdockmodel = WestDockerModel()
            westdockmodel.id = str(west.id)
            westdockmodel.west_version = west.west_version
            westdockmodel.gcc_version = west.gcc_version
            westdockmodel.gfortan_version = west.gfortan_version
            westdockmodel.blas_version = west.blas_version
            westdockmodel.lapack_version = west.lapack_version
            westdockmodel.mpi_version = west.mpi_version
            westdockmodel.fftw_version = west.fftw_version
            westdockmodel.python_version = west.python_version
            westdockmodel.extraFields = west.extraFields
            allWestVersions.append(westdockmodel.__dict__)
        return allWestVersions

    def getAllIds(self):
        """
        fetches all docker west id's
        :return: list: allWestVersions
        """
        allWestIds = []
        for west in WestDocker.objects():
            allWestIds.append(str(west.id))
        return allWestIds

    def deleteFromDB(self,id):
        """
        Deletes entry from DB
        :param id: Input id
        :return: None
        """
        WestDocker.objects(id=id).delete()
