import sqlite3


def add_teacher_data(n, user, pas, add, mail, phone):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS teachers(
        name text,
        user text,
        password text,
        address text,
        email text,
        phone_number text 
    )
    """)
    c.execute("INSERT INTO teachers VALUES (?, ?, ?, ?, ?, ?)", (n, user, pas, add, mail, phone))
    c.execute("SELECT rowid, * FROM teachers")
    teacher_data = c.fetchall()
    conn.commit()
    conn.close()
    return teacher_data


def reade_teachers():
    conn1 = sqlite3.connect('teacher.db')
    cur = conn1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS teachers(
        name text,
        user text,
        password text,
        address text,
        email text,
        phone_number text 
    )
    """)
    cur.execute("SELECT rowid, * FROM teachers")
    data = cur.fetchall()
    list1 = [i[2] for i in data]
    list2 = data
    conn1.commit()
    conn1.close()
    all_list = (list1, list2)
    return all_list


def delete_row(name, table, id_no):
    con = sqlite3.connect(f'{name}.db')
    cu = con.cursor()
    cu.execute(f"DELETE from {table} WHERE rowid= {id_no}")
    con.commit()
    con.close()


def create_lists(db_name, table_name, column_name, **kwargs):
    conn = sqlite3.connect(f'{db_name}.db')
    c = conn.cursor()
    c.execute(f"SELECT {column_name} FROM {table_name}")
    names = [row[0] for row in c.fetchall()]
    for name in names:
        c.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY)")
        for col_name, col_type in kwargs.items():
            c.execute(f"ALTER TABLE {name} ADD COLUMN {col_name} {col_type}")
    conn.commit()
    conn.close()


def add_student_data(n, user, add, mail, phone):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students(
        name text,
        user text,
        address text,
        email text,
        phone_number text
    )
    """)
    c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (n, user, add, mail, phone))
    c.execute("SELECT rowid, * FROM students")
    teacher_data = c.fetchall()
    conn.commit()
    conn.close()
    return teacher_data


def reade_student():
    conn1 = sqlite3.connect('teacher.db')
    cur = conn1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
        name text,
        user text,
        address text,
        email text,
        phone_number text 
    )
    """)
    cur.execute("SELECT rowid, * FROM students")
    data = cur.fetchall()
    list1 = [i[2] for i in data]
    list2 = data
    conn1.commit()
    conn1.close()
    all_list = (list1, list2)
    return all_list


def user_email_data():
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students(
        name text,
        user text,
        address text,
        email text,
        phone_number text 
    )
    """)
    c.execute("SELECT rowid, * FROM students")
    data = c.fetchall()
    list1 = [i[2] for i in data]
    list2 = [i[4] for i in data]
    conn.commit()
    conn.close()
    dictionary = {key: val for (key, val) in zip(list1, list2)}
    return dictionary


def add_std_marks(t_name, f_sem=None, s_sem=None, t_sem=None, practical=None):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{t_name}_marks';")
    table_exists = c.fetchone()
    if not table_exists:
        c.execute(f"""CREATE TABLE {t_name}_marks(
            f_sem INTEGER,
            s_sem INTEGER,
            t_sem INTEGER,
            practical INTEGER
        )""")
        c.execute(f"INSERT INTO {t_name}_marks (f_sem, s_sem, t_sem, practical) VALUES (?, ?, ?, ?)",
                  (f_sem, s_sem, t_sem, practical))
    else:
        c.execute(f"SELECT * FROM {t_name}_marks")
        marks_data = c.fetchone()
        if f_sem is not None:
            marks_data = (f_sem, marks_data[1], marks_data[2], marks_data[3])
        if s_sem is not None:
            marks_data = (marks_data[0], s_sem, marks_data[2], marks_data[3])
        if t_sem is not None:
            marks_data = (marks_data[0], marks_data[1], t_sem, marks_data[3])
        if practical is not None:
            marks_data = (marks_data[0], marks_data[1], marks_data[2], practical)
        c.execute(f"UPDATE {t_name}_marks SET f_sem=?, s_sem=?, t_sem=?, practical=?",
                  marks_data)
    conn.commit()
    c.execute(f"SELECT f_sem, s_sem, t_sem, practical FROM {t_name}_marks")
    marks_data = c.fetchone()
    conn.close()
    return marks_data


def reade_user_marks(u_name):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {u_name}_marks")
    marks_data = c.fetchall()
    conn.commit()
    conn.close()
    return marks_data[0]


def add_fee_details(t_name, username=None, amount=None, status=None, phone=None, penalty=None):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{t_name}_info';")
    table_exists = c.fetchone()
    if not table_exists:
        c.execute(f"""CREATE TABLE {t_name}_info(
            username TEXT,
            amount INTEGER,
            status TEXT,
            phone TEXT,
            penalty INTEGER
        )""")
        c.execute(f"INSERT INTO {t_name}_info (username, amount, status, phone, penalty) VALUES (?, ?, ?, ?, ?)",
                  (username, amount, status, phone, penalty))
    else:
        c.execute(f"SELECT * FROM {t_name}_info")
        info_data = c.fetchone()
        if username is not None:
            info_data = (username, info_data[1], info_data[2], info_data[3], info_data[4])
        if amount is not None:
            info_data = (info_data[0], amount, info_data[2], info_data[3], info_data[4])
        if status is not None:
            info_data = (info_data[0], info_data[1], status, info_data[3], info_data[4])
        if phone is not None:
            info_data = (info_data[0], info_data[1], info_data[2], phone, info_data[4])
        if penalty is not None:
            info_data = (info_data[0], info_data[1], info_data[2], info_data[3], penalty)
        c.execute(f"UPDATE {t_name}_info SET username=?, amount=?, status=?, phone=?, penalty=?",
                  info_data)
    conn.commit()
    c.execute(f"SELECT username, amount, status, phone, penalty FROM {t_name}_info")
    info_data = c.fetchone()
    conn.close()
    return info_data


def reade_fee_details(u_name):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {u_name}_info")
    fee_data = c.fetchall()
    conn.commit()
    conn.close()
    return fee_data[0]


def add_subject_details(username=None, subject1=None, subject2=None, subject3=None, backlog=None):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{username}_subject';")
    table_exists = c.fetchone()
    if not table_exists:
        c.execute(f"""CREATE TABLE {username}_subject(
            username TEXT,
            subject1 TEXT,
            subject2 TEXT,
            subject3 TEXT,
            backlog TEXT
        )""")
        c.execute(f"INSERT INTO {username}_subject (username, subject1, subject2, subject3, backlog)"
                  f" VALUES (?, ?, ?, ?, ?)", (username, subject1, subject2, subject3, backlog))
    else:
        c.execute(f"SELECT * FROM {username}_subject")
        marks_data = c.fetchone()
        if username is not None:
            marks_data = (username, marks_data[1], marks_data[2], marks_data[3], marks_data[4])
        if subject1 is not None:
            marks_data = (marks_data[0], subject1, marks_data[2], marks_data[3], marks_data[4])
        if subject2 is not None:
            marks_data = (marks_data[0], marks_data[1], subject2, marks_data[3], marks_data[4])
        if subject3 is not None:
            marks_data = (marks_data[0], marks_data[1], marks_data[2], subject3, marks_data[4])
        if backlog is not None:
            marks_data = (marks_data[0], marks_data[1], marks_data[2], marks_data[3], backlog)
        c.execute(f"UPDATE {username}_subject SET username=?, subject1=?, subject2=?, subject3=?, backlog=?",
                  marks_data)
    conn.commit()
    c.execute(f"SELECT username, subject1, subject2, subject3, backlog FROM {username}_subject")
    marks_data = c.fetchone()
    conn.close()
    return marks_data


def reade_subject(username):
    conn = sqlite3.connect("teacher.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {username}_subject")
    subject_data = c.fetchall()
    conn.commit()
    conn.close()
    return subject_data[0]

