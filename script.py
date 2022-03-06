import os
import flask
import pandas as pd
from joblib import load
from flask import url_for


app = flask.Flask(__name__, static_folder='assets', template_folder='templates')
app.config["DEBUG"] = False


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html')

def ValuePredictor(to_predict_list):
    pipeline = load("stroke_model.joblib")
    result = pipeline.predict(pd.DataFrame(to_predict_list, index=[0]))
    return result[0]


@app.route('/pred', methods=['GET','POST'])
def pred():
    return flask.render_template('pred.html')

@app.route('/upload', methods=['GET','POST'])   
def upload():
    if flask.request.method == 'POST':
        to_predict_list = flask.request.form.to_dict()

        to_predict_list['marital_status'] = to_predict_list.pop('marital')
        to_predict_list['work_type'] = to_predict_list.pop('w_class')
        to_predict_list['residence_type'] = to_predict_list.pop('resident')
        to_predict_list['smoking_status'] = to_predict_list.pop('smoking')
        to_predict_list['age'] = int(to_predict_list.pop('age'))
        to_predict_list['hypertension'] = int(to_predict_list.pop('hypert'))
        to_predict_list['heart_disease'] = int(to_predict_list.pop('heart_d'))
        to_predict_list['avg_glucose_level'] = int(to_predict_list.pop('avg_gl'))
        to_predict_list['bmi'] = int(to_predict_list.pop('c_loss'))

        result = ValuePredictor(to_predict_list)

        if int(result) == 1:
         
            prediction = "Please consult a doctor. Based on your inputs you are likely to get stroke."
        else:
            
            prediction = "Congratulations! Based on your inputs you are not likely to get a stroke."

        return flask.render_template("pred.html", prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
