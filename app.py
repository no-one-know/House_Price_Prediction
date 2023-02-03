from flask import Flask,render_template,redirect,url_for,request
import numpy as np
import gzip,joblib
from forms import details

app=Flask(__name__)

app.config['SECRET_KEY']='4ab8ae09bf8631c477c32bc99e4a1135'

with gzip.open('reg_model.gz','rb') as file:
    reg_model=joblib.load(file)

with gzip.open('std_model.gz','rb') as file:
    std_model=joblib.load(file)

@app.route("/",methods=['get','post'])
def home():
    form=details()
    if form.validate_on_submit():
        CRIM=form.crim.data
        ZN=form.zn.data
        INDUS=form.indus.data
        CHAS=form.chas.data
        NOX=form.nox.data
        RM=form.rm.data
        AGE=form.age.data
        DIS=form.dis.data
        RAD=form.rad.data
        TAX=form.tax.data
        PTRATIO=form.ptratio.data
        B_B=form.b.data
        LSTAT=form.lstat.data
        arr=np.array([CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B_B,LSTAT])
        arr=np.reshape(arr,(1,arr.size))
        arr=std_model.transform(arr)
        result=int(reg_model.predict(arr)[0])*1000
        return redirect(url_for('prediction',value=result))
    return render_template("home.html",form=form)

@app.route("/information",methods=['get'])
def information():
    return render_template("information.html")

@app.route("/prediction/<value>",methods=['get'])
def prediction(value):
    return render_template("prediction.html",value=value)

if __name__=='__main__':
    app.run(debug=True)