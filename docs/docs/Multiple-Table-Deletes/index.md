#### Menghapus Beberapa Tabel

Dalam bab ini, kita akan melihat ekspresi Multiple Table Deletes yang mirip dengan menggunakan fungsi Multiple Table Updates.

Lebih dari satu tabel dapat dirujuk dalam klausa WHERE dari pernyataan DELETE dalam banyak dialek DBMS. Untuk PG dan MySQL, sintaks "DELETE USING" digunakan; dan untuk SQL Server, menggunakan ekspresi "DELETE FROM" mengacu pada lebih dari satu tabel. Konstruksi SQLAlchemy delete() mendukung kedua mode ini secara implisit, dengan menentukan beberapa tabel dalam klausa WHERE sebagai berikut

```python
stmt = users.delete().\
   where(users.c.id == addresses.c.id).\
   where(addresses.c.email_address.startswith('xyz%'))
conn.execute(stmt)
```

>output error karena SQLite tidak mendukung multi-table DELETE

Pada backend PostgreSQL, SQL yang dihasilkan dari pernyataan di atas akan dirender sebagai 

```sql
DELETE FROM users USING addresses
WHERE users.id = addresses.id
AND (addresses.email_address LIKE %(email_address_1)s || '%%')
```

Jika metode ini digunakan dengan database yang tidak mendukung perilaku ini, kompiler akan memunculkan NotImplementedError.