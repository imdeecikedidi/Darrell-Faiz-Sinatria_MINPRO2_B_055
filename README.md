<div align="center">

# 🎬 XX1 Cinema Management System 🎬

**Program Manajemen Data Film Bioskop Berbasis Terminal (CLI)**

</div>

---

## 👤 Biodata Mahasiswa

| Keterangan | Data Mahasiswa |
| :--- | :--- |
| **Nama Lengkap** | Darrell Faiz Sinatria |
| **NIM** | 2609116055 |
| **Kelas** | B |
| **Mata Kuliah** | Dasar-Dasar Pemrograman (DDP) |
| **Tugas** | Mini Project 2 |

---

# Penjelasan Kode XX1 Cinema

## 1. Import Library

``` python
import datetime
import random
import os
```

Penjelasan:

Kode ini digunakan untuk memanggil library yang diperlukan.

-   `datetime` digunakan untuk mengambil tanggal dan waktu ketika
    pengguna berhasil login.
-   `random` digunakan untuk membuat angka acak ketika film berhasil
    ditambahkan.
-   `os` digunakan untuk menjalankan perintah sistem operasi, pada
    program ini digunakan untuk membersihkan terminal.

------------------------------------------------------------------------

## 2. Data Akun

``` python
akun = {
    "admin": ["admin123", "admin"],
    "user": ["user123", "user"]
}
```

Penjelasan:

Kode ini membuat dictionary yang menyimpan data akun pengguna.

Setiap akun memiliki: - Username sebagai key. - Password dan role
sebagai value.

Contohnya akun admin memiliki password `admin123` dan role `admin`.

Role digunakan untuk menentukan menu yang dapat diakses pengguna.

------------------------------------------------------------------------

## 3. Data Film

``` python
film = [
    ["The Batman", "Action", 40000],
    ["Spirited Away", "Animation", 40000],
    ["Jujutsu Kaisen", "Fantasy", 40000]
]
```

Penjelasan:

Kode ini menyimpan daftar film menggunakan list dua dimensi.

Setiap data film terdiri dari: - Nama film. - Kategori film. - Harga
tiket.

Data ini nantinya dapat ditampilkan, ditambah, diubah, dan dihapus.

------------------------------------------------------------------------

## 4. Fungsi Membersihkan Terminal

``` python
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")
```

Penjelasan:

Fungsi `bersihkan()` digunakan untuk membersihkan layar terminal.

Program mengecek sistem operasi: - Jika Windows menggunakan perintah
`cls`. - Jika Linux/Mac menggunakan perintah `clear`.

Fungsi ini dipanggil sebelum menampilkan menu agar tampilan lebih rapi.

------------------------------------------------------------------------

## 5. Fungsi Login

``` python
def login():
    print("@@@ LOGIN XX1 CINEMA @@@")

    for i in range(3):
        user = input("Username: ")

        if user == "":
            print("Program ditutup")
            return "keluar"

        pw = input("Password: ")

        if user in akun and pw == akun[user][0]:
            print("Login berhasil")
            print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
            return akun[user][1]

        print("Login salah")

    return None
```

Penjelasan:

Fungsi `login()` digunakan untuk melakukan proses masuk ke program.

Bagian:

``` python
for i in range(3):
```

memberikan kesempatan login sebanyak tiga kali.

Bagian:

``` python
user = input("Username: ")
```

digunakan untuk menerima input username.

Bagian:

``` python
if user == "":
```

digunakan untuk mengecek apakah username kosong. Jika kosong program
akan berhenti.

Bagian:

``` python
if user in akun and pw == akun[user][0]:
```

digunakan untuk mencocokkan username dan password dengan data akun.

Jika benar, program mengembalikan role pengguna.

------------------------------------------------------------------------

## 6. Fungsi Melihat Film

``` python
def lihat():
    print("@@@ DAFTAR FILM @@@")

    for i, f in enumerate(film, 1):
        print(f"{i}. {f[0]} | {f[1]} | Rp{f[2]}")
```

Penjelasan:

Fungsi `lihat()` digunakan untuk menampilkan seluruh daftar film.

Bagian:

``` python
enumerate(film, 1)
```

memberikan nomor urut pada setiap data film.

Bagian:

``` python
f[0], f[1], f[2]
```

digunakan untuk mengambil: - Judul film. - Kategori. - Harga.

------------------------------------------------------------------------

## 7. Fungsi Tambah Film

``` python
def tambah():
    try:
        data = [
            input("Nama film: "),
            input("Kategori: "),
            int(input("Harga: "))
        ]

        film.append(data)

        print("Film berhasil ditambah")
        print("Kode:", random.randint(1000, 9999))

    except:
        print("Input harga harus angka")
```

Penjelasan:

Fungsi `tambah()` digunakan admin untuk menambahkan film baru.

Bagian:

``` python
try
```

digunakan untuk menangkap kesalahan input.

Bagian:

``` python
film.append(data)
```

menambahkan data film baru ke dalam list.

Bagian:

``` python
random.randint(1000,9999)
```

membuat kode angka acak.

------------------------------------------------------------------------

## 8. Fungsi Mengubah Film

``` python
def ubah():
    lihat()

    try:
        no = int(input("Nomor film: "))

        if 0 < no <= len(film):
            film[no-1] = [
                input("Nama baru: "),
                input("Kategori baru: "),
                int(input("Harga baru: "))
            ]

            print("Film berhasil diubah")
```

Penjelasan:

Fungsi `ubah()` digunakan untuk mengganti data film.

Pertama program menampilkan daftar film menggunakan fungsi `lihat()`.

Kemudian pengguna memilih nomor film.

Bagian:

``` python
film[no-1]
```

digunakan karena index list dimulai dari angka 0.

------------------------------------------------------------------------

## 9. Fungsi Menghapus Film

``` python
def hapus():
    lihat()

    try:
        no = int(input("Nomor film: "))

        if 0 < no <= len(film):
            film.pop(no-1)
            print("Film berhasil dihapus")
```

Penjelasan:

Fungsi `hapus()` digunakan untuk menghapus data film.

Bagian:

``` python
film.pop(no-1)
```

menghapus data berdasarkan posisi index pada list.

------------------------------------------------------------------------

## 10. Fungsi Menu

``` python
def menu(role):

    while True:
        bersihkan()

        print("@@@ MENU XX1 CINEMA @@@")
```

Penjelasan:

Fungsi `menu()` mengatur tampilan utama setelah pengguna berhasil login.

Parameter:

``` python
role
```

digunakan untuk mengetahui apakah pengguna adalah admin atau user.

Perulangan:

``` python
while True
```

membuat menu terus berjalan sampai pengguna memilih logout.

------------------------------------------------------------------------

## 11. Menu Admin

``` python
if role == "admin":
    print("2. Tambah Film")
    print("3. Ubah Film")
    print("4. Hapus Film")
```

Penjelasan:

Jika pengguna memiliki role admin, maka menu tambahan akan muncul.

Admin dapat melakukan operasi CRUD terhadap data film.

------------------------------------------------------------------------

## 12. Program Utama

``` python
while True:

    role = login()

    if role == "keluar":
        break

    elif role:
        menu(role)

    else:
        print("Login gagal")
        break
```

Penjelasan:

Bagian ini merupakan program utama.

Alur program:

1.  Program menjalankan login.
2.  Login mengembalikan role pengguna.
3.  Jika role admin/user, masuk ke menu.
4.  Jika memilih keluar, program berhenti.
5.  Jika login gagal, program selesai.
