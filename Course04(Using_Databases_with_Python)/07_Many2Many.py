import sqlite3
import json

conn = sqlite3.connect('courseDB.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Roles;

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT 
);
CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT,
    email   TEXT
);
CREATE TABLE Member (
    user_id  INTEGER,
    course_id  INTEGER,
    role_id    INTEGER,
    PRIMARY KEY (user_id, course_id)
);
CREATE TABLE Roles (
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    role  TEXT UNIQUE )
''')

cur.executescript('''
            INSERT INTO Roles (id, role) VALUES (0, 'Student');
            INSERT INTO Roles (id, role) VALUES (1, 'Teacher')''')

fname = 'roster.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]
    
    cur.execute('SELECT role FROM Roles WHERE id = ? ', (role, ))
    role_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role_id) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role_id ) )

    conn.commit()

cur.close()
