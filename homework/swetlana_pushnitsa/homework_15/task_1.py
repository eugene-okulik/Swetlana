import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)


def new_student(name, second_name):
    query_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
    cursor.execute(query_student, (name, second_name))
    return cursor.lastrowid


def new_book(book_title, student_id):
    query_book = "INSERT INTO books (title, taken_by_student_id) values (%s, %s)"
    cursor.execute(query_book, (book_title, student_id))
    return cursor.lastrowid


def new_group(title_of_group, start_date, end_date):
    query_group = "INSERT INTO `groups` (title, start_date, end_date) values (%s, %s, %s)"
    cursor.execute(query_group, (title_of_group, start_date, end_date))
    return cursor.lastrowid


def update_group(group_id, student_id):
    query_update_group = "UPDATE students SET group_id = %s WHERE id = %s"
    cursor.execute(query_update_group, (group_id, student_id))
    return cursor.lastrowid


def new_subject(subject_title):
    query_subject = "INSERT INTO subjets (title) VALUES (%s)"
    cursor.execute(query_subject, (subject_title,))
    return cursor.lastrowid


def new_lesson(lesson_title, subject_id):
    query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    cursor.execute(query_lessons, (lesson_title, subject_id))
    return cursor.lastrowid


def marks(mark, lesson_id, student_id):
    query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    cursor.execute(query_marks, (mark, lesson_id, student_id))
    return cursor.lastrowid


jj_oliver_id = new_student('J.J', 'Oliver')
book_python_id = new_book('Python', jj_oliver_id)
book_testing_software_id = new_book('Testing Software', jj_oliver_id)
book_testcases_id = new_book('Testcases', jj_oliver_id)
monty_python_group_id = new_group('Monty Python', 'jan 2025', 'jan 2026')
add_JJ_Oliver_in_group = update_group(monty_python_group_id, jj_oliver_id)

programming_languages_id = new_subject('Programming languages')
theory_of_developing_id = new_subject('Theory of developing')
math_id = new_subject('Mathematics')
python_lesson_id = new_lesson('Python', programming_languages_id)
javascript_lesson_id = new_lesson('JavaScript', programming_languages_id)
agile_lesson_id = new_lesson('Agile', theory_of_developing_id)
waterfall_lesson_id = new_lesson('Waterfall', theory_of_developing_id)
algebra_lesson_id = new_lesson('Algebra', math_id)
geometry_lesson_id = new_lesson('Geometry', math_id)

mark_python = marks(5, python_lesson_id, jj_oliver_id)
mark_javascript = marks(3, javascript_lesson_id, jj_oliver_id)
mark_agile = marks(4, agile_lesson_id, jj_oliver_id)
mark_waterfall = marks(3, waterfall_lesson_id, jj_oliver_id)
mark_algebra = marks(4, algebra_lesson_id, jj_oliver_id)
mark_geometry = marks(5, geometry_lesson_id, jj_oliver_id)

marks_query = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(marks_query, (jj_oliver_id,))

marks_student = cursor.fetchall()

marks_query = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(marks_query, (jj_oliver_id,))
books_taken_by_student = cursor.fetchall()

query_all_info_about_student = '''
SELECT * FROM students
JOIN books
ON students.id = books.taken_by_student_id
JOIN marks
ON students.id = marks.student_id
JOIN lessons
ON marks.lesson_id = lessons.id
WHERE students.id = %s
'''

cursor.execute(query_all_info_about_student, (jj_oliver_id,))
all_info_about_student = cursor.fetchall()

db.commit()

print(all_info_about_student)

db.close()
