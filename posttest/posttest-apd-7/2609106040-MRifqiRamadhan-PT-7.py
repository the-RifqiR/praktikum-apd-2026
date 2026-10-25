import os

accounts = {
    "adminvlao": {"password": "admin123", "role": "admin"},
    "bangyoga": {"password": "049", "role": "admin"},
    "mbafina": {"password": "016", "role": "admin"},
    "aja": {"password": "041", "role": "user"},
}

daftar_rank = {1: "Iron", 2: "Bronze", 3: "Silver", 4: "Gold", 5: "Platinum", 6: "Diamond", 7: "Ascendant", 8: "Immortal", 9: "Radiant"}

daftar_map = {"Ascent": True, "Bind": True, "Haven": True, "Split": True, "Lotus": True, "Sunset": True, "Abyss": True, "Corrode": True, "Icebox": True, "Summit": True, "Pearl": True, "Fracture": True, "Breeze": True}

agents = {
    "Duelist": {"Jett": True, "Phoenix": True, "Raze": True, "Reyna": True, "Yoru": True, "Neon": True, "Iso": True, "Waylay": True, "Hush": True},
    "Initiator": {"Breach": True, "Sova": True, "Skye": True, "Kayo": True, "Fade": True, "Gekko": True, "Tejo": True},
    "Controller": {"Brimstone": True, "Omen": True, "Viper": True, "Astra": True, "Harbor": True, "Clove": True, "Miks": True},
    "Sentinel": {"Sage": True, "Cypher": True, "Killjoy": True, "Chamber": True, "Deadlock": True, "Vyse": True, "Veto": True}
}

data_performa = {}
bintang = "=" * 45

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def jeda():
    input("\nTekan ENTER untuk kembali...")


def judul(teks):
    print(bintang)
    print(teks.center(45, "="))
    print(bintang)


def tampil_menu_awal():
    judul(" SELAMAT DATANG DI VLAOTRACKER ")
    print("1. Admin")
    print("2. Lu Member")
    print("3. Belum Punya Akun? (Register)")
    print("4. Keluar Program")
    print(bintang)


def tampil_menu_admin(username):
    judul(f" ADMIN ({username}) ")
    print("1. Tambah Map Baru")
    print("2. Tambah Agent Baru")
    print("3. Lihat Rekap Pengguna")
    print("4. Logout")


def tampil_menu_user(username):
    judul(f" DASHBOARD USER ({username}) ")
    print("1. Catat Performa Game Baru")
    print("2. Menu Kelola & Statistik Performa (CRUD)")
    print("3. Logout")


def tampil_menu_crud():
    judul(" KELOLA & STATISTIK PERFORMA ")
    print("1. Lihat Data Per Game")
    print("2. Tambah Data Game")
    print("3. Update Data Game")
    print("4. Delete (Hapus) Data Game")
    print("5. Lihat Statistik & Rekap Lengkap")
    print("6. Kembali ke Dashboard")