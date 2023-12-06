from flask import Flask, render_template
from flask import jsonify

import requests

app = Flask(__name__, static_folder='immage')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/rate')
def rate():
    return render_template('rate.html')

@app.route('/self')
def self_page():
    return render_template('self.html')

@app.route('/data')
def get_data():
    response = requests.get('https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
