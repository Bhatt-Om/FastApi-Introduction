from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
  1:{
      "name": "om",
      "age": 22,
      "email": "ombhatt1111@gmail.com"
  }
}

class Student(BaseModel):
    name: str
    age: int
    email: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

@app.get("/")
def index():
    return students

@app.get("/get-studednt/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
      if students[student_id]["name"] == name:
          return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create(student_id: int, student: Student):
    if student_id in students:
        return { "Error": "Student exists" }

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
      return { "Error": "Student Does Not Exist" }

    # if we don't do this it will only return the value that is coming from response other will be nil
    if student.name != None:
      students[student_id].name = student.name

    if student.age != None:
      students[student_id].age = student.age

    if student.email != None:
      students[student_id].email = student.email

    students[student_id] = student
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
      return { "Error": "Student Does Not Exist" }

    del students[student_id]
    return { "Message": "Student Deleted SuccessFully" }