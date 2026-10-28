# hasil_bagi = divmod(8,3)


# pangkat = pow(4,4)
# print(hasil_bagi)
# print(pangkat)


# import math

# math.sqrt()

# from math import sqrt

# from datetime import datetime

# print(datetime.now())


# import calendar as kalender
# print(kalender.calendar(2045))


import random
# Menghasilkan satu bilangan bulat acak dari 1 sampai 5 (inklusif)
# print(random.randint(1, 5))


# buah = ["pisang", "rambutan", "manggis"]
# huruf = "abcd"
# print(random.choice(buah)) # memilih 1 item acak pada list
# print(random.choice(huruf)) # memilih 1 karakter acak pada string
# kumpulan_angka = "0123456789"
# pin_acak = ""
# for i in range(4):
#     pin_acak += random.choice(kumpulan_angka)
# print(pin_acak)

# kartu = {"As" : "Wajik", "3":"Hati", "7": "Sekop"}
# random.shuffle(kartu)
# print(kartu)
# from prettytable import PrettyTable
# # Membuat objek tabel dan menentukan nama-nama kolom
# tabel = PrettyTable()
# tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]
# # Menambahkan satu baris data ke dalam tabel
# tabel.add_row(["2609106001", "Andi Alarice", "Informatika"])
# # Menambahkan beberapa baris data sekaligus menggunakan list di dalam list
# tabel.add_rows([
# ["2609106002", "Hammam Nopal", "Informatika"],
# ["2609106003", "Abimar LLM", "Sistem Informasi"]
# ])

# tabel.align["Nama Mahasiswa"] = "c"
# print(tabel)
# import inquirer
# # Menyusun daftar pertanyaan menu
# pertanyaan = [
#     inquirer.List(
#         'menu',
#         message='Pilih menu aplikasi',
#         choices=['Tambah Data', 'Lihat Data', 'Keluar'],
#     ),
# ]
# # Menampilkan prompt di terminal dan menyimpan hasil pilihan
# jawaban = inquirer.prompt(pertanyaan)
# print(jawaban) # Output berupa Dictionary, misal: {'menu': 'Tambah Data'}
# print(jawaban["menu"]) # Mengambil nilai berdasarkan key 'menu': Tambah Data

# studi kasus
import random
from datetime import datetime

kode_keamanan = "0123456789"
kode = ""

for i in range(6):
    kode += random.choice(kode_keamanan)

waktu_pembuatan = datetime.now()
tanggal = waktu_pembuatan.strftime("%d/%m/%Y")

print(tanggal)
print(kode)