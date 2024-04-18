from flask import Flask, request, jsonify, Blueprint
import util
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Create a Blueprint for API routes with prefix '/api'
# api_bp = Blueprint('api', __name__, url_prefix='/api')
# app.register_blueprint(api_bp)  # Register the Blueprint with the app


@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'location': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk =  int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify(
        {
            'estimated_price': util.get_estimated_price(location=location, sqft= total_sqft, bath=bath, bhk=bhk),
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print(os.getcwd())
    print("Starting Python Flash Server...")
    app.run(host="0.0.0.0")