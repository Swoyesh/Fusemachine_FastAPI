from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
import os
from contextlib import asynccontextmanager

from apps.my_app.calculator import add, subtract, multiply, divide

# Configuration using environment variables (12-Factor: III. Config)
class Settings(BaseModel):
    app_name: str = Field(default="Calculator API")
    debug_mode: bool = Field(default=False)
    version: str = Field(default="0.1.0")

    @classmethod
    def from_env(cls):
        return cls(
            app_name=os.getenv("APP_NAME", "Calculator API"),
            debug_mode=os.getenv("DEBUG_MODE", "False").lower() == "true",
            version=os.getenv("APP_VERSION", "0.1.0")
        )

settings = Settings.from_env()

# Define request models
class CalculationRequest(BaseModel):
    a: float
    b: float

class CalculationResponse(BaseModel):
    result: float
    operation: str

# Startup and shutdown events (12-Factor: IX. Disposability)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print(f"Starting {settings.app_name} v{settings.version}")
    yield
    # Shutdown logic
    print(f"Shutting down {settings.app_name}")

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="A simple calculator API built with FastAPI",
    version=settings.version,
    debug=settings.debug_mode,
    lifespan=lifespan
)

#Calculator endpoints
@app.post("/add", response_model=CalculationResponse)
async def add_numbers(request: CalculationRequest):
    result = add(request.a, request.b)
    return CalculationResponse(result=result, operation="add")

@app.post("/subtract", response_model=CalculationResponse)
async def subtract_numbers(request: CalculationRequest):
    result = subtract(request.a, request.b)
    return CalculationResponse(result=result, operation="subtract")

@app.post("/multiply", response_model=CalculationResponse)
async def multiply_numbers(request: CalculationRequest):
    result = multiply(request.a, request.b)
    return CalculationResponse(result=result, operation="multiply")

@app.post("/divide", response_model=CalculationResponse)
async def divide_numbers(request: CalculationRequest):
    try:
        result = divide(request.a, request.b)
        return CalculationResponse(result=result, operation="divide")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))