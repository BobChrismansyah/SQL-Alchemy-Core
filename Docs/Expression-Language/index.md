### Expression Language

Inti SQLAlchemy mencakup mesin rendering SQL, integrasi DBAPI, integrasi transaksi , dan layanan deskripsi skema . Inti SQLAlchemy menggunakan SQL Expression Language yang menyediakan paradigma penggunaan yang berpusat pada skema sedangkan SQLAlchemy ORM adalah mode penggunaan yang berpusat pada domain .

Bahasa Ekspresi SQL menyajikan sistem yang merepresentasikan struktur dan ekspresi basis data relasional menggunakan konstruksi Python. Ini menyajikan sistem yang mewakili konstruksi primitif dari basis data relasional secara langsung tanpa pendapat, yang berbeda dengan ORM yang menyajikan pola penggunaan tingkat tinggi dan abstrak, yang dengan sendirinya merupakan contoh penggunaan terapan dari Bahasa Ekspresi.

Bahasa Ekspresi adalah salah satu komponen inti dari SQLAlchemy. Ini memungkinkan pemrogram untuk menentukan pernyataan SQL dalam kode Python dan menggunakannya secara langsung dalam kueri yang lebih kompleks. Bahasa ekspresi tidak bergantung pada backend dan secara komprehensif mencakup setiap aspek SQL mentah. Ini lebih dekat ke SQL mentah daripada komponen lain di SQLAlchemy.

Bahasa Ekspresi mewakili konstruksi primitif dari basis data relasional secara langsung. Karena ORM didasarkan pada bahasa Expression, aplikasi database Python yang khas mungkin memiliki penggunaan keduanya yang tumpang tindih. Aplikasi dapat menggunakan bahasa ekspresi saja, meskipun harus menentukan sistemnya sendiri untuk menerjemahkan konsep aplikasi ke dalam kueri basis data individual.

Pernyataan bahasa Ekspresi akan diterjemahkan ke dalam kueri SQL mentah yang sesuai oleh mesin SQLAlchemy. Sekarang kita akan mempelajari cara membuat mesin dan menjalankan berbagai kueri SQL dengan bantuannya.