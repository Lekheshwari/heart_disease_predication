from flask import Flask , jsonify , redirect ,url_for , render_template,request
import config
from utils import HeartDisease
import sklearn
import pandas 
import numpy


app = Flask(__name__)

@app.route('/prediction', methods = ["POST","GET"])
def make_predication():
    if request.method == "POST":
        data = request.form


        pred = HeartDisease(data)
        result = pred.predication_heart()

        return jsonify({"Predication": result})
    

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NO)