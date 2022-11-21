#### Environment setup

Setiap versi Python yang lebih tinggi dari 2.7 diperlukan untuk menginstal SQLAlchemy. Cara termudah untuk menginstal adalah dengan menggunakan Python Package Manager, pip . Utilitas ini dibundel dengan distribusi standar Python.

```text
pip install sqlalchemy
```

Dalam kasus distribusi anaconda dari Python, SQLAlchemy dapat diinstal dari terminal conda menggunakan perintah di bawah ini

```text
conda install -c anaconda sqlalchemy
```

Dimungkinkan juga untuk menginstal SQLAlchemy dari kode sumber di bawah ini\

```text
python setup.py install
```

Cek version SQLAlchemy

```text
>> import sqlalchemy
>> sqlalchemy.__version__
```