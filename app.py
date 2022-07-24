import os

from flask import Flask, request, render_template
import pickle



app = Flask(__name__)

model_file = open('model.sav', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/run_script')
def run_script():
    dump_cmd = 'python C:/Users/ASUS-GK/Documents/dts-deployment-linreg/sraper_sender.py'
    p = os.popen(dump_cmd)
    return "test"

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/nonddos')
def index2():
    return render_template('index2.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    #age, sex, smoker = [x for x in request.form.values()]

    dt,pktcount,bytecount,pktperflow,byteperflow, pktrate,Pairflow,tx_kbps,rx_kbps,tot_kbps = [x for x in request.form.values()]

    data = [float(dt),float(pktcount),float(bytecount),float(pktperflow),float(byteperflow),float(pktrate),float(Pairflow),float(tx_kbps),float(rx_kbps),float(tot_kbps)]


    print("parameter")
    
    print(data)
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    if (output == 1):
         dump_cmd = 'python C:/Users/ASUS-GK/Documents/dts-deployment-linreg/sraper_sender.py'
         p = os.popen(dump_cmd)

    return render_template('index.html', prediksi=output)

@app.route('/predict2', methods=['POST'])
def predict2():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    #age, sex, smoker = [x for x in request.form.values()]

    dt,pktcount,bytecount,pktperflow,byteperflow, pktrate,Pairflow,tx_kbps,rx_kbps,tot_kbps = [x for x in request.form.values()]

    data = [float(dt),float(pktcount),float(bytecount),float(pktperflow),float(byteperflow),float(pktrate),float(Pairflow),float(tx_kbps),float(rx_kbps),float(tot_kbps)]


    print("parameter")
    
    print(data)
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    if (output == 1):
         dump_cmd = 'python C:/Users/ASUS-GK/Documents/dts-deployment-linreg/sraper_sender.py'
         p = os.popen(dump_cmd)

    return render_template('index2.html', prediksi=output)
   


if __name__ == '__main__':
    app.run(debug=True)