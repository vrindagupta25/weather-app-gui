# app.py (Python Flask Backend)
import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from flask_cors import CORS # Using flask_cors for simplicity in development/demo

# Load environment variables from .env file at the very start
load_dotenv()

app = Flask(__name__, static_folder='static')

# --- DevSecOps Principle: CORS Configuration ---
# Allow requests from all origins during development.
# In production, restrict this to your specific frontend domain(s).
CORS(app)

# --- Configuration ---
# DevSecOps Principle: API Key Protection
# API key is accessed only on the backend, never exposed to the frontend.
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# --- Route to serve the static frontend HTML ---
@app.route('/')
def serve_index():
    """Serves the main HTML file for the frontend."""
    return send_from_directory(app.static_folder, 'index.html')

# --- API Endpoint for Weather Data ---
@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    """
    Fetches weather data for a given city and returns it as JSON.
    DevSecOps Principles:
    - Input Validation: Checks for 'city' parameter.
    - API Key Protection: Uses backend-only API key.
    - Error Handling: Catches various API and network errors.
    - No sensitive info leakage in error messages.
    """
    city_name = request.args.get('city')

    # DevSecOps Principle: Input Validation (Server-side)
    if not city_name:
        return jsonify({"error": "City name is required"}), 400

    if not OPENWEATHER_API_KEY:
        print("CRITICAL ERROR: OpenWeather API key not found. Check .env file.")
        return jsonify({"error": "Server configuration error: API key missing."}), 500

    params = {
        "q": city_name,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric" # Use 'imperial' for Fahrenheit
    }

    try:
        # Make the request to OpenWeatherMap API
        response = requests.get(OPENWEATHER_BASE_URL, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

        weather_data = response.json()

        # Check for specific API error codes from OpenWeatherMap (e.g., city not found)
        if weather_data.get("cod") == "404":
            return jsonify({"error": f"City '{city_name}' not found."}), 404
        elif weather_data.get("cod") != 200: # Generic OpenWeatherMap API error
             return jsonify({"error": f"OpenWeatherMap API error: {weather_data.get('message', 'Unknown error')} "}), 500

        # Return the weather data to the frontend
        return jsonify(weather_data)

    except requests.exceptions.HTTPError as http_err:
        # DevSecOps Principle: Generic error messages for client
        print(f"HTTP error occurred: {http_err} - Status: {response.status_code} - Response: {response.text}")
        return jsonify({"error": "Error fetching weather data. Please try again later."}), 500
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return jsonify({"error": "Network error. Please check your internet connection."}), 503
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return jsonify({"error": "Request timed out. Please try again."}), 504
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected request error occurred: {req_err}")
        return jsonify({"error": "An unexpected error occurred."}), 500
    except ValueError as json_err:
        print(f"Error decoding JSON response: {json_err} - Raw response: {response.text}")
        return jsonify({"error": "Invalid response from weather service."}), 500

# --- Health Check (for Docker/orchestration) ---
@app.route('/health')
def health_check():
    """Simple health check endpoint."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Use 0.0.0.0 to make the Flask app accessible from outside the container
    app.run(debug=os.getenv("FLASK_DEBUG", "True") == "True", host='0.0.0.0', port=5000)