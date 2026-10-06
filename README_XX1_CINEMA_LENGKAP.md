# XX1 CINEMA - Sistem Manajemen Film Python

## 1. Deskripsi Singkat Program

XX1 Cinema merupakan program berbasis Python yang digunakan untuk
melakukan pengelolaan data film sederhana dengan sistem login dan
pembagian hak akses pengguna.

Program memiliki dua role pengguna:

-   **Admin**: dapat melihat, menambah, mengubah, dan menghapus data
    film.
-   **User**: hanya dapat melihat daftar film.

Program menerapkan konsep pemrograman Python seperti function, list,
dictionary, percabangan, perulangan, exception handling, dan CRUD.

------------------------------------------------------------------------

# 2. Flowchart Program

Flowchart program dapat dilihat pada file berikut:

[Flowchart XX1 Cinema](assets/flowchart.drawio)

## Penjelasan Alur Flowchart

1.  Program dimulai.
2.  Pengguna melakukan login dengan memasukkan username dan password.
3.  Sistem melakukan pengecekan akun.
4.  Jika login gagal, pengguna diberikan kesempatan mencoba kembali.
5.  Jika login berhasil, sistem membaca role pengguna.
6.  Jika pengguna merupakan admin, maka tersedia menu:
    -   Lihat film
    -   Tambah film
    -   Ubah film
    -   Hapus film
7.  Jika pengguna merupakan user, maka hanya tersedia:
    -   Lihat film
8.  Pengguna dapat memilih logout untuk kembali ke halaman login.
9.  Program selesai ketika pengguna keluar.

------------------------------------------------------------------------

# 3. Dokumentasi Program dan Output

## A. Tampilan Login Admin

![Login Admin](assets/output_login_admin.png)

Penjelasan:

Pada tampilan ini pengguna melakukan login menggunakan akun admin.

Admin memiliki akses penuh terhadap sistem sehingga setelah login
berhasil akan muncul menu pengelolaan film.

------------------------------------------------------------------------

## B. Tampilan Login User

![Login User](assets/output_login_user.png)

Penjelasan:

Pada login user, sistem mengenali role sebagai pengguna biasa.

User hanya mendapatkan akses untuk melihat daftar film dan logout.

------------------------------------------------------------------------

## C. Menu Admin

![Menu Admin](assets/output_menu_admin.png)

Penjelasan:

Menu admin memiliki lima pilihan:

1.  Lihat Film
2.  Tambah Film
3.  Ubah Film
4.  Hapus Film
5.  Logout

Menu tambahan hanya muncul karena akun yang digunakan memiliki role
admin.

------------------------------------------------------------------------

## D. Menu User

![Menu User](assets/output_login_user.png)

Penjelasan:

Menu user lebih terbatas karena hanya dapat melihat film dan melakukan
logout.

Hal ini menunjukkan penerapan sistem hak akses berdasarkan role.

------------------------------------------------------------------------

## E. Menampilkan Daftar Film

![Daftar Film](assets/output_lihat_film.png)

Penjelasan:

Ketika memilih menu lihat film, program menampilkan seluruh data film
yang tersimpan.

Data yang ditampilkan:

-   Nomor film
-   Nama film
-   Kategori
-   Harga tiket

Contoh output:

    1. The Batman | Action | Rp40000
    2. Spirited Away | Animation | Rp40000
    3. Jujutsu Kaisen | Fantasy | Rp40000

------------------------------------------------------------------------

## F. Menambahkan Film Baru

![Tambah Film](assets/output_tambah_film.png)

Penjelasan:

Admin dapat menambahkan film baru dengan memasukkan:

-   Nama film
-   Kategori film
-   Harga film

Data baru akan disimpan menggunakan fungsi append() ke dalam list film.

------------------------------------------------------------------------

# 4. Dokumentasi Penerapan Nilai Tambah

Program ini memiliki beberapa nilai tambah:

## 1. Sistem Role User dan Admin

Program tidak hanya memiliki login biasa, tetapi menerapkan pembagian
hak akses.

Admin memiliki fitur CRUD, sedangkan user hanya dapat melihat data.

------------------------------------------------------------------------

## 2. Validasi Login

Program memberikan batas percobaan login sebanyak tiga kali.

Selain itu, username kosong akan langsung menghentikan program.

------------------------------------------------------------------------

## 3. Error Handling

Program menggunakan try-except untuk mencegah program berhenti ketika
pengguna memasukkan data yang tidak sesuai.

Contohnya ketika harga film harus berupa angka.

------------------------------------------------------------------------

## 4. Random Code

Ketika admin berhasil menambahkan film, program menghasilkan kode acak
sebagai informasi tambahan.

------------------------------------------------------------------------

## 5. Tampilan Terminal Lebih Rapi

Program menggunakan fungsi pembersihan terminal agar perpindahan menu
lebih nyaman digunakan.
