from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

class StudentDB(BaseModel):
    roll_no: int
    name: str
    year: str
    branch: str

students_info = []

# To load data from JSON file
def load_data():
    if os.path.exists('students.json'):
        with open('students.json', 'r') as f:
            data = json.load(f)
            return [StudentDB(**student) for student in data]
    return []

# To save data to JSON file
def save_data():
    with open('students.json', 'w') as f:
        json.dump([student.dict() for student in students_info], f)

save_data()
# Load existing data on startup
students_info = load_data()


#Home Method of the server
@app.get("/")
def read_root():
    return {"Hello From Question 1": "Welcome to Student Management System Designed Using FastAPI"}

#Get all student records existing in the system
@app.get("/students/", response_model=List[StudentDB])
def get_student_records():
    return students_info


#Get student record by roll number
@app.get("/student/{roll_no}", response_model=StudentDB)
def get_student_record(roll_no: int):
    for student in students_info:
        if student.roll_no == roll_no:
            return student
    raise HTTPException(status_code=404, detail="Student Record not found")

#Insert student record by roll number
@app.post("/insert_student_data/", response_model=StudentDB)
def create_student_record(student: StudentDB):
    students_info.append(student)
    save_data()
    return student

#Insert multiple student records
@app.post("/insert_students_data/", response_model=List[StudentDB])
def create_students_records(students: List[StudentDB]):
    for student in students:
        students_info.append(student)
    save_data()
    return students

#Update existing record
@app.put("/update_student_data/", response_model=StudentDB)
def update_student_data(student: StudentDB):
    for i in students_info:
        if i.roll_no == student.roll_no:
            i.name = student.name
            i.year = student.year
            i.branch = student.branch
            save_data()
            return i
    raise HTTPException(status_code=404, detail="Student Record not found")

#Delee existing record by roll number

@app.delete('/delete_student/{roll_no}')
def delete_student_record(roll_no: int):
    for i in students_info:
        if i.roll_no == roll_no:
            students_info.remove(i)
            save_data()
            return {"message": "Student Record deleted"}
    raise HTTPException(status_code=404, detail="Student Record not found")


#Shouldnt be used as same name can be there for multiple students
@app.delete('/delete_student/{name}')
def delete_student_record(name: str):
    for i in students_info:
        if i.name == name:
            students_info.remove(i)
            save_data()
            return {"message": "Student Record deleted"}
    raise HTTPException(status_code=404, detail="Student Record not found")
