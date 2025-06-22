 Weather Application (GUI)
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

🚀 Getting Started
To run this application locally using Docker:

Prerequisites
Git: Install Git

Docker Desktop: Download and Install Docker Desktop. Ensure it's running before proceeding. On Windows, ensure WSL 2 is installed and up to date (wsl --update in PowerShell as Admin).

OpenWeatherMap API Key:

Go to https://openweathermap.org/api and sign up for a free account.

Navigate to your "API keys" section.

Generate a new API key if you don't have one, and copy it.

Crucially, confirm your email address by clicking the verification link in the email from OpenWeatherMap. New keys are often inactive until confirmed.

Setup Steps
Clone the Repository:

git clone https://github.com/vrindagupta25/weather-app-gui.git

Navigate to the Project Directory:

cd weather-app-gui

Create .env file:

In the root of the weather-app-gui directory, create a new file named .env (note the leading dot, no extension).

Paste your OpenWeatherMap API key into this file exactly as shown below:

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY_HERE

Important: Replace YOUR_OPENWEATHER_API_KEY_HERE with the actual API key you copied. Ensure there are no spaces around the = sign and no quotes around the key. This file is ignored by Git (.gitignore) to keep your key secure.

Build and Run with Docker Compose:

Open your terminal (e.g., VS Code integrated terminal).

Ensure Docker Desktop is running in the background.

In your terminal, confirm you are in the weather-app-gui directory.

Execute the Docker Compose command:

docker compose up --build

This command will build the Docker image (downloading Python, installing dependencies, copying files) and then start the Flask application container. This process might take a few minutes the first time.

Access the Application:

Once the Docker Compose command shows output indicating the Flask server is running (e.g., * Running on http://0.0.0.0:5000), open your web browser.

Go to: http://localhost:5000

You should now see the graphical weather application!

💡 Usage
Enter City Name: Type the name of a city (e.g., "London", "New York", "Mumbai", "Delhi", "Bengaluru") into the input field.

Get Weather: Click the "Get Weather" button or press Enter.

View Results: The application will display the current temperature, "feels like" temperature, weather description, humidity, and wind speed for the entered city.

Error Messages: If the city is not found or a network error occurs, a clear error message will be displayed.

🔮 Future Enhancements
Unit & Integration Tests: Add automated tests for both Flask backend API endpoints and frontend JavaScript logic.

Dark Mode Toggle: Implement a toggle to switch between light and dark themes.

Location-Based Weather: Add functionality to detect the user's current location and display weather automatically.

Forecast Display: Extend to show 3-day or 5-day weather forecasts.

Dedicated Hosting: Deploy to a cloud platform like AWS (ECS, App Runner, EC2) and integrate with a CI/CD pipeline (e.g., Jenkins, GitHub Actions) for automated builds and deployments.

Container Security Scanning: Integrate tools like Trivy or Snyk in the CI pipeline to scan Docker images for vulnerabilities.

📞 Contact
For any questions or suggestions, feel free to reach out.
