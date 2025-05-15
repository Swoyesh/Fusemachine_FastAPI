Calculator API
A simple calculator API built with FastAPI that follows the 12-Factor App methodology.
Features

Basic arithmetic operations (add, subtract, multiply, divide)
RESTful API using FastAPI
Docker containerization
Environment-based configuration
Comprehensive test suite
CI/CD pipeline using GitHub Actions

12-Factor App Implementation
This project implements the following 12-Factor principles:

Codebase: One codebase tracked in version control, many deploys
Dependencies: Explicitly declare and isolate dependencies
Config: Store config in the environment
Backing services: Treat backing services as attached resources
Build, release, run: Strictly separate build and run stages
Processes: Execute the app as one or more stateless processes
Port binding: Export services via port binding
Concurrency: Scale out via the process model
Disposability: Maximize robustness with fast startup and graceful shutdown
Dev/prod parity: Keep development, staging, and production as similar as possible
Logs: Treat logs as event streams
Admin processes: Run admin/management tasks as one-off processes

Getting Started
Prerequisites

Python 3.8+
Docker and Docker Compose (optional)

Local Development

Clone the repository:
bashgit clone https://github.com/Swoyesh/Fusemachine_FastAPI.git
cd calculator-fastapi

Create a virtual environment and install dependencies:
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements/dev.txt

Set up environment variables:
bashcp .env.example .env

Run the application:
bashpython serve.py

Access the API documentation at http://localhost:8000/docs

Using Docker

Build and run using Docker Compose:
bashdocker-compose up -d

Access the API documentation at http://localhost:8000/docs

API Endpoints

POST /add - Add two numbers
POST /subtract - Subtract one number from another
POST /multiply - Multiply two numbers
POST /divide - Divide one number by another

Example Request/Response
Request:
jsonPOST /add
{
  "a": 5,
  "b": 3
}
Response:
json{
  "result": 8,
  "operation": "add"
}
Running Tests
bashpytest
Or with coverage:
bashpytest --cov=my_app tests/