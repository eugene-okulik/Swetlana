import csv
import os
import dotenv
import mysql.connector as mysql
from pathlib import Path


parent_dir = Path.cwd().parent.parent
file_path = parent_dir/"eugene_okulik/Lesson_16/hw_data/data.csv"
# new_file_path = Path.cwd()/"student_info_csv.csv"

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)

cursor = db.cursor(dictionary=True)
cursor.execute('''SELECT students.name, students.second_name, `groups`.title AS group_title, 
books.title AS book_title, subjets.title AS subject_title, lessons.title AS lesson_title, marks.value AS mark_value
FROM students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
''')
db_students = cursor.fetchall()

with open(file_path, newline='') as file:
    data_file = list(csv.DictReader(file))
    for student in data_file:
        if student not in db_students:
            print(student)
