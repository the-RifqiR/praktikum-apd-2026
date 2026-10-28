from autentifikasi import login
from mahasiswa import tambah_mahasiswa as create
from mahasiswa import lihat_mahasiswa as read

if login("admin", "123"):
    print("Login berhasil!\n")
# Menggunakan fungsi dari modul mahasiswa
    create("Budi Santoso", "2609106010")
    create("Siti Aminah", "2609106011")
    read()
else:
    print("Login gagal! Username atau password salah.") 