import mysql.connector as mysql


db = mysql.connect(
    user = 'st-onl',
    passwd = 'AVNS_tegPDkI5BlB2lW5eASC',
    host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port = 25060,
    database = 'st-onl'
)


cursor = db.cursor(dictionary=True)


query_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(query_student, ('Thomas', 'Mann'))
new_student_id = cursor.lastrowid

query_book = "INSERT INTO books (title, taken_by_student_id) values (%s, %s)"
cursor.executemany(
    query_book, [
        ('Magic Rock', new_student_id),
        ('Buddenbroki', new_student_id),
        ('Dr.Faust', new_student_id)
    ]
)

cursor.execute("SELECT id FROM books order by id DESC LIMIT 3")
book_1, book_2, book_3 = cursor.fetchmany(3)
book_1_id = book_1['id']
book_2_id = book_2['id']
book_3_id = book_3['id']

query_group = "INSERT INTO `groups` (title, start_date, end_date) values (%s, %s, %s)"
cursor.execute(query_group, ('Monty Python', 'jan 25', 'jan 26'))
new_group_id = cursor.lastrowid

query_update_group = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query_update_group, (new_group_id, new_student_id))

query_subject = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    query_subject, [
        ('Culture',),
        ('Geography',),
        ('Medicine',)
    ]
)

cursor.execute("SELECT id FROM subjets order by id DESC LIMIT 3")
medicine, geography, culture = cursor.fetchmany(3)
medicine_id = medicine['id']
geography_id = geography['id']
culture_id = culture['id']

query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(query_lessons, [
        ('Impressionism', culture_id),
        ('Modernism', culture_id),
        ('France', geography_id),
        ('Spain', geography_id),
        ('Surgery', medicine_id),
        ('Pediatric', medicine_id)
    ]
)

cursor.execute("SELECT id FROM lessons order by id DESC LIMIT 6")
pediatric, surgery, spain, france, modernism, impressionism = cursor.fetchmany(6)
pediatric_id = pediatric['id']
surgery_id = surgery['id']
spain_id = spain['id']
france_id = france['id']
modernism_id = modernism['id']
impressionism_id = impressionism['id']


query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query_marks, [
        (5, impressionism_id, new_student_id),
        (3, modernism_id, new_student_id),
        (2, france_id, new_student_id),
        (5, spain_id, new_student_id),
        (5, surgery_id, new_student_id),
        (5, pediatric_id, new_student_id)
    ]
)

marks_query = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(marks_query, (new_student_id,))

marks_student = cursor.fetchall()

marks_query = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(marks_query, (new_student_id,))
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

cursor.execute(query_all_info_about_student, (new_student_id,))
all_info_about_student = cursor.fetchall()

db.commit()

print(all_info_about_student)

db.close()
