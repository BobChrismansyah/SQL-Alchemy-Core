from sqlalchemy import and_
from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

conn = engine.connect()
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)

addresses = Table(
   'addresses', meta, 
   Column('id', Integer, primary_key = True), 
   Column('st_id', Integer), 
   Column('postal_add', String), 
   Column('email_add', String)
)

#ins = students.insert()
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
# from sqlalchemy.sql import alias, select
# st = students.alias("a")
# s = select([st]).where(st.c.id > 2)
# result = conn.execute(s).fetchall()

# for row in result:
#    print (row)
# ========== alias ==========

# ========== Update ==========
# conn = engine.connect()
# stmt=students.update().where(students.c.lastname=='Saja').values(lastname='Sajami')
# conn.execute(stmt)
# s = students.select()
# result = conn.execute(s).fetchall()

# for row in result:
#    print (row)
# ========== Update ==========

# ========== Update mengggunakan modul sqlalchemy.sql.expression ==========   
# from sqlalchemy.sql.expression import update
# stmt = update(students).where(students.c.lastname == 'Sajami').values(lastname = 'Lagi')

# conn.execute(stmt)
# s = students.select()
# result = conn.execute(s)

# for row in result:
#    print (row)
# ========== Update mengggunakan modul sqlalchemy.sql.expression  ==========


# ========== Delete ==========
# from sqlalchemy.sql.expression import update
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# engine = create_engine('sqlite:///college.db', echo = True)

# meta = MetaData()

# students = Table(
#    'students', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('name', String), 
#    Column('lastname', String), 
# )

# conn = engine.connect()
# stmt = students.delete().where(students.c.lastname == 'Lagi')
# conn.execute(stmt)
# s = students.select()
# result = conn.execute(s).fetchall()

# for row in result:
#    print (row)
# ========== Delete ==========

# ========== Memuat dua tabel ==========
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
# engine = create_engine('sqlite:///college.db', echo=True)
# meta = MetaData()

# students = Table(
#    'students', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('name', String), 
#    Column('lastname', String), 
# )

# addresses = Table(
#    'addresses', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('st_id', Integer, ForeignKey('students.id')), 
#    Column('postal_add', String), 
#    Column('email_add', String))

# meta.create_all(engine)
# ========== Memuat dua tabel ==========


# ========== Menambahkan isi kedalam tabel ==========



# ========== Menambahkan isi kedalam tabel ==========
# result = conn.execute(students.insert(), [
#    {'name':'Bob', 'lastname':'Chrismansyah'},
#    {'name':'Ariandini', 'lastname' : 'Aulia'},
#    {'name':'Ahmad','lastname' : 'Haidir'},
# ])
# ========== Menambahkan isi kedalam tabel students ==========

# ========== Menambahkan isi kedalam tabel addresses==========
# addresses = Table(
#    'addresses', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('st_id', Integer), 
#    Column('postal_add', String), 
#    Column('email_add', String)
# )
# conn.execute(addresses.insert(), [
#    {'st_id':1, 'postal_add':'Pk 4', 'email_add':'bob@ilkom.my.id'},
#    {'st_id':1, 'postal_add':'PK 5', 'email_add':'ariandini@gmail.com'},
#    {'st_id':3, 'postal_add':'Pk 6', 'email_add':'haidir757@gmail.com'},
# ])
# ========== Menambahkan isi kedalam tabel addresses ==========

# ========== mengambil data dari kedua tabel ==========
# from sqlalchemy.sql import select
# s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
# result = conn.execute(s)

# for row in result:
#    print (row)
# ========== mengambil data dari kedua tabel ==========

# ========== Update beberapa tabel ==========
# stmt = students.update().\
# values({
#    students.c.name:'Ariandini',
#    addresses.c.email_add:'dini.cantik@proton.me'
# }).\
# where(students.c.id == addresses.c.id)
#Namun di SQLite tidak mendukung multi-table UPDATE 

# stmt = students.update().\
#    values(name = 'Bob').\
#    where(students.c.id == addresses.c.id)
# ========== Update beberapa tabel ==========

# ========== Update Parameter Berurutan ==========

# stmt = students.update(preserve_parameter_order = True).\
#    values([(students.c.y, 20), (students.c.x, students.c.y + 10)])
# ========== Update Parameter Berurutan ==========


# ========== Hapus Beberapa Tabel ==========
# stmt = students.delete().\
#    where(students .c.id == addresses.c.id).\
#    where(addresses.c.email_add.startswith('gmail'))
# conn.execute(stmt)

#output error karena SQLite tidak mendukung multi-table DELETE
# ========== Hapus Beberapa Tabel ==========

# ========== Menggunakan Join ==========
# from sqlalchemy import join
# from sqlalchemy.sql import select
# j = students.join(addresses, students.c.id == addresses.c.st_id)
# stmt = select([students]).select_from(j)
# result = conn.execute(stmt)

# for row in result:
#    print (row)
       
# ========== Menggunakan Join ==========