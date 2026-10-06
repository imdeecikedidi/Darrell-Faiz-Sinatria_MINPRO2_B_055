# Mini Project 2 - Dasar-Dasar Pemrograman (DDP)

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

## 📌 Deskripsi Program

Program ini merupakan aplikasi berbasis Command Line Interface (CLI) yang mengimplementasikan sistem manajemen bioskop sederhana (**XX1 Cinema**). Sistem ini menerapkan konsep dasar pemrograman Python meliputi:
- **Autentikasi Multi-Role** (Admin & User biasa) dengan proteksi batas percobaan dan timestamp waktu login.
- **Operasi CRUD (Create, Read, Update, Delete)** data film.
- **Role-Based Access Control (RBAC)** untuk membatasi hak akses pengguna biasa dan administrator.
- **Penanganan Kesalahan (Exception Handling)** dengan blok `try-except` agar program tidak mengalami *crash* saat pengguna memasukkan tipe data yang salah.
- **Pemanfaatan Library Standar Python**: `datetime`, `random`, dan `os`.

---

## 🔑 Akun & Kredensial Login

| Role | Username | Password | Hak Akses |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin` | `admin123` | Akses penuh CRUD (Lihat, Tambah, Ubah, Hapus Film) |
| **User** | `user` | `user123` | Hanya Lihat Film (Read only) |

---

## ⚙️ Penjelasan Kode Program

Berikut rincian alur dan fungsi-fungsi yang digunakan dalam file program:

### 1. Import Modul
```python
import datetime
import random
import os
```
- `datetime`: Digunakan untuk merekam dan menampilkan waktu saat login berhasil dalam format tanggal dan jam (`%d-%m-%Y %H:%M`).
- `random`: Digunakan untuk menghasilkan kode film 4 digit acak (`random.randint(1000, 9999)`) saat penambahan data film baru.
- `os`: Digunakan untuk membersihkan tampilan terminal layar secara otomatis (`os.system`).

### 2. Struktur Data Utama
```python
akun = {
    "admin": ["admin123", "admin"],
    "user": ["user123", "user"]
}

film = [
    ["The Batman", "Action", 40000],
    ["Spirited Away", "Animation", 40000],
    ["Jujutsu Kaisen", "Fantasy", 40000]
]
```
- `akun` *(Dictionary)*: Menyimpan data pengguna dengan format `key: [password, role]`. Mempermudah verifikasi dan pencarian akun pengguna.
- `film` *(Nested List / List of Lists)*: Menyimpan koleksi data film berupa baris data yang memuat `[Nama Film, Kategori, Harga Tiket]`.

### 3. Fungsi `bersihkan()`
```python
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")
```
- Berfungsi membersihkan tampilan terminal. Menyesuaikan perintah OS secara otomatis: `cls` untuk Windows (`os.name == 'nt'`) dan `clear` untuk Linux/macOS.

### 4. Fungsi `login()`
```python
def login():
    ...
```
- Memberikan kesempatan maksimal **3 kali percobaan** kepada user untuk memasukkan username dan password.
- Jika pengguna langsung menekan `Enter` tanpa mengisi username (string kosong `""`), program langsung keluar (`return "keluar"`).
- Jika username dan password cocok, program mencetak tanggal & waktu saat itu (`datetime.datetime.now()`) lalu mengembalikan nama role (`admin` atau `user`).
- Jika gagal 3 kali, mengembalikan `None`.

### 5. Fungsi `lihat()` (Read)
```python
def lihat():
    print("@@@ DAFTAR FILM @@@")
    for i, f in enumerate(film, 1):
        print(f"{i}. {f[0]} | {f[1]} | Rp{f[2]}")
```
- Menggunakan perulangan `for` bersama `enumerate(film, 1)` untuk menampilkan daftar film berurutan mulai dari nomor 1 secara rapi dengan format: `Nomor. Judul | Genre | Harga`.

### 6. Fungsi `tambah()` (Create)
```python
def tambah():
    ...
```
- Meminta input nama film, kategori/genre, dan harga tiket.
- Menggunakan `film.append(data)` untuk memasukkan data baru ke dalam list `film`.
- Memanfaatkan `random.randint(1000, 9999)` untuk memberikan nomor kode unik pada film baru.
- Dilengkapi blok `try-except` untuk menangani kesalahan konversi jika input harga bukan angka numerik.

### 7. Fungsi `ubah()` (Update)
```python
def ubah():
    ...
```
- Menampilkan daftar film terlebih dahulu dengan memanggil fungsi `lihat()`.
- Meminta user memasukkan nomor urut film yang ingin diubah.
- Menggunakan validasi kondisi `0 < no <= len(film)`. Jika nomor valid, data di indeks ke-`no-1` diganti dengan data baru yang dimasukkan.
- Dilengkapi `try-except` untuk menangani jika user memasukkan karakter non-angka pada nomor film.

### 8. Fungsi `hapus()` (Delete)
```python
def hapus():
    ...
```
- Menampilkan daftar film melalui `lihat()`.
- Menghapus item dari list berdasarkan indeks menggunakan method bawaan `film.pop(no-1)`.
- Memvalidasi nomor film agar tidak terjadi *IndexError* dan menangani exception input.

### 9. Fungsi `menu(role)`
```python
def menu(role):
    ...
```
- Menampilkan menu dinamis berdasarkan peran pengguna:
  - Jika `role == "admin"`, opsi 1 sampai 5 akan ditampilkan (Lihat, Tambah, Ubah, Hapus, Logout).
  - Jika `role == "user"`, menu 2, 3, dan 4 disembunyikan sehingga user hanya dapat memilih opsi 1 (Lihat Film) dan 5 (Logout).
- Menggunakan perulangan `while True` agar pengguna dapat terus memilih menu hingga memilih opsi `5. Logout`.

### 10. Alur Program Utama (Main Execution Loop)
```python
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
- Mengatur siklus hidup program: memanggil `login()`, mengecek status hasil login, menjalankan `menu(role)`, serta menghentikan program jika user keluar atau batas percobaan terlampaui.

---

## 📸 Panduan Screenshot Terminal

Berikut adalah skenario screenshot terminal yang disarankan untuk melengkapi dokumentasi laporan/tugas.

### 💡 Tips Mengambil Screenshot di Windows
1. Jalankan program di Terminal / Command Prompt / VS Code Terminal dengan perintah:
   ```powershell
   python "MinPro 2 DDP B darrell.py"
   ```
2. Tekan kombinasi tombol **`Win + Shift + S`** pada keyboard untuk memilih area terminal.
3. Simpan gambar di folder misalnya `screenshots/` dengan nama yang sesuai.

---

### Daftar Screenshot yang Perlu Diambil:

#### 1. Screenshot Login Berhasil (Sebagai Admin)
- **Langkah**:
  1. Masukkan Username: `admin`
  2. Masukkan Password: `admin123`
- **Tampilan Output**: Muncul pesan `Login berhasil`, tanggal dan jam login (datetime), serta Menu Utama Admin (Opsi 1 sampai 5).
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Login Admin](screenshots/01_login_admin.png)
  ```

#### 2. Screenshot Fitur Lihat Film (Read)
- **Langkah**:
  1. Pada menu, pilih nomor `1`
- **Tampilan Output**: Menampilkan daftar film awal (The Batman, Spirited Away, Jujutsu Kaisen) dengan format nomor, genre, dan harga.
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Lihat Film](screenshots/02_lihat_film.png)
  ```

#### 3. Screenshot Fitur Tambah Film (Create - Role Admin)
- **Langkah**:
  1. Pilih nomor `2`
  2. Masukkan Nama film: `Inception`
  3. Masukkan Kategori: `Sci-Fi`
  4. Masukkan Harga: `45000`
- **Tampilan Output**: Menampilkan pesan `Film berhasil ditambah` dan `Kode: [4 digit acak]`.
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Tambah Film](screenshots/03_tambah_film.png)
  ```

#### 4. Screenshot Fitur Ubah Film (Update - Role Admin)
- **Langkah**:
  1. Pilih nomor `3`
  2. Masukkan nomor film yang ingin diubah (misalnya `1`)
  3. Masukkan data baru (misal: nama, kategori, harga baru)
- **Tampilan Output**: Muncul daftar film, input data baru, dan konfirmasi `Film berhasil diubah`.
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Ubah Film](screenshots/04_ubah_film.png)
  ```

#### 5. Screenshot Fitur Hapus Film (Delete - Role Admin)
- **Langkah**:
  1. Pilih nomor `4`
  2. Masukkan nomor film yang ingin dihapus (misalnya `2`)
- **Tampilan Output**: Muncul daftar film dan pesan `Film berhasil dihapus`.
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Hapus Film](screenshots/05_hapus_film.png)
  ```

#### 6. Screenshot Penanganan Error (Exception Handling)
- **Langkah**:
  1. Pilih menu `2` (Tambah Film)
  2. Masukkan Nama dan Kategori seperti biasa
  3. Pada input Harga, masukkan huruf (contoh: `abc`)
- **Tampilan Output**: Muncul pesan `Input harga harus angka` tanpa menyebabkan program error/crash keluar.
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Error Handling](screenshots/06_error_handling.png)
  ```

#### 7. Screenshot Tampilan Menu Pengguna Biasa (User)
- **Langkah**:
  1. Logout dari admin (menu `5`), lalu login dengan Username: `user` dan Password: `user123`.
- **Tampilan Output**: Perhatikan bahwa menu yang tampil hanya nomor `1. Lihat Film` dan `5. Logout` (tidak ada opsi tambah, ubah, dan hapus).
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Menu User](screenshots/07_menu_user.png)
  ```

#### 8. Screenshot Login Gagal (Batas 3 Kali Percobaan)
- **Langkah**:
  1. Masukkan password yang salah berturut-turut sebanyak 3 kali.
- **Tampilan Output**: Muncul pesan `Login salah` sebanyak 3 kali dan ditutup dengan pesan `Login gagal`.
- *Tempat Screenshot*:
  ```markdown
  ![Screenshot Login Gagal](screenshots/08_login_gagal.png)
  ```

---

## 🚀 Cara Menjalankan Program

1. Buka Terminal atau Command Prompt di direktori tempat file disimpan.
2. Jalankan perintah:
   ```bash
   python "MinPro 2 DDP B darrell.py"
   ```
3. Ikuti instruksi pada layar terminal untuk login dan memilih menu.
