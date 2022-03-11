import sqlite3 #importing sqlite3

conn = sqlite3.connect('dbassignment.db') #shorting the code for connecting sqlite3 to my database by assigning it to a variable named "conn"

with conn:
    cur = conn.cursor()  #using the cursor method to gain access into the database and execute commands
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_project(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        Files TEXT)")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('dbassignment.db')

with conn: #iterating through tuple for specific extension to insert into database
     cur = conn.cursor()
     for file in fileList:
            if file.endswith('.txt'):
                cur.execute("INSERT INTO tbl_project(Files) VALUES (?)",(file,))
                conn.commit()
conn.close()

for file in fileList:
    if file.endswith('.txt'):
        print(file)



