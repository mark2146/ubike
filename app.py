import os

from flask import Flask, render_template
from flask import jsonify
import requests

app = Flask(__name__, static_folder='immage')

@app.route('/')
def home():
    return render_template(
        'index.html',
        google_maps_api_key=os.getenv('GOOGLE_MAPS_API_KEY', ''),
    )

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
    try:
        response = requests.get(
            'https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1',
            timeout=(3.05, 10),
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, (list, dict)):
            raise ValueError('Unexpected upstream response shape')
        return jsonify(data)
    except (requests.RequestException, ValueError):
        return jsonify({'error': 'Station data is temporarily unavailable.'}), 503

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '').lower() in {'1', 'true', 'yes'})
app.config['TEMPLATES_AUTO_RELOAD'] = True
