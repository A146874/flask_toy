from flask import Flask, redirect, url_for, render_template, request, session
import random
import model

app = Flask(__name__)
app.secret_key = '99999999999999'

mm = model.MeanModel()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model", methods=['GET', 'POST'])
def model():
    if request.method == "POST":
        # submitting data
        f1 = float(request.form['f1'])
        f2 = float(request.form['f2'])
        features = [f1, f2]
        session['prediction'] = mm.predict(features)
        return redirect(url_for("predict"))
    else:
        # collecting new data
        session.pop('prediction', None) # delete old prediction
        return render_template("model.html")

@app.route("/predict")
def predict():
    if 'prediction' in session:
        prediction = session['prediction']
        return render_template('predict.html', prediction=prediction)
    else:
        return redirect(url_for('model'))

if __name__ == '__main__':
    app.run(debug=True)