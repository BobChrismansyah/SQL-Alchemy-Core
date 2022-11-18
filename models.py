from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
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
from sqlalchemy.sql import select
s = select([students])
result = conn.execute(s)

for row in result:
   print (row)