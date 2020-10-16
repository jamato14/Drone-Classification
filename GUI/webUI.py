from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.php')

@app.route('/results.html')
def results():
    files = os.listdir("../TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results/")
    files.sort()
    return render_template('results.html',files=files)

@app.route('/train/<epochs>/<val_split>')
def training(epochs=5,val_split=.35):
    subprocess.call(['./train.sh', '--epochs', epochs, '--val_split', str(val_split)])
    return render_template('index.php')

@app.route('/inference')
def inference():
    subprocess.call("./inference.sh")
    return render_template('index.php')

    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
