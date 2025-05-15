# Calculator_FASTAPI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-latest-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, modular calculator API built with FastAPI. This project follows the [12-Factor App](https://12factor.net/) methodology and demonstrates best practices for developing maintainable and scalable web applications.

**Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [12-Factor App Implementation](#12-factor-app-implementation)
- [License](#license)

---

**Project Overview**

This API performs basic arithmetic operations and is designed using FastAPI. It uses environment-based configuration and includes a comprehensive test suite. The structure supports scalability, modularity, and maintainability.

---

**Features**
* RESTful API using FastAPI
* Basic arithmetic operations: addition, subtraction, multiplication, division
* Environment-based configuration
* Automated testing using Pytest
* Documentation using MkDocs

---

**Project Structure**

```
Calculator_FASTAPI/
├── docs/
│   ├── guide/
│   │   └── getting-started.md
│   ├── index.md
│   └── mkdocs.yml
├── requirements/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   └── requirements-test.txt
├── src/
│   ├── apps/
│   ├── tests/
│   ├── main.py
│   └── serve.py
├── .env
├── .gitignore
├── Makefile
├── pytest.ini
├── pyproject.toml
├── README.md
└── LICENSE
```

---

**Getting Started**

**Prerequisites**
* Python 3.8+

**Installation**
1. **Clone the repository:**

```
git clone https://github.com/yourusername/Calculator_FASTAPI.git
cd Calculator_FASTAPI
```

2. **Create and activate a virtual environment:**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```
pip install -r requirements/requirements-dev.txt
```

4. **Set up environment variables:**

```
cp .env.example .env
```

5. **Run the application:**

```
python src/serve.py
```

---

**Usage**

**Send HTTP Requests**
* Use any HTTP client to interact with the API endpoints.
* All operations accept JSON payloads.

**Example Request:**

```
POST /add
Content-Type: application/json

{
  "a": 5,
  "b": 3
}
```

**Example Response:**

```
{
  "result": 8,
  "operation": "add"
}
```

---

**API Endpoints**

| Method | Endpoint   | Description                   |
|--------|------------|-------------------------------|
| POST   | /add       | Add two numbers               |
| POST   | /subtract  | Subtract one number from another |
| POST   | /multiply  | Multiply two numbers          |
| POST   | /divide    | Divide one number by another  |

---

**Testing**

**Run Basic Tests**
* Execute the test suite:

```
pytest
```

**Run Tests with Coverage**
* Get coverage metrics:

```
pytest --cov=src tests/
```

**Filter Tests**
* Run tests by keyword:

```
pytest -k "add"
```

**Run Specific Test File**
* Execute tests from a specific file:

```
pytest src/tests/test_calculator.py
```

**Generate HTML Coverage Report**
* Create detailed HTML coverage report:

```
pytest --cov=src --cov-report=html tests/
```

**Verbose Output**
* See detailed test information:

```
pytest -v
```

---

**12-Factor App Implementation**

This project adheres to the 12-Factor principles:

1. **Codebase**: One codebase tracked in version control, many deploys
2. **Dependencies**: Explicitly declared and isolated in requirement files
3. **Config**: Config stored in environment variables
4. **Backing Services**: Treated as attached resources
5. **Build, Release, Run**: Clearly separated stages
6. **Processes**: Stateless processes
7. **Port Binding**: Services exported via port binding
8. **Concurrency**: Supports horizontal scaling
9. **Disposability**: Fast startup and graceful shutdown
10. **Dev/Prod Parity**: Similar environments for dev and prod
11. **Logs**: Output as event streams
12. **Admin Processes**: Run management tasks as one-off processes

---

**License**

Distributed under the MIT License. See `LICENSE` for more information.
