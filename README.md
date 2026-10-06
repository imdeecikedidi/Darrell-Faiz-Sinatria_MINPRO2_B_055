[README_XX1_CINEMA_FINAL.md]
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

sistem menampilkan seluruh data film yang tersimpan. Pada menu tambah
film, admin dapat memasukkan data film baru yang kemudian disimpan ke
dalam daftar film. Pada menu ubah film, admin dapat memperbarui data
film berdasarkan nomor film yang dipilih. Sedangkan pada menu hapus
film, admin dapat menghapus data film tertentu.

Setelah selesai menggunakan sistem, pengguna dapat memilih logout untuk
kembali ke halaman login. Apabila pengguna memasukkan menu yang tidak
tersedia, sistem akan memberikan pesan kesalahan dan meminta pengguna
memilih menu kembali.

------------------------------------------------------------------------

# 3. Dokumentasi Program dan Output

## Login Admin

<img width="178" height="114" alt="output_login_admin" src="https://github.com/user-attachments/assets/eed535e7-1194-459f-b33d-7e91fd46494f" />


Pada bagian ini pengguna masuk menggunakan akun admin. Setelah proses
login berhasil, sistem mengenali role sebagai admin dan memberikan akses
terhadap seluruh fitur pengelolaan film.

## Login User

<img width="129" height="57" alt="output_login_user" src="https://github.com/user-attachments/assets/197794ea-ee9d-40b8-b62a-974070e6e6ab" />

Pada bagian ini pengguna masuk menggunakan akun user. Sistem membatasi
fitur yang tersedia karena user hanya memiliki akses untuk melihat film
dan logout.

## Menu Admin

<img width="122" height="83" alt="output_menu_admin" src="https://github.com/user-attachments/assets/73df10eb-274a-4889-bda6-89cd636f394c" />


Menu admin menyediakan fitur: - Lihat Film - Tambah Film - Ubah Film -
Hapus Film - Logout

Fitur tersebut digunakan untuk mengelola data film dalam sistem.

## Daftar Film

<img width="202" height="126" alt="output_lihat_film" src="https://github.com/user-attachments/assets/a88a11b8-0aee-42b4-b1a6-b89d138d7421" />


Menu lihat film menampilkan data film yang tersimpan berupa nomor film,
nama film, kategori, dan harga tiket.

## Tambah Film

<img width="188" height="133" alt="output_tambah_film" src="https://github.com/user-attachments/assets/09e6f7fb-ffc7-4701-9178-a1975b53c42c" />


Admin dapat memasukkan film baru dengan mengisi nama film, kategori, dan
harga. Data tersebut kemudian disimpan ke dalam list film.

------------------------------------------------------------------------

# 4. Penjelasan Kode Program

## Import Library

``` python
import datetime
import random
import os
```

Kode tersebut digunakan untuk memanggil library yang diperlukan oleh
program. Library datetime digunakan untuk menampilkan waktu login,
random digunakan untuk membuat kode acak ketika film ditambahkan, dan os
digunakan untuk membersihkan terminal.

------------------------------------------------------------------------

## Data Akun

``` python
akun = {
    "admin": ["admin123", "admin"],
    "user": ["user123", "user"]
}
```

Kode ini menyimpan data akun pengguna menggunakan dictionary. Data
tersebut berisi username, password, dan role pengguna yang digunakan
untuk menentukan hak akses menu.

------------------------------------------------------------------------

## Data Film

``` python
film = [
    ["The Batman", "Action", 40000],
    ["Spirited Away", "Animation", 40000],
    ["Jujutsu Kaisen", "Fantasy", 40000]
]
```

Kode ini menyimpan daftar film menggunakan list dua dimensi. Setiap data
film terdiri dari nama film, kategori, dan harga tiket.

------------------------------------------------------------------------

## Fungsi Bersihkan Terminal

``` python
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")
```

Fungsi ini digunakan untuk membersihkan tampilan terminal. Perintah yang
digunakan menyesuaikan sistem operasi yang digunakan.

------------------------------------------------------------------------

## Fungsi Login

``` python
def login():
```

Fungsi login digunakan untuk melakukan proses autentikasi pengguna.
Program melakukan pengecekan username dan password sebanyak tiga kali
percobaan.

Jika data sesuai, fungsi mengembalikan role pengguna. Jika username
kosong, program akan berhenti.

------------------------------------------------------------------------

## Fungsi Lihat Film

``` python
def lihat():
```

Fungsi ini digunakan untuk menampilkan seluruh data film. Program
menggunakan perulangan enumerate() agar setiap film memiliki nomor urut.

------------------------------------------------------------------------

## Fungsi Tambah Film

``` python
def tambah():
```

Fungsi tambah digunakan oleh admin untuk memasukkan data film baru. Data
yang dimasukkan akan disimpan menggunakan append() ke dalam list film.

Program menggunakan try-except untuk menangani kesalahan input, terutama
pada bagian harga yang harus berupa angka.

------------------------------------------------------------------------

## Fungsi Ubah Film

``` python
def ubah():
```

Fungsi ini digunakan untuk memperbarui data film. Admin memilih nomor
film kemudian memasukkan data baru untuk menggantikan data sebelumnya.

Penggunaan index `no-1` dilakukan karena index list Python dimulai dari
angka 0.

------------------------------------------------------------------------

## Fungsi Hapus Film

``` python
def hapus():
```

Fungsi ini digunakan untuk menghapus data film menggunakan method pop().
Data dihapus berdasarkan nomor film yang dipilih oleh admin.

------------------------------------------------------------------------

## Fungsi Menu

``` python
def menu(role):
```

Fungsi menu digunakan untuk mengatur tampilan berdasarkan role pengguna.
Admin mendapatkan menu lengkap, sedangkan user mendapatkan menu
terbatas.

Perulangan while digunakan agar menu terus berjalan sampai pengguna
memilih logout.

------------------------------------------------------------------------

## Program Utama

``` python
while True:
    role = login()
```

Bagian ini menjalankan keseluruhan program. Sistem akan menjalankan
login terlebih dahulu, kemudian mengarahkan pengguna ke menu sesuai role
yang berhasil masuk.

------------------------------------------------------------------------

# 5. Penerapan Nilai Tambah

Program XX1 Cinema memiliki beberapa nilai tambah, yaitu:

## 1. Sistem Role Pengguna

Program menerapkan pembagian hak akses antara admin dan user sehingga
setiap pengguna mendapatkan fitur sesuai kebutuhan.

## 2. Validasi Input

Program melakukan validasi terhadap input pengguna untuk mengurangi
kesalahan, seperti pengecekan password dan validasi harga harus berupa
angka.

## 3. Error Handling

Penggunaan try-except membuat program tetap berjalan ketika terjadi
kesalahan input.

## 4. Kode Random

Program memberikan kode acak setelah admin berhasil menambahkan film
sebagai informasi tambahan.

## 5. Tampilan Terminal

Penggunaan fungsi pembersihan terminal membuat tampilan program lebih
rapi dan mudah digunakan.

------------------------------------------------------------------------

# Kesimpulan

XX1 Cinema merupakan program pengelolaan film berbasis Python yang
menerapkan sistem login, hak akses pengguna, dan operasi CRUD. Program
ini menunjukkan penerapan konsep dasar pemrograman Python dalam membuat
sistem sederhana yang memiliki struktur dan validasi yang baik.


FLOWCHART DAN PENJELASAN
<img width="6087" height="4758" alt="FLOWCHART MINPRO 2 DARRELL final betul drawio" src="https://github.com/user-attachments/assets/7b314507-49ca-4f59-b5ab-c980a11e1ee3" />
Penjelasan Alur Flowchart Program XX1 Cinema
Flowchart program XX1 Cinema menggambarkan alur kerja sistem mulai dari program dijalankan hingga pengguna keluar dari sistem. Program diawali dengan proses mulai, kemudian sistem menampilkan halaman login yang meminta pengguna memasukkan username dan password. Setelah data dimasukkan, sistem akan melakukan proses validasi dengan mencocokkan data tersebut dengan akun yang telah tersimpan.
Jika username atau password yang dimasukkan tidak sesuai, sistem akan menampilkan pesan bahwa login gagal dan pengguna dapat melakukan percobaan login kembali. Namun, jika data login benar, sistem akan menampilkan pesan login berhasil serta mencatat waktu login menggunakan fungsi datetime. Setelah proses login berhasil, sistem akan melakukan pengecekan terhadap role pengguna untuk menentukan menu yang dapat diakses.
Apabila pengguna memiliki role sebagai admin, maka sistem akan menampilkan menu lengkap yang terdiri dari melihat film, menambah film, mengubah film, menghapus film, dan logout. Admin memiliki hak akses penuh terhadap pengelolaan data film karena dapat melakukan proses CRUD (Create, Read, Update, Delete). Sedangkan apabila pengguna memiliki role sebagai user, sistem hanya menampilkan menu untuk melihat daftar film dan melakukan logout. Pembatasan menu ini dilakukan agar setiap pengguna memiliki akses sesuai dengan hak yang telah ditentukan.
Pada menu lihat film, sistem akan mengambil data film yang tersimpan kemudian menampilkannya dalam bentuk daftar yang berisi nomor film, nama film, kategori, dan harga tiket. Pada menu tambah film, admin diminta memasukkan data film baru berupa nama film, kategori, dan harga. Data yang telah dimasukkan akan melalui proses validasi, kemudian disimpan ke dalam daftar film apabila data sesuai. Program juga menghasilkan kode acak sebagai informasi tambahan setelah film berhasil ditambahkan.
Pada menu ubah film, admin terlebih dahulu memilih nomor film yang ingin diperbarui. Sistem akan mengecek apakah nomor tersebut tersedia dalam daftar film. Jika nomor valid, admin dapat memasukkan data baru untuk menggantikan data film sebelumnya. Sedangkan pada menu hapus film, admin memilih nomor film yang ingin dihapus, kemudian sistem akan menghapus data tersebut dari daftar apabila nomor film ditemukan.
Setelah pengguna selesai menggunakan sistem, pengguna dapat memilih menu logout. Ketika logout dipilih, sistem akan menghapus sesi menu pengguna dan kembali ke halaman login. Jika pengguna memasukkan pilihan menu yang tidak tersedia, sistem akan menampilkan pesan bahwa menu tidak tersedia dan mengarahkan pengguna kembali ke menu utama.
Secara keseluruhan, flowchart ini menunjukkan bahwa program XX1 Cinema menerapkan sistem login berbasis role dengan pengelolaan data film yang terstruktur. Alur program dibuat agar setiap proses memiliki validasi sehingga pengguna dapat menjalankan sistem dengan lebih mudah dan mengurangi kesalahan saat melakukan input data.
