import numpy as np
from Static import *
import pickle
from inputScript import main

app = Flask(__name__)

# use the model
model = pickle.load(open('Phishing_Website.pkl', "rb"))


@app.route('/dashboard')
def predict_data():
    return render_template('Secondpage.html')


@app.route('/form')
def single_page():
    return render_template('MainPage.html')


@app.route('/predictdata', methods=["GET", "POST"])
def get_prediction():
    url = request.form['url']
    print(url)
    print(type(url))
    checking = main(url)
    predicted_value = model.predict(checking)
    value = predicted_value[0]
    val = 0
    if value == 1:
        val = 1
        txt = "This is not a phishing website continue to use"
    else:
        val = 0
        txt = "This is a phishing website"
    return render_template("dashboard.html", predicted='{}'.format(txt), url=url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
