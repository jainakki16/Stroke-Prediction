import flask
import pandas as pd
from joblib import load


app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    pipeline = load("stroke_model.joblib")
    result = pipeline.predict(pd.DataFrame(to_predict_list, index=[0]))
    return result[0]


@app.route('/result', methods=['POST'])
def result():
    if flask.request.method == 'POST':
        to_predict_list = flask.request.form.to_dict()

        to_predict_list['marital_status'] = to_predict_list.pop('martial_stat')
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

        return flask.render_template("result.html", prediction=prediction)


app.run()
