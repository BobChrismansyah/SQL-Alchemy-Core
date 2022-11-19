from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import and_
from sqlalchemy.sql import select

engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
conn = engine.connect()

ins = students.insert()
# ins = students.insert().values(name = 'Bob', lastname = 'Chrismansayah')
# ins = students.insert().values(name = 'Ariandini', lastname = 'Aulia')
# ins = students.insert().values(name = 'Haidir', lastname = 'Haidir')
# insert data dieksekusi hanya satu per satu, tidak bisa 3 sekaligus



# conn.execute(students.insert(), [
#    {'name':'Bob', 'lastname' : 'Langau'},
#    {'name':'Aiandini','lastname' : 'Dini'},
#    {'name':'Haidir','lastname' : 'Ahmed'},
#    {'name':'Masuk','lastname' : 'Saja'},
# ])
   
# result = conn.execute(ins)


# ///Select-Rows///
# s = students.select()
# conn = engine.connect()
# result = conn.execute(s)

# for row in result:
#    print (row)

# ///Select-Rows menggunakan modul sqlachemy.sql///
# from sqlalchemy.sql import select
# s = select([students])
# result = conn.execute(s)

# for row in result:
#    print (row)


# ========== Menggunakan text() ==========
# from sqlalchemy import text
# t = text("SELECT * FROM students")
# result = conn.execute(t)
# for row in result:
#    print (row)
# ========== Menggunakan text() ==========


# ========== Select Menggunakan parameter terikat ==========
# from sqlalchemy.sql import text
# s = text("select students.name, students.lastname from students where students.name between :x and :y")
# result = conn.execute(s, x = 'A', y = 'L').fetchall()

# for row in result:
#    print (row)
# ========== Select Menggunakan parameter terikat ==========


# ========== Select Menggunakan bindparams ==========
# from sqlalchemy.sql import select
# from sqlalchemy import bindparam
# stmt = text("SELECT * FROM students WHERE students.name BETWEEN :x AND :y")

# stmt = stmt.bindparams(
#    bindparam("x", type_= String), 
#    bindparam("y", type_= String)
# )

# result = conn.execute(stmt, {"x": "A", "y": "L"})
 
# for row in result:
#    print (row)

# ========== Select Menggunakan bindparams ==========


# ================ Menggunakan Alias =================


# ========== alias ==========
from sqlalchemy.sql import alias, select
st = students.alias("a")
s = select([st]).where(st.c.id > 2)
result = conn.execute(s).fetchall()

for row in result:
   print (row)