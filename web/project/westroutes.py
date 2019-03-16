from flask import (
    render_template, request, jsonify, url_for, redirect)
from project import app
from project.views import (
    WestForm, PassCodeForm, WestCreateForm, WestDeleteForm)
from project.db import (
    DBAcessObjects, MongoDBConnection)


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    """ Fetches the homepage
    """
    form = WestForm(request.form)

    #mock/dummy values start
    form.westversion.choices = [('', ''), ('3.1.1', '3.1.1')]
    form.gccversion.choices = [('', ''), ('7.4', '7.4')]
    form.gfortanversion.choices = [('', ''), ('7.4', '7.4')]
    form.mpiversion.choices = [('', ''), ('7.4', '7.4')]
    form.fftwversion.choices = [('', ''), ('7.4', '7.4')]
    form.blasversion.choices = [('', ''), ('7.4', '7.4')]
    form.lapackversion.choices = [('', ''), ('7.4', '7.4')]
    form.pythonversion.choices = [('', ''), ('7.4', '7.4')]
    #end

    try:
        MongoDBConnection.getDB()
        dbAccessObj = DBAcessObjects()
        allwestlist = dbAccessObj.getAllInstances()
    except Exception as e:
        print("Could not connect to DB", e)
        return render_template('index.html', form=form)
    return render_template('index.html',allwestlist=allwestlist, form=form)

@app.route('/verifyPasscode',methods=['GET','POST'])
def verifypasscode():
    """ This method verifies with input passcode of flask connection.
    """
    verifyform = PassCodeForm(request.form)
    confirmpasscode = app.config['passkey']
    if request.method == 'POST' and verifyform.validate():
        if confirmpasscode == verifyform.passcode.data:
            return jsonify(msg="success"),200
        else:
            return jsonify(msg="failed"), 200
    return jsonify(msg="failed"), 401



@app.route('/westcreate',methods=['GET','POST'])
def westcreate():
    """ Insert new metadata procedure
    """
    MongoDBConnection.getDB()
    dbAccessObj = DBAcessObjects()
    form = WestCreateForm(request.form)
    verifyform = PassCodeForm(request.form)
    if request.method == 'POST' and form.validate():
        objId = dbAccessObj.insertIntoDB(form.data)
        return redirect(url_for('index'))
    return render_template('insert.html',form=form,verifyform=verifyform)

@app.route('/westdelete',methods=['GET','POST'])
def westdelete():
    """ Delete metadata procedure
    """
    MongoDBConnection.getDB()
    dbAccessObj = DBAcessObjects()
    verifyform = PassCodeForm(request.form)
    deleteform = WestDeleteForm(request.form)
    deleteform.dockerid.choices = [(id, id) for id in dbAccessObj.getAllIds()]
    if request.method == 'POST' and deleteform.validate():
        dbAccessObj = DBAcessObjects()
        dbAccessObj.deleteFromDB(deleteform.dockerid.data)
        return redirect(url_for('index'))
    return render_template('delete.html',form=deleteform,verifyform=verifyform)


