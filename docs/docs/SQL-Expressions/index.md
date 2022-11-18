### SQL Expression

Ekspresi SQL dibangun menggunakan metode yang sesuai relatif terhadap objek tabel target. Misalnya, pernyataan INSERT dibuat dengan mengeksekusi metode insert() sebagai berikut

```python
ins = students.insert()
```

Hasil dari metode di atas adalah objek sisipan yang dapat diverifikasi dengan menggunakan fungsi str(). Kode di bawah ini menyisipkan detail seperti id siswa, nama, nama belakang.

```python
'INSERT INTO students (id, name, lastname) VALUES (:id, :name, :lastname)'
```

Dimungkinkan untuk memasukkan nilai dalam bidang tertentu dengan metode values() untuk memasukkan objek. Kode untuk hal yang sama diberikan di bawah ini

```python
>>> ins = users.insert().values(name = 'Karan')
>>> str(ins)
'INSERT INTO users (name) VALUES (:name)'
```

SQL yang bergema di konsol Python tidak menunjukkan nilai sebenarnya ('Karan' dalam kasus ini). Sebagai gantinya, SQLALchemy menghasilkan parameter bind yang terlihat dalam bentuk pernyataan yang dikompilasi.

```python
ins.compile().params
{'name': 'Karan'}
```

Demikian pula, metode seperti update(), delete() dan select() masing-masing membuat ekspresi UPDATE, DELETE dan SELECT. Kita akan belajar tentang mereka di bab-bab selanjutnya.