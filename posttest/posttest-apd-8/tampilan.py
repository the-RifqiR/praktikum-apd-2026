import os # Untuk membersihkan terminal
from prettytable import PrettyTable # Library untuk tabel
from InquirerPy import inquirer # Library menu pointer
from colorama import Fore, Style, init # Library untuk mewarnai teks

init(autoreset=True)

bintang = "=" * 45

def clear():
    os.system("cls || clear")

def jeda():
    input(Fore.YELLOW + "\nTekan enter untuk melanjutkan..." + Style.RESET_ALL)

def judul(teks):
    print(Fore.CYAN + bintang)
    print(teks.center(45, "="))
    print(bintang + Style.RESET_ALL)

def sukses(teks):
    print(Fore.GREEN + teks + Style.RESET_ALL)

def error(teks):
    print(Fore.RED + teks + Style.RESET_ALL)

def peringatan(teks):
    print(Fore.YELLOW + teks + Style.RESET_ALL)

def cetak_tabel(headers, rows, rata="c", lebar_maks=None):
    tabel = PrettyTable()
    tabel.field_names = [f"{Fore.BLUE}{item}{Style.RESET_ALL}" for item in headers]
    
    for baris in rows:
        tabel.add_row([str(item) for item in baris])
    tabel.align = rata
    if lebar_maks:
        tabel.max_width = lebar_maks
    print(tabel)

def pilih_menu(judul_teks, opsi):
    judul(judul_teks)
    return inquirer.select(
        message="Pilih menu:",
        choices=opsi,
        pointer="➡️ ",
        qmark=""
    ).execute()