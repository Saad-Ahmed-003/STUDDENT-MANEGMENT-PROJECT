from flask import Flask, render_template, request, flash, get_flashed_messages, session
from backend import *

app = Flask(__name__)

app.secret_key = "as+-d*fg+-ra*dg+as-dg"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    passe = []
    man = reade_teachers()
    for i in man[1]:
        passe.append(i[3])
    dictionary = {k: v for (k, v) in zip(man[0], passe)}
    message = None
    if request.method == "POST":
        u_id = request.form["username"]
        password = request.form["password"]
        if u_id == "admin" and password == "admin":
            return render_template("admin.html")
        elif u_id in dictionary:
            passcode = dictionary[u_id]
            if password == passcode:
                return render_template('student-manegment.html')
        else:
            if u_id != "admin" or password != "admin":
                message = "Wrong username or password!"
                flash(message)
    return render_template('index.html', message=message)


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/admin/add_teacher', methods=["GET", "POST"])
def add_teacher():
    if request.method == "POST":
        # get the teacher details from the form
        name = request.form["name"]
        user_name = request.form["username"]
        password = request.form["password"]
        address = request.form["address"]
        email = request.form["email"]
        phone_number = request.form["number"]
        data = reade_teachers()
        if user_name in data[0]:
            flash("user name already exists try something else")
            print(data)
        else:
            flash("continue")
            add_teacher_data(name, user_name, password, address, email, phone_number)
    return render_template('add-teacher.html')


# define the view teachers route

@app.route('/admin/view_teacher')
def view_teachers():
    data = reade_teachers()
    return render_template('view-teachers.html', teacher_data=data[1])


@app.route('/admin/view_teacher/<name>/<table>/<int:id_num>')
def delete_teacher(name, table, id_num):
    delete_row(name, table, id_num)
    data = reade_teachers()
    flash("user deleted successfully.")
    return render_template('view-teachers.html', teacher_data=data[1])


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________


@app.route('/student')
def student():
    return render_template('student-manegment.html')


@app.route('/student/add', methods=["GET", "POST"])
def add_students():
    if request.method == "POST":
        name = request.form['name']
        user = request.form['username']
        address = request.form['address']
        email = request.form['email']
        phone_number = request.form['number']
        print(name, user, address, email, phone_number)
        data = reade_student()
        if user in data[0]:
            flash('user name already exists try something else')
        else:
            add_student_data(name, user, address, email, phone_number)
            session['add_Username_Id'] = user
            flash('user added success fully.')
    return render_template('Add-student.html')


@app.route('/student/view')
def view_student():
    data = reade_student()
    return render_template('View-Students.html', student_data=data[1])


@app.route('/student/view/<name>/<table1>/<int:id_num>/<user>')
def delete_student(name, table1, id_num, user):
    delete_row(name, table=table1, id_no=id_num)
    flash(f'user {user} deleted success fully')
    print(user)
    session['delete_Username_Id'] = user
    data = reade_student()
    return render_template('View-Students.html', student_data=data[1])


@app.route('/student/marks', methods=['GET', 'POST'])
def add_marks():
    if request.method == 'POST':
        user_id = request.form['username']
        data = reade_student()
        if user_id in data[0]:
            first_sem = request.form['first_sem']
            second_sem = request.form['second_sem']
            third_sem = request.form['third_sem']
            practical = request.form['practical']
            print(first_sem, second_sem, third_sem, practical)
            show = add_std_marks(user_id, first_sem, second_sem, third_sem, practical)
            print(show)
        else:
            print('user dose not exist')
    return render_template('Marks.html')


@app.route('/student/login/view_marks', methods=['GET', 'POST'])
def login_view_marks():
    if request.method == 'POST':
        user_student = request.form['username']
        email = request.form['email']
        data = user_email_data()
        if user_student in data:
            user_email = data[user_student]
            if email == user_email:
                m_data = reade_user_marks(user_student)
                return render_template('Performence.html', marks_data=m_data)
        else:
            flash('user dose not exist')
    return render_template('view_login.html')


@app.route('/student/fee_details', methods=['GET', 'POST'])
def fee_details():
    if request.method == 'POST':
        user_id = request.form['username']
        data = reade_student()
        if user_id in data[0]:
            amount = request.form["amount"]
            status = request.form["status"]
            phone_ = request.form["phone_number"]
            penalty = request.form["Penalty"]
            add_fee_details(user_id, username=user_id, amount=amount, status=status, phone=phone_, penalty=penalty)
            print(user_id, amount, status, phone_, penalty)
            flash('added successfully.')
        else:
            flash('user dose not exist.')
    return render_template('Add-Fee-details.html')


@app.route('/student/login/view_fee_details', methods=['GET', 'POST'])
def view_fee_detail():
    if request.method == 'POST':
        user_student = request.form['username']
        email = request.form['email']
        data = user_email_data()
        if user_student in data:
            user_email = data[user_student]
            if email == user_email:
                m_data = reade_fee_details(user_student)
                return render_template('view-fee-detail.html', fee_data=m_data)
        else:
            flash('user dose not exist')
    return render_template('view_fee_login.html')


@app.route('/student/subject', methods=['GET', 'POST'])
def add_subject():
    if request.method == 'POST':
        user_id = request.form['username']
        data = reade_student()
        if user_id in data[0]:
            subject_1 = request.form['Subject-1']
            subject_2 = request.form['Subject-2']
            subject_3 = request.form['Subject-3']
            backlogs = request.form['Backlogs']
            p = add_subject_details(username=user_id, subject1=subject_1, subject2=subject_2, subject3=subject_3,
                                    backlog=backlogs)
            print(user_id, subject_1, subject_2, subject_3, backlogs, p)
            flash('added successfully.')
        else:
            flash('user dose not exist.')
    return render_template('Add-subjects.html')


@app.route('/student/login/view_subject', methods=['GET', 'POST'])
def view_subject():
    if request.method == 'POST':
        user_student = request.form['username']
        email = request.form['email']
        data = user_email_data()
        if user_student in data:
            user_email = data[user_student]
            if email == user_email:
                m_data = reade_subject(user_student)
                print(m_data)
                return render_template("View-subjects.html", fee_data=m_data)
        else:
            flash('user dose not exist')
    return render_template("view_subject_login.html")


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
