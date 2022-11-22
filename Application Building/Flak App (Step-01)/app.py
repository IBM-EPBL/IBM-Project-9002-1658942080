import numpy as np
import requests as requests
from flask import Flask, request, jsonify, render_template
import pickle
# importing the feature file used to analyze the URL
import feature
import _json


import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<j8gnwjgK1Pk7vrnA7wND_ivnq17Bh4dlbFy3-iq_s-mt>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
url = request.form['url']
        obj = feature.FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30)
        print(x.tolist())

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["index",	"having_IPhaving_IP_Address", "URLURL_Length",	"Shortining_Service","having_At_Symbol",	"double_slash_redirecting",	"Prefix_Suffix",	"having_Sub_Domain","SSLfinal_State","SSLfinal_State",	"Domain_registeration_length","Favicon","port",	"HTTPS_token",	"Request_URL",	"URL_of_Anchor",	"Links_in_tags",	"SFH",	"Submitting_to_email",	"Abnormal_URL",	"Redirect",	"on_mouseover",	"RightClick",	"popUpWidnow",	"Iframe",	"age_of_domain",	"DNSRecord",	"web_traffic",	"Page_Rank",	"Google_Index",	"Links_pointing_to_page",	"Statistical_report"
        ]], "values": x.tolist()}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/wpd/predictions?version=2022-11-22', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())

response_text = response_scoring.json()
y_pred = response_text['predictions'][0]['values'][0][0]
y_pro_phishing = response_text['predictions'][0]['values'][0][1][0]
y_pro_non_phishing = response_text['predictions'][0]['values'][0][1][1]

# load model
class Flask:
    pass


app = Flask(__name__)
model = pickle.load(open('Phishing_website.pkl', 'rb'))


# fetches the URL given by the URL and passes to feature
@app.route('/_predict', methods=['POST'])
def y_predict():
    '''
        For rendering results on HTML GUI
        '''

    url = request.form['URL']
    checkprediction = feature.main(url)
    prediction = model.predict(checkprediction)
    print(prediction)
    output = prediction[0]
    if (output == 1):
        pred = "Your are safe!!  This is a Legitimate Website."
    else:
        pred = "Your are on the wrong site. Be cautious!"
    return render_template('final.html', prediction_text='{}'.formate(pred), url=url)


# Takes the input parameters fetched from the URL by inputsScript and returns the
@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
        For direct API calls trought request
        '''

    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)