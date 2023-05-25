from flask import Flask , request, render_template
from pymongo import MongoClient 
app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')
@app.route('/display',methods=['POST',"GET"])
def display():
    Name=request.form.get('Name')
    Age=request.form.get('Age')
    Gender=request.form.get('Gender')
    Date=request.form.get('Date')
    Time=request.form.get('Time')
    Myopia=request.form.get('Myopia')
    Hypermetropia=request.form.get('Hypermetropia')
    Wet_AMD=request.form.get('Wet_AMD')
    Dry_AMD=request.form.get('Dry_AMD')
    Cataract=request.form.get('Cataract')
    Diabetic_Retinopathy=request.form.get("Diabetic_Retinopathy")
    Glaucoma=request.form.get('Glaucoma')
    data={'Name':Name,'Age':Age,'Gender':Gender,'Date':Date,'Time':Time,'Myopia':Myopia,'Hypermetropia':Hypermetropia,'Wet_AMD':Wet_AMD,'Dry_AMD':Dry_AMD,'Cataract':Cataract,'Diabetic_Retinopathy':Diabetic_Retinopathy,'Glaucoma':Glaucoma}
    return render_template('display.html',Name=Name,Age=Age,Gender=Gender,Date=Date,Time=Time,Myopia=Myopia,Hypermetropia=Hypermetropia,Wet_AMD=Wet_AMD,Dry_AMD=Dry_AMD,Cataract=Cataract,Diabetic_Retinopathy=Diabetic_Retinopathy,Glaucoma=Glaucoma)

if __name__ == '__main__':
    app.run(debug=True)