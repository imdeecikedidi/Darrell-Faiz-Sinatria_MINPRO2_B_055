# XX1 CINEMA - Sistem Manajemen Film Berbasis Python

## Biodata Pengembang

**Nama:** Darrell Faiz Sinatria  
**NIM:** 2609116055  
**Kelas:** B  
**Mata Kuliah:** Minpro 2  

---

# Deskripsi Program

XX1 Cinema merupakan program berbasis Python yang digunakan untuk mengelola data film sederhana menggunakan sistem login dan hak akses pengguna.

Program ini memiliki dua jenis pengguna, yaitu:

- **Admin**: memiliki akses penuh untuk melihat, menambah, mengubah, dan menghapus data film.
- **User**: hanya dapat melihat daftar film yang tersedia.

Program menerapkan konsep dasar pemrograman Python seperti:
- Variabel dan tipe data
- List dan dictionary
- Function
- Percabangan
- Perulangan
- Exception handling
- Import module
- Sistem login sederhana
- CRUD (Create, Read, Update, Delete)

---

# Fitur Program

## 1. Sistem Login

Program memiliki sistem autentikasi dengan dua akun:

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Admin |
| user | user123 | User |

Pengguna diberikan maksimal 3 kali percobaan login.

Jika username dikosongkan, program akan langsung berhenti.

---

## 2. Melihat Daftar Film

Semua pengguna dapat melihat daftar film yang tersedia.

Data film terdiri dari:

- Nama film
- Kategori film
- Harga tiket

Contoh data awal:

```
1. The Batman | Action | Rp40000
2. Spirited Away | Animation | Rp40000
3. Jujutsu Kaisen | Fantasy | Rp40000
```

---

## 3. Tambah Film (Admin)

Fitur ini hanya dapat digunakan oleh admin.

Admin dapat memasukkan:

- Nama film baru
- Kategori film
- Harga film

Setelah berhasil menambah film, program akan memberikan kode random sebagai tanda transaksi.

---

## 4. Ubah Data Film (Admin)

Admin dapat melakukan perubahan data film yang sudah tersedia.

Data yang dapat diubah:

- Nama film
- Kategori
- Harga tiket

Admin memilih nomor film kemudian memasukkan data baru.

---

## 5. Hapus Film (Admin)

Admin dapat menghapus film berdasarkan nomor urutan film.

Jika nomor film sesuai, data film akan dihapus dari daftar.

---

## 6. Logout

Pengguna dapat keluar dari menu utama dengan memilih menu logout.

Setelah logout, program akan kembali ke halaman login.

---

# Struktur Program

```
XX1 CINEMA

|
|-- akun
|-- film
|
|-- bersihkan()
|
|-- login()
|
|-- lihat()
|
|-- tambah()
|
|-- ubah()
|
|-- hapus()
|
|-- menu()
|
|-- Program Utama
```

---

# Penjelasan Kode

## 1. Import Library

```python
import datetime
import random
import os
```

Library yang digunakan:

- `datetime`  
  Digunakan untuk mengambil waktu login pengguna.

- `random`  
  Digunakan untuk membuat kode acak ketika film berhasil ditambahkan.

- `os`  
  Digunakan untuk membersihkan tampilan terminal.

---

# 2. Data Akun

```python
akun = {
    "admin": ["admin123", "admin"],
    "user": ["user123", "user"]
}
```

Bagian ini menyimpan data username, password, dan role pengguna.

Admin memiliki hak akses lebih banyak dibanding user.

---

# 3. Data Film

```python
film = [
    ["The Batman", "Action", 40000],
    ["Spirited Away", "Animation", 40000],
    ["Jujutsu Kaisen", "Fantasy", 40000]
]
```

Data film disimpan menggunakan list.

Setiap data film memiliki tiga bagian:

1. Nama film
2. Kategori film
3. Harga tiket

---

# 4. Fungsi Bersihkan Terminal

```python
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")
```

Fungsi ini digunakan untuk membersihkan layar terminal agar tampilan menu lebih rapi.

Jika menggunakan Windows menggunakan:

```
cls
```

Jika menggunakan Linux/Mac menggunakan:

```
clear
```

---

# 5. Fungsi Login

```python
def login():
```

Fungsi login bertugas melakukan pengecekan:

- Username
- Password
- Role pengguna

Jika data benar maka pengguna dapat masuk ke sistem.

Jika salah sebanyak 3 kali maka login gagal.

---

# 6. Fungsi Lihat Film

```python
def lihat():
```

Fungsi ini digunakan untuk menampilkan seluruh daftar film.

Perulangan:

```python
for i, f in enumerate(film, 1):
```

digunakan untuk memberikan nomor urut pada setiap film.

---

# 7. Fungsi Tambah Film

```python
def tambah():
```

Fungsi ini digunakan admin untuk menambahkan film baru.

Program menggunakan:

```python
film.append(data)
```

untuk memasukkan data baru ke dalam list film.

---

# 8. Fungsi Ubah Film

```python
def ubah():
```

Fungsi ini digunakan untuk mengganti data film yang sudah ada.

Pengguna memilih nomor film kemudian memasukkan data baru.

---

# 9. Fungsi Hapus Film

```python
def hapus():
```

Fungsi ini menghapus data film menggunakan:

```python
film.pop(no-1)
```

Method `pop()` digunakan untuk menghapus data berdasarkan posisi index.

---

# 10. Fungsi Menu

```python
def menu(role):
```

Fungsi menu mengatur tampilan berdasarkan hak akses.

Jika role:

### Admin

Mendapatkan menu:

```
1. Lihat Film
2. Tambah Film
3. Ubah Film
4. Hapus Film
5. Logout
```

### User

Hanya mendapatkan:

```
1. Lihat Film
5. Logout
```

---

# 11. Program Utama

```python
while True:
```

Program utama menggunakan perulangan agar sistem dapat berjalan terus sampai pengguna logout atau keluar.

Alurnya:

```
Mulai
 |
Login
 |
Validasi akun
 |
Masuk menu sesuai role
 |
Melakukan aktivitas
 |
Logout/Keluar
 |
Selesai
```

---

# Cara Menjalankan Program

1. Pastikan Python sudah terinstall.

Cek versi Python:

```
python --version
```

2. Simpan file dengan nama:

```
xx1_cinema.py
```

3. Jalankan melalui terminal:

```
python xx1_cinema.py
```

---

# Kesimpulan

Program XX1 Cinema merupakan implementasi sistem pengelolaan film sederhana menggunakan Python.

Program ini menerapkan konsep login dengan role berbeda serta operasi CRUD untuk mengelola data film.

Melalui program ini, pengguna dapat memahami penggunaan function, list, dictionary, percabangan, perulangan, dan pengolahan data sederhana dalam Python.
