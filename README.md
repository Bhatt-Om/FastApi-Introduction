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

Let's go through each method in your FastAPI code and provide detailed explanations for each.

### 1. `index` - Get All Students
```python
@app.get("/")
def index():
    return students
```
- **Description**: This endpoint retrieves a dictionary containing all student records.
- **Method**: `GET`
- **Response**: Returns a JSON object with the details of all students.

### 2. `get_student` - Get Student by ID
```python
@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
```
- **Description**: This endpoint retrieves a specific student record by providing the student ID.
- **Method**: `GET`
- **Parameters**: `student_id` (int) - ID of the student to retrieve.
- **Response**: Returns a JSON object with the details of the specified student.

### 3. `get_student_by_name` - Get Student by Name
```python
@app.get("/get-by-name")
def get_student_by_name(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}
```
- **Description**: This endpoint retrieves a student record by providing the student's name.
- **Method**: `GET`
- **Parameters**: `name` (optional, str) - Name of the student to retrieve.
- **Response**: Returns a JSON object with the details of the matching student or a message if not found.

### 4. `create` - Create Student
```python
@app.post("/create-student/{student_id}")
def create(student_id: int, student: Student):
    if student_id in students:
        return { "Error": "Student exists" }

    students[student_id] = student
    return students[student_id]
```
- **Description**: This endpoint creates a new student record with the provided details.
- **Method**: `POST`
- **Parameters**: `student_id` (int) - ID for the new student.
- **Request Body**: JSON object containing `name`, `age`, and `email`.
- **Response**: Returns the details of the created student.

### 5. `update_student` - Update Student
```python
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return { "Error": "Student Does Not Exist" }

    if student.name is not None:
        students[student_id].name = student.name

    if student.age is not None:
        students[student_id].age = student.age

    if student.email is not None:
        students[student_id].email = student.email

    return students[student_id]
```
- **Description**: This endpoint updates the details of a specific student with the provided values.
- **Method**: `PUT`
- **Parameters**: `student_id` (int) - ID of the student to update.
- **Request Body**: JSON object containing optional fields: `name`, `age`, and `email`.
- **Response**: Returns the updated details of the student.

### 6. `delete_student` - Delete Student
```python
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return { "Error": "Student Does Not Exist" }

    del students[student_id]
    return { "Message": "Student Deleted Successfully" }
```
- **Description**: This endpoint deletes a specific student record.
- **Method**: `DELETE`
- **Parameters**: `student_id` (int) - ID of the student to delete.
- **Response**: Returns a message confirming the deletion.
