# 🎬 XX1 Cinema - Minpro 2

## 👨‍🎓 Biodata Mahasiswa

  Keterangan           Data
  -------------------- -----------------------
  Nama                 Darrell Faiz Sinatria
  NIM                  2609116055
  Kelas                B
  Project              Minpro 2
  Bahasa Pemrograman   Python

## 📌 Deskripsi Program

XX1 Cinema merupakan program sederhana berbasis Python yang menerapkan
sistem login dan pengelolaan data film.

Fitur: - Login admin dan user - Melihat daftar film - Menambah film -
Mengubah film - Menghapus film - Logout

## 📷 Dokumentasi Screenshot

Tambahkan hasil screenshot terminal pada folder:

    screenshot/
    ├── login.png
    ├── menu.png
    ├── lihatfilm.png
    ├── tambahfilm.png
    └── hapusfilm.png

Kemudian tampilkan:

``` md
![Login](screenshot/login.png)
![Menu](screenshot/menu.png)
![Daftar Film](screenshot/lihatfilm.png)
![Tambah Film](screenshot/tambahfilm.png)
![Hapus Film](screenshot/hapusfilm.png)
```

# 📝 Penjelasan Kode

## Import Library

``` python
import datetime
import random
import os
```

-   datetime digunakan untuk menampilkan waktu login.
-   random digunakan membuat kode angka acak.
-   os digunakan membersihkan terminal.

## Data Akun

``` python
akun = {
    "admin": ["admin123", "admin"],
    "user": ["user123", "user"]
}
```

Menyimpan username, password, dan role pengguna.

Admin memiliki hak akses CRUD, sedangkan user hanya dapat melihat film.

## Data Film

``` python
film = [
    ["The Batman", "Action", 40000],
    ["Spirited Away", "Animation", 40000],
    ["Jujutsu Kaisen", "Fantasy", 40000]
]
```

Menyimpan data nama film, kategori, dan harga.

## Fungsi Login

Fungsi login digunakan untuk mengecek username dan password pengguna.

Jika data benar, sistem mengembalikan role pengguna.

## Fungsi Lihat Film

Menampilkan seluruh daftar film menggunakan perulangan.

## Fungsi Tambah Film

Digunakan admin untuk memasukkan data film baru menggunakan:

``` python
film.append(data)
```

## Fungsi Ubah Film

Mengganti data film berdasarkan nomor pilihan pengguna.

## Fungsi Hapus Film

Menghapus data film menggunakan:

``` python
film.pop(no-1)
```

## Fungsi Menu

Menampilkan menu berdasarkan hak akses admin atau user.

## Program Utama

Program berjalan menggunakan perulangan:

``` python
while True:
```

Kemudian menjalankan login dan menu sesuai role pengguna.

# Kesimpulan

XX1 Cinema merupakan project Minpro 2 menggunakan Python dengan konsep
dictionary, list, function, looping, percabangan, dan exception
handling.
