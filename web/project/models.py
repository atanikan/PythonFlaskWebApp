from mongoengine import (
    Document, ListField, StringField, QuerySet)


"""
    
"""

class FilterQuerySet(QuerySet):
    """ Class to filter query on mongo database
    """

    def get_unique_values(self, field):
        """ fetches list of unique values
        :param field: field to filter on in database
        :return: list of field values
        """
        unique_values = {str(v).lower(): v for v in self.distinct(field=field)}.values()
        return unique_values


class WestDocker(Document):
    """
    Class defining Database attribute models
    """
    west_version = StringField()
    gcc_version = StringField()
    gfortan_version = StringField()
    blas_version = StringField()
    lapack_version = StringField()
    mpi_version = StringField()
    fftw_version = StringField()
    python_version = StringField()
    extraFields = ListField()
    meta = {'strict': False,
            'queryset_class': FilterQuerySet}


class WestDockerModel():
    """
    Class with model constants
    """
    id = ""
    west_version = ""
    gcc_version = ""
    gfortan_version = ""
    blas_version = ""
    lapack_version = ""
    mpi_version = ""
    fftw_version = ""
    python_version = ""
    extraFields = ""