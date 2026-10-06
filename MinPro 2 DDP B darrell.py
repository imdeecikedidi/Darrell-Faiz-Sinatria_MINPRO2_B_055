import datetime
import random
import os


akun = {
    "admin": ["admin123", "admin"],
    "user": ["user123", "user"]
}


film = [
    ["The Batman", "Action", 40000],
    ["Spirited Away", "Animation", 40000],
    ["Jujutsu Kaisen", "Fantasy", 40000]
]


def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    print("@@@ LOGIN XX1 CINEMA @@@")

    for i in range(3):
        user = input("Username: ")

        # Jika username kosong, program langsung ditutup
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


def lihat():
    print("@@@ DAFTAR FILM @@@")

    for i, f in enumerate(film, 1):
        print(f"{i}. {f[0]} | {f[1]} | Rp{f[2]}")


def tambah():
    print("@@@ TAMBAH FILM @@@")

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

        else:
            print("Film tidak ditemukan")

    except:
        print("Input tidak valid")


def hapus():
    lihat()

    try:
        no = int(input("Nomor film: "))

        if 0 < no <= len(film):
            film.pop(no-1)
            print("Film berhasil dihapus")

        else:
            print("Film tidak ditemukan")

    except:
        print("Input tidak valid")


def menu(role):

    while True:
        bersihkan()

        print("@@@ MENU XX1 CINEMA @@@")
        print("1. Lihat Film")

        if role == "admin":
            print("2. Tambah Film")
            print("3. Ubah Film")
            print("4. Hapus Film")

        print("5. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            lihat()

        elif pilih == "2" and role == "admin":
            tambah()

        elif pilih == "3" and role == "admin":
            ubah()

        elif pilih == "4" and role == "admin":
            hapus()

        elif pilih == "5":
            print("Logout berhasil")
            break

        else:
            print("Menu tidak tersedia")

        input("\nEnter untuk lanjut...")


while True:

    role = login()

    if role == "keluar":
        break

    elif role:
        menu(role)

    else:
        print("Login gagal")
        break