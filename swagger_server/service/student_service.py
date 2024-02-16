from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017')
db = client['student_db']
students = db.create_collection('students')


def add(student=None):
    existing_student = students.find_one({'first_name': student.first_name, 'last_name': student.last_name})
    if existing_student:
        return 'already exists', 409
    result = students.insert_one(student.to_dict())
    student.student_id = str(result.inserted_id)
    return student.student_id


def get_by_id(student_id=None, subject=None):
    student = students.find_one({'student_id': student_id})
    if not student:
        return 'not found', 404
    student['student_id'] = student_id
    print(student)
    return student


def delete(student_id=None):
    student = students.find_one({'student_id': student_id})
    if not student:
        return 'not found', 404
    students.delete_one({'student_id': student_id})
    return student_id
