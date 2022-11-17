### Menghubungkan ke database

Pada materi sebelumnya, kita telah membahas tentang bahasa ekspresi di SQLAlchemy. Sekarang mari kita lanjutkan ke langkah-langkah yang dibutuhkan dalam menghubungkan ke database.

Kelas mesin menghubungkan Pool dan Dialect bersama -sama untuk menyediakan sumber konektivitas dan perilaku database. Objek kelas Engine dibuat instance-nya menggunakan fungsi create_engine().

Fungsi create_engine() mengambil database sebagai satu argumen. Basis data tidak perlu didefinisikan di mana pun. Formulir pemanggilan standar harus mengirim URL sebagai argumen posisi pertama, biasanya berupa string yang menunjukkan dialek database dan argumen koneksi. Menggunakan kode yang diberikan di bawah ini, kita dapat membuat database.

```sql
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///college.db', echo = True)
```

Untuk database MySQL , gunakan perintah di bawah ini

```sql
engine = create_engine("mysql://user:pwd@localhost/college",echo = True)
```

Untuk secara khusus menyebutkan DB-API yang akan digunakan untuk koneksi, string URL berbentuk sebagai berikut

```sql
dialect[+driver]://user:password@host/dbname
```

Misalnya, jika Anda menggunakan driver PyMySQL dengan MySQL , gunakan perintah berikut

```sql
mysql+pymysql://<username>:<password>@<host>/<dbname>
```

Echo Flasgs adalah shortcut untuk menyiapkan logging SQLAlchemy, yang dilakukan melalui modul logging standar Python. Pada bab selanjutnya, kita akan mempelajari semua SQL yang dihasilkan. Untuk menyembunyikan output verbose, setel atribut echo ke None. Argumen lain untuk fungsi create_engine() mungkin khusus untuk dialek.

| No  | Metode & Deskripsi  |
|---|---|
| 1  | **connect()** <br> Return koneksi object  |
| 2  | **execute()** <br> Mengeksekusi konstruksi pernyataan SQL |
| 3  | **begin()** <br> Mengembalikan konteks manager yang mengirimkan koneksi dengan transaksi yang dibuat  |
| 4  | **dispose()** <br> Membuang kumpulan koneksi yang digunakan oleh Engine |
| 5 | **driver()** <br> Nama driver yang digunakan oleh Engine |
| 6 | **table_name()** <br> Mengembalikan daftar semua nama tabel yang tersedia di database |
| 7 | **transaction()** <br> Mengeksekusi fungsi yang diberikan dalam batas transaksi|