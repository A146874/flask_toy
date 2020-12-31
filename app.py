from flask import Flask, redirect, url_for, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = '99999999999999'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model", methods=['GET', 'POST'])
def model():
    if request.method == "POST":
        # submitting data
        f1 = float(request.form['f1'])
        f2 = float(request.form['f2'])
        session['prediction'] = f2 + (f2-f1)
        return redirect(url_for("predict"))
    else:
        # collecting new data
        session.pop('prediction', None)
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