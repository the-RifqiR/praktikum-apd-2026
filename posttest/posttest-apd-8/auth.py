from pwinput import pwinput # Agar password tidak terlihat di terminal
from data import accounts
from tampilan import clear, judul, jeda, sukses, error
from input_util import input_teks

def cek_login(username, password, role):
    akun = accounts.get(username)
    return akun is not None and akun["password"] == password and akun["role"] == role

def login(role):
    clear()
    judul(f" LOGIN {role.upper()} ")
    inputUsername = input_teks("Username: ")
    inputPassword = pwinput("Password: ").strip()
    if cek_login(inputUsername, inputPassword, role):
        sukses("\nSelamat login berhasil")
        jeda()
        return inputUsername
    error("\nLogin gagal, mungkin ada yang salah 🤔")
    jeda()
    return None