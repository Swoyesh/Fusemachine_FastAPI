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

calculator-fastapi/
├── docs/                   # Documentation files
│   ├── api/                # API usage docs
│   ├── development/        # Development guides
│   ├── img/                # Images for documentation
│   └── index.md            # Documentation home page
├── requirements/           # Dependency files
│   ├── requirements.txt    # Production dependencies
│   ├── requirements-dev.txt  # Development dependencies
│   └── requirements-test.txt # Testing dependencies
├── src/                    # Source code
│   ├── api/                # API endpoints
│   │   ├── __init__.py
│   │   ├── calculator.py   # Calculator routes
│   │   └── router.py       # API router setup
│   ├── core/               # Core application code
│   │   ├── __init__.py
│   │   ├── config.py       # Configuration handling
│   │   └── exceptions.py   # Custom exceptions
│   ├── services/           # Business logic
│   │   ├── __init__.py
│   │   └── calculator.py   # Calculator operations
│   ├── tests/              # Test suite
│   │   ├── __init__.py
│   │   ├── conftest.py     # Test configuration
│   │   ├── test_api.py     # API tests
│   │   └── test_services.py # Service tests
│   ├── main.py             # FastAPI application setup
│   └── serve.py            # Application entry point
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker configuration
├── LICENSE                 # License file
├── Makefile                # Make commands for common tasks
├── pyproject.toml          # Project metadata and configuration
└── README.md               # Project documentation
bash
Copy
Edit

## Getting Started

### Prerequisites

- Python 3.8+  
- Docker and Docker Compose (optional)

### Installation

# Clone repository
git clone https://github.com/yourusername/calculator-fastapi.git
cd calculator-fastapi

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/requirements.txt

# Copy example environment file and modify as needed
cp .env.example .env

# Run the application
python src/serve.py
Visit http://localhost:8000/docs to see the interactive API documentation.
Docker Installation
bash# Build and start the container
docker-compose up -d

# View logs
docker-compose logs -f

### Configuration
The application uses environment variables for configuration:
VariableDescriptionDefaultHOSTHost to bind the server0.0.0.0PORTPort to bind the server8000LOG_LEVELLogging levelINFOENVIRONMENTApplication environmentdevelopment

### 12-Factor App Implementation
This project follows the 12-Factor App methodology:

Codebase: One version-controlled repository
Dependencies: Explicitly declared and isolated
Config: Stored in environment variables
Backing Services: N/A (stateless calculator)
Build, Release, Run: Separated stages via Dockerfile
Processes: Stateless processes
Port Binding: Self-contained with port binding
Concurrency: Scales horizontally via process model
Disposability: Fast startup and graceful shutdown
Dev/Prod Parity: Similar environments via Docker
Logs: Output as event streams
Admin Processes: Admin/maintenance tasks as one-offs

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

### License
Distributed under the MIT License. See LICENSE for more information.