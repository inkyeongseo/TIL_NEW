import sqlite3
db = sqlite3.connect("Person.db")
cursor = db.cursor()
datas=[(1,"Dominica","14"),(2,"Ruri","13"),(3,"Ruo","9")]
cursor.execute("create table person (Id serial, Name text, age text)")
cursor.executemany("insert into person values(?,?,?)", datas)
cursor.execute("select * from person")
for row in cursor:
    print(row[1]+"의 나이는"+row[2]+"입니다.")
