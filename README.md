**Weather Application (GUI)**
A real-time, interactive weather application with a modern graphical user interface, built using a Python Flask backend and a responsive HTML/CSS/JavaScript frontend (Tailwind CSS). This project demonstrates API integration, client-server architecture, and explicitly incorporates DevSecOps principles.

✨ Features
Real-time Weather Data: Fetches and displays current weather conditions for any city worldwide.

Intuitive User Interface: Clean, responsive, and modern design built with HTML, vanilla JavaScript, and Tailwind CSS.

Temperature & Details: Shows temperature, "feels like" temperature, weather description, humidity, and wind speed.

Error Handling: Graceful handling of invalid city names, network errors, and API issues.

🔒 DevSecOps Principles Applied
This project was developed with DevSecOps principles integrated from the ground up:

1. API Key Protection:

The OpenWeatherMap API key (OPENWEATHER_API_KEY) is stored securely in a .env file on the backend server.

It is never exposed to the client-side (frontend), preventing unauthorized access or leakage. All API calls to OpenWeatherMap are proxied through the Flask backend.

2. Input Validation & Sanitization:

Frontend: User input (city name) is trimmed and URI-encoded (encodeURIComponent) before being sent to the backend, mitigating basic injection risks.

Backend (Server-side): The Flask application performs server-side validation to ensure the city name is provided before making an external API call. This prevents unnecessary or malicious requests to the external weather API.

3. Robust Error Handling & Information Disclosure Prevention:

Backend: Comprehensive try-except blocks are implemented in app.py to catch various requests exceptions (HTTP errors, connection issues, timeouts, JSON decoding errors) when communicating with OpenWeatherMap.

Secure Error Responses: Generic, user-friendly error messages are returned to the frontend (e.g., "City not found", "Error fetching weather data") instead of leaking sensitive backend details or raw API error messages.

Frontend: Displays clear error messages to the user when issues occur, improving user experience and guiding troubleshooting.

4. CORS (Cross-Origin Resource Sharing) Configuration:

Flask-CORS is used in the backend (app.py) to explicitly manage cross-origin requests.

Production Readiness: While set to allow all origins for development simplicity, it is explicitly noted that in a production environment, this would be strictly configured to allow requests only from trusted frontend domains, preventing cross-site scripting vulnerabilities.

5. Containerization & Reproducibility (Infrastructure as Code - IaC):

The entire application (Flask backend + static frontend files) is containerized using Docker.

A multi-stage Dockerfile ensures a lean production image, separating build-time dependencies from runtime.

docker-compose.yml orchestrates the application locally, defining how the container is built and run, ensuring a consistent and reproducible environment across different machines. This demonstrates IaC principles by defining the application's runtime environment programmatically.

6. Version Control (.gitignore):

A .gitignore file is meticulously configured to prevent sensitive files (like .env containing API keys) and unnecessary build artifacts/dependencies (__pycache__, venv/) from being committed to the public GitHub repository. This is fundamental for maintaining security in open-source projects.

🏛️ Architecture
The application follows a standard client-server architecture:

graph TD
    User(Web Browser) -->|HTTP Requests| Frontend(HTML/CSS/JS with Tailwind)
    Frontend -->|API Call (Fetch Weather)| Backend(Python Flask Server)
    Backend -->|API Call (OpenWeatherMap API Key Protected)| OpenWeatherMap(OpenWeatherMap API)
    OpenWeatherMap -->|Weather Data| Backend
    Backend -->|JSON Weather Data| Frontend
    Frontend -->|Display UI| User

Frontend (Static Files): Served by the Flask backend, this includes index.html (structure), script.js (client-side logic), and style.css (minimal custom styles). Tailwind CSS is loaded via CDN for rapid styling.

Backend (Python Flask): A lightweight server that exposes a /api/weather endpoint. It acts as a proxy to the OpenWeatherMap API, securing the API key and performing server-side logic.

OpenWeatherMap API: Provides the raw weather data.
