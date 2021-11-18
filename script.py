import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request


app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,10)
    loaded_model = pickle.load(open("model_final_pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        
        to_predict_list['age'] = int(to_predict_list['age'])
        to_predict_list['hypert'] = int(to_predict_list['hypert'])
        to_predict_list['heart_d'] = int(to_predict_list['heart_d'])
        to_predict_list['avg_gl'] = int(to_predict_list['avg_gl'])
        to_predict_list['c_loss'] = int(to_predict_list['c_loss'])

        to_predict_list=list(to_predict_list.values())
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='chance of getting stroke'
        else:
            prediction='Not a chance of getting stroke for now'
            
        return render_template("result.html",prediction=to_predict_list)

app.run()