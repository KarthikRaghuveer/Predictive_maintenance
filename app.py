import numpy as np
from flask import Flask,render_template,request
import pickle

app=Flask(__name__, template_folder='templates')
model= pickle.load(open(r'C:\Users\User\Downloads\Predictive_maintenance\fail_detect.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
    
@app.route('/predict_failure',methods=['POST'])
def predict_failure():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    #print(round(prediction[0],0))

    if output ==0:
        output1='Not fail'
    else:
        output1='Fail'
    return render_template('index.html',prediction_text='The machine is very likely ${}'.format(output1))
    
    
if __name__=="__main__":
    app.run(debug=True)