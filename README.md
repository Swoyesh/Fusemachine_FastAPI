# Calculator_FASTAPI

A simple, modular calculator API built with FastAPI. This project follows the [12-Factor App](https://12factor.net/) methodology and demonstrates best practices for developing maintainable and scalable web applications.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Docker](#docker)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [12-Factor App Implementation](#12-factor-app-implementation)
- [License](#license)

## Project Overview

This API performs basic arithmetic operations and is designed using FastAPI. It is containerized with Docker, uses environment-based configuration, and includes a test suite. The structure supports scalability, modularity, and maintainability.

## Features

- RESTful API using FastAPI  
- Basic arithmetic operations: addition, subtraction, multiplication, division  
- Environment-based configuration  
- Docker containerization  
- Automated testing using Pytest  
- Documentation using MkDocs

## Project Structure

Calculator_FASTAPI/
├── docs/
│ ├── guide/
│ │ └── getting-started.md
│ ├── index.md
│ └── mkdocs.yml
├── requirements/
│ ├── requirements.txt
│ ├── requirements-dev.txt
│ └── requirements-test.txt
├── src/
│ ├── apps/
│ ├── tests/
│ ├── main.py
│ └── serve.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── Makefile
├── pytest.ini
├── pyproject.toml
├── README.md
└── LICENSE

bash
Copy
Edit

## Getting Started

### Prerequisites

- Python 3.8+  
- Docker and Docker Compose (optional)

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Calculator_FASTAPI.git
cd Calculator_FASTAPI
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements/requirements-dev.txt
Set up environment variables:

bash
Copy
Edit
cp .env.example .env
Run the application:

bash
Copy
Edit
python src/serve.py
Visit: http://localhost:8000/docs

Usage
Send HTTP POST requests to the respective endpoints with JSON input:

Example:

http
Copy
Edit
POST /add
Content-Type: application/json

{
  "a": 5,
  "b": 3
}
Response:

json
Copy
Edit
{
  "result": 8,
  "operation": "add"
}
Docker
Build and run the application using Docker Compose:

bash
Copy
Edit
docker-compose up -d
Visit: http://localhost:8000/docs

API Endpoints
Method	Endpoint	Description
POST	/add	Add two numbers
POST	/subtract	Subtract one number from another
POST	/multiply	Multiply two numbers
POST	/divide	Divide one number by another

Testing
Run the test suite:

bash
Copy
Edit
pytest
With coverage:

bash
Copy
Edit
pytest --cov=src tests/
12-Factor App Implementation
This project adheres to the 12-Factor principles:

Codebase: One codebase tracked in version control, many deploys

Dependencies: Explicitly declared and isolated in requirement files

Config: Config stored in environment variables

Backing Services: Treated as attached resources

Build, Release, Run: Clearly separated stages

Processes: Stateless processes

Port Binding: Services exported via port binding

Concurrency: Supports horizontal scaling

Disposability: Fast startup and graceful shutdown

Dev/Prod Parity: Similar environments for dev and prod

Logs: Output as event streams

Admin Processes: Run management tasks as one-off processes

License
Distributed under the MIT License. See LICENSE for more information.