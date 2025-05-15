Prerequisites

Python 3.8+
Docker and Docker Compose (optional)
Git

Local Development
Clone the Repository
bashgit clone https://github.com/Swoyesh/Fusemachine_FastAPI.git
cd calculator-fastapi
Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bashpip install -r requirements/dev.txt
Set Up Environment Variables
bashcp .env.example .env
Edit the .env file to customize your configuration:
APP_NAME=Calculator API
APP_VERSION=0.1.0
DEBUG_MODE=True
PORT=8000
Run the Application
bashpython serve.py
The API will be available at http://localhost:8000, and the interactive documentation at http://localhost:8000/docs.
Using Docker
Run with Docker Compose
bashdocker-compose up -d
This will build the Docker image and start the container. The API will be available at http://localhost:8000.
Run with Docker Directly
bashdocker build -t calculator-api .
docker run -p 8000:8000 -d calculator-api
Testing the API
Using the Interactive Documentation

Open http://localhost:8000/docs in your browser
Try out the different endpoints using the interactive interface

Using curl

# Addition
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'

# Subtraction
curl -X POST http://localhost:8000/subtract -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'

# Multiplication
curl -X POST http://localhost:8000/multiply -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'

# Division
curl -X POST http://localhost:8000/divide -H "Content-Type: application/json" -d '{"a": 6, "b": 2}'
Running Tests
bashpytest
Or with coverage:
bashpytest --cov=my_app tests/