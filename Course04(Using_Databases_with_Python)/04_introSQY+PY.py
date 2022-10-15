import sqlite3

conn = sqlite3.connect('emailDB.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (emails TEXT, Count INTEGER)''')

fname = input('Enter the file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE emails=? ',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (emails, count) VALUES (?, 1) ''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE emails=?', (email,))
    
    conn.commit()
    
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT emails, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()