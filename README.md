# FastAPI Profile API

A simple FastAPI application that serves user profile information along with random cat facts.

## Features

- **User Profile Endpoint** - Returns user information (email, name, tech stack)
- **Cat Facts Integration** - Fetches random cat facts from an external API
- **Async Support** - Built with FastAPI's async capabilities for fast performance
- **ISO 8601 Timestamps** - Returns UTC timestamps in standardized format
- **Error Handling** - Graceful fallback when external APIs are unavailable

## Project Structure

```
stage0_profile_api/
├── main.py              # Main FastAPI application
├── config.py            # Configuration and constants
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables (if using)
├── __pycache__/         # Python cache directory
└── README.md            # Project documentation
```

### File Descriptions

- **main.py** - Contains the FastAPI app with route handlers and the cat facts fetching logic
- **config.py** - Stores configuration variables like email, name, stack, and API endpoints
- **requirements.txt** - Lists all Python package dependencies

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd stage0_profile_api
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependencies are:
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server to run the application
- **httpx** - Async HTTP client for external API calls

## Running Locally

### 1. Start the Development Server

```bash
python main.py
```

You should see output like:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

Alternatively, you can use uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Access the API

Open your browser or use a tool like Postman or cURL.

**Base URL:** `http://localhost:8000`

#### Health Check Endpoint

```
GET http://localhost:8000/
```

**Response:**
```json
{
  "message": "Server is running",
  "status": "ok"
}
```

#### Get Profile with Cat Fact

```
GET http://localhost:8000/me
```

**Response:**
```json
{
  "status": "success",
  "user": {
    "email": "ogukwee91@gmail.com",
    "name": "Emmanuel Ogukwe",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T14:30:45Z",
  "fact": "Cats have a specialized collarbone that allows them to squeeze through tight spaces."
}
```

### 3. Interactive API Documentation

FastAPI automatically generates interactive documentation:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Deployment

### Deployed URL

The application is deployed and accessible at:

```
https://hng13-stage-0-backend.onrender.com/
```

### Access Deployed Endpoints

**Health Check:**
```
GET https://hng13-stage-0-backend.onrender.com/
```

**Get Profile:**
```
GET https://hng13-stage-0-backend.onrender.com/me
```


- Ensure your app is listening on `0.0.0.0` (not `127.0.0.1`)
- Check that the PORT environment variable is being read correctly
- Review the deployment logs for startup errors

### Dependencies Installation Issues

```bash
# Upgrade pip first
pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

### External API Timeout

If the cat facts API is slow, the fallback message will be returned:
```json
"fact": "Could not fetch a cat fact at this time."
```

## API Response Format

All responses follow this structure:

**Success Response:**
```json
{
  "status": "success",
  "user": {
    "email": "string",
    "name": "string",
    "stack": "string"
  },
  "timestamp": "ISO 8601 string",
  "fact": "string"
}
```

**Status Codes:**
- `200 OK` - Request successful
- `500 Internal Server Error` - Server error (rarely occurs due to error handling)

## Dependencies

See `requirements.txt` for the complete list:

```
fastapi
uvicorn
httpx
```

