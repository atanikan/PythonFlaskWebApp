#Defines views in html
from wtforms import ( Form, SelectField, StringField, validators, PasswordField, FieldList,FormField)

class PassCodeForm(Form):
    """
    Form for entering passcode
    """
    passcode = PasswordField('Passcode',description='Enter passcode to change mongo database details')

class ExtraForm(Form):
    """
    Form providing extra/user defined attributes
    """
    extrakey = StringField(description='Enter custom label',render_kw={"placeholder": "Enter Field Label"})
    extravalue = StringField(description='Enter custom value', render_kw={"placeholder": "Enter Field Value"})


class WestForm(Form):
    """
    Form with select fields
    """
    westversion = SelectField('West version', description='Select West version')
    gccversion = SelectField('gcc version', description='Select gcc version')
    gfortanversion = SelectField('gfortan version', description='Select gfortan version')
    mpiversion = SelectField('MPI version', description='Select MPI version')
    fftwversion = SelectField('FFTW version', description='Select FFTW version')
    blasversion = SelectField('blas version', description='Select blas version')
    lapackversion = SelectField('lapack version', description='Select lapack version')
    pythonversion = SelectField('Python version', description='Select Python version')

class WestCreateForm(Form):
    """
    Form for inserting: insert.html
    """
    west_version = StringField('West version', [validators.DataRequired()],description='Enter West version', render_kw={"placeholder": "Enter West version"})
    gcc_version = StringField('gcc version', [validators.DataRequired()],description='Enter gcc version', render_kw={"placeholder": "Enter gcc version"})
    gfortan_version = StringField('gfortan version', [validators.DataRequired()],description='Enter gfortan version', render_kw={"placeholder": "Enter gfortan version"})
    blas_version = StringField('blas version', [validators.DataRequired()],description='Enter blas version', render_kw={"placeholder": "Enter blas version"})
    lapack_version = StringField('lapack version', [validators.DataRequired()],description='Enter lapack version', render_kw={"placeholder": "Enter lapack version"})
    mpi_version = StringField('MPI version', [validators.DataRequired()],description='Enter MPI version', render_kw={"placeholder": "Enter MPI version"})
    fftw_version = StringField('FFTW version', [validators.DataRequired()],description='Enter FFTW version', render_kw={"placeholder": "Enter FFTW version"})
    python_version = StringField('Python version', [validators.DataRequired()],description='Enter Python version', render_kw={"placeholder": "Enter Python version"})
    extraFields = FieldList(FormField(ExtraForm), label='Properties', description='Enter a label name and add a value to it',min_entries=1,id='extraWestFields')

class WestDeleteForm(Form):
    """
    Form for deletion: delete.html
    """
    dockerid = SelectField('Docker Id', description='Select Docker version')