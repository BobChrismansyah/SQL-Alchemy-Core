#### Update Parameter Berurutan


Kueri UPDATE dari SQL mentah memiliki klausa SET. Ini dirender oleh konstruksi update() menggunakan pengurutan kolom yang diberikan dalam objek Tabel asal. Oleh karena itu, pernyataan UPDATE tertentu dengan kolom tertentu akan dirender sama setiap saat. Karena parameter itu sendiri diteruskan ke metode Update.values() sebagai kunci kamus Python, tidak ada pengurutan tetap lain yang tersedia.

Dalam beberapa kasus, urutan parameter yang diberikan dalam klausa SET signifikan. Di MySQL, menyediakan pembaruan untuk nilai kolom didasarkan pada nilai kolom lainnya.

Berikut hasil pernyataan

```sql
UPDATE table1 SET x = y + 10, y = 20
```

akan memiliki hasil yang berbeda dari

```sql
UPDATE table1 SET y = 20, x = y + 10
```

Klausa SET di MySQL dievaluasi berdasarkan per nilai dan bukan berdasarkan per baris. Untuk tujuan ini, preserved_parameter_order digunakan. Daftar 2-tupel Python diberikan sebagai argumen untuk metode **Update.values()**

```python
stmt = table1.update(preserve_parameter_order = True).\
   values([(table1.c.y, 20), (table1.c.x, table1.c.y + 10)])
```

Objek Daftar mirip dengan kamus kecuali yang dipesan. Ini memastikan bahwa klausa SET kolom "y" akan dirender terlebih dahulu, kemudian klausa SET kolom "x".