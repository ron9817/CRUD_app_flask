from flask import Flask,render_template,request, jsonify, make_response
from model import *
app=Flask(__name__)


@app.route("/update/<id>", methods=["get","post"])
def update(id):
    if request.method=="POST":
        form=request.form
        name=form["name"]
        category=form["category"]
        description=form["description"]
        data={}
        if name is not None:
            data["name"]=name
        else:
            data["name"]=""
        if name is not None:
            data["category"]=category
        else:
            data["category"]=""
        if name is not None:
            data["description"]=description
        else:
            data["description"]=""
        db=Database()
        code=db.update(id,data)
        if code==1:
            return jsonify({'response': "Successful"})
        elif code==0:
            return jsonify({'response': "Unsuccessful"})
        else:
            return jsonify({'response': "Error"})
    else:
        db=Database()
        result,code=db.selectID(id)
        if code==1:
            for i,j in result.items():
                name=j[0]
                category=j[1]
                description=j[2]
            return render_template("updateView.html",id=id, name=name, category=category, description=description)
        else:
            return render_template("updateView.html",id=id, name="", category="", description="")


@app.route("/insert", methods=["get","post"])
def insert():
    if request.method=="POST":
        form=request.form
        name=form["name"]
        category=form["category"]
        description=form["description"]
        data={}
        if name is not None:
            data["name"]=name
        else:
            data["name"]=""
        if name is not None:
            data["category"]=category
        else:
            data["category"]=""
        if name is not None:
            data["description"]=description
        else:
            data["description"]=""

        db=Database()
        code=db.insert(data)
        if code==1:
            return jsonify({'response': "Successful"})
        elif code==0:
            return jsonify({'response': "Unsuccessful"})
        else:
            return jsonify({'response': "Error"})
    else:
        return render_template("InsertView.html")



@app.route("/delete/<id>")
def delete(id):
    db=Database()
    code=db.delete(id)
    if code==1:
        return jsonify({'response': "Successful"})
    elif code==0:
        return jsonify({'response': "Unsuccessful"})
    else:
        return jsonify({'response': "Error"})


@app.route('/')
@app.route("/view")
@app.route("/view/<id>")
def view(id=None):
    if id is None:
        db=Database()
        result,code=db.select()
        return render_template("viewView.html",result=result, code=code)
    else:
        db=Database()
        result,code=db.selectID(id)


        response=""""""
        #response="""<div class="row"><div class="col"></div><div class="col">"""
        for i,k in result.items():
            response+="""<div class="row"><div class="col">ID</div><div class="col">"""+str(i)+"""</div></div>"""
            counterloop=0
            for j in k:
                counterloop+=1
                response+="""<div class="row"><div class="col">"""
                if counterloop ==1 :
                    response+="""Name"""
                if counterloop ==2 :
                    response+="""Category"""
                if counterloop ==3 :
                    response+="""Description"""
                response+="""</div><div class="col">"""+j+"""</div></div>"""
        if code==0:
            response+="""<div class=row><div class=col></div><div class=col>Some error occured</div><div class=col></div></div>"""
        #response+="""</div><div class="col"></div></div>"""
        return jsonify({'response': response})
        #return render_template("detailsviewView.html",result=result, code=code)

