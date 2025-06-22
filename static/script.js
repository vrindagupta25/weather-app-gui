// static/script.js (Frontend Logic)

// --- DevSecOps Principle: DOM Access Safety ---
// Cache DOM elements to avoid repeated lookups and potential errors.
const cityInput = document.getElementById('cityInput');
const fetchWeatherBtn = document.getElementById('fetchWeatherBtn');
const loadingIndicator = document.getElementById('loadingIndicator');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');
const weatherDisplay = document.getElementById('weatherDisplay');
const weatherCity = document.getElementById('weatherCity');
const weatherTemp = document.getElementById('weatherTemp');
const weatherFeelsLike = document.getElementById('weatherFeelsLike');
const weatherDesc = document.getElementById('weatherDesc');
const weatherHumidity = document.getElementById('weatherHumidity');
const weatherWind = document.getElementById('weatherWind');

// Base URL for your Flask backend API
// This would be replaced by an environment variable in a real production build process
const API_BASE_URL = window.location.origin; // Dynamically gets current origin (e.g., http://localhost:5000)

// --- Helper Functions for UI State Management ---
function showLoading() {
    loadingIndicator.classList.remove('hidden');
    weatherDisplay.classList.add('hidden');
    errorMessage.classList.add('hidden');
    fetchWeatherBtn.disabled = true; // Disable button while loading
}

function hideLoading() {
    loadingIndicator.classList.add('hidden');
    fetchWeatherBtn.disabled = false; // Re-enable button
}

function showWeatherDisplay() {
    weatherDisplay.classList.remove('hidden');
}

function hideWeatherDisplay() {
    weatherDisplay.classList.add('hidden');
}

function showErrorMessage(message) {
    errorText.textContent = message;
    errorMessage.classList.remove('hidden');
    hideWeatherDisplay(); // Hide weather display if an error occurs
}

function hideErrorMessage() {
    errorMessage.classList.add('hidden');
}

// --- Main Function to Fetch Weather ---
async function fetchWeather() {
    const city = cityInput.value.trim(); // DevSecOps Principle: Input Sanitization (Frontend)

    if (!city) {
        showErrorMessage('Please enter a city name.');
        return;
    }

    showLoading();
    hideErrorMessage(); // Clear previous errors

    try {
        // Fetch weather data from your Flask backend
        // DevSecOps Principle: API Key is handled by backend, not exposed here.
        const response = await fetch(`${API_BASE_URL}/api/weather?city=${encodeURIComponent(city)}`);

        // Check for HTTP errors
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({ error: 'Unknown server error' })); // Try to parse JSON error, fallback if not JSON
            showErrorMessage(errorData.error || `Error: ${response.status} ${response.statusText}`);
            return;
        }

        const data = await response.json();

        // Update UI with fetched data
        weatherCity.textContent = `${data.name}, ${data.sys.country}`;
        weatherTemp.textContent = data.main.temp.toFixed(1);
        weatherFeelsLike.textContent = data.main.feels_like.toFixed(1);
        weatherDesc.textContent = data.weather[0].description;
        weatherHumidity.textContent = data.main.humidity;
        weatherWind.textContent = data.wind.speed.toFixed(1);

        showWeatherDisplay();

    } catch (error) {
        // DevSecOps Principle: Catch network/fetch errors gracefully
        console.error('Fetch error:', error);
        showErrorMessage('Could not connect to the weather service. Please try again later.');
    } finally {
        hideLoading(); // Always hide loading indicator
    }
}

// --- Event Listeners ---
fetchWeatherBtn.addEventListener('click', fetchWeather);

// Allow pressing Enter key in the input field to trigger search
cityInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        fetchWeather();
    }
});

// Fetch weather for default city on page load
document.addEventListener('DOMContentLoaded', fetchWeather);
