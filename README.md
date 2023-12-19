# MyAPI - FastAPI Setup Guide

## Installation

### Step 1: Install Python

Ensure that Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install FastAPI

```bash
  pip install fastapi
```

FastAPI requires an ASGI server for production, such as Uvicorn or Hypercorn. Install Uvicorn with:

```bash
  pip install "uvicorn[standard]"
```

### Step 3: Install Uvicorn (ASGI server)

On Ubuntu, you can install Uvicorn using the following command:

```bash
  sudo apt install uvicorn
```

## Running FastAPI

To run the FastAPI application, execute the following command in your terminal:

```bash
  uvicorn myapi:app --reload
```

Replace `myapi` with the name of your FastAPI file.

## API Documentation

FastAPI automatically generates documentation for your API using Swagger UI.

To access the documentation, navigate to the following URL in your browser:

```
  http://127.0.0.1:8000/docs
```

This will provide an interactive interface where you can explore and test your API endpoints.
