from pwinput import pwinput
from data import accounts
from tampilan import clear, judul, jeda, sukses, error
from input_util import input_teks

def register():
    clear()
    judul(" REGISTER AKUN BARU ")
    while True:
        username = input_teks("Masukkan username baru: ")
        # SET: cek duplikat tanpa peduli huruf besar/kecil
        username_terpakai = {nama.lower() for nama in accounts}
        if username.lower() in username_terpakai:
            error("Username sudah terdaftar!")
        else:
            break
    while True:
        password = pwinput("Masukkan password baru: ").strip()
        if password:
            break
        error("Password tidak boleh kosong!")
    accounts[username] = {"password": password, "role": "user"}
    sukses("Registrasi berhasil, silakan login.")
    jeda()