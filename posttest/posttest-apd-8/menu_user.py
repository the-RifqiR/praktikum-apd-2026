import random
from data import data_performa
from tampilan import clear, judul, jeda, pilih_menu, peringatan
from crud import tampil_daftar_game, catat_game, update_game, hapus_game
from statistik import statistik

TIPS = (
    "Tips: Catat game segera setelah main biar datanya akurat.",
    "Tips: Cek statistik untuk tahu map yang paling jarang kamu mainkan.",
    "Tips: Kalah itu biasa, yang penting main buat hobi.",
    "Tips: Jangan lupa istirahat, rank gak kemana-mana tapi posttest duh le.",
)

def menu_crud(user_data):
    while True:
        clear()
        pilihan = pilih_menu(" KELOLA & STATISTIK PERFORMA ", {
            1 : "Lihat Data Per Game",
            2 : "Tambah Data Game",
            3 : "Update Data Game",
            4 : "Delete (Hapus) Data Game",
            5 : "Lihat Statistik & Rekap Lengkap",
            6 : "Kembali ke Dashboard"
        })
        if pilihan == 1:
            clear()
            judul(" DAFTAR GAME TERCATAT ")
            tampil_daftar_game(user_data["history_catat"])
            jeda()
        elif pilihan == 2:
            catat_game(user_data)
        elif pilihan == 3:
            update_game(user_data)
        elif pilihan == 4:
            hapus_game(user_data)
        elif pilihan == 5:
            statistik(user_data)
        else:
            break

def menu_user(username):
    if username not in data_performa:
        data_performa[username] = {"rank": 0, "rr_awal": 0, "rank_sudah_diisi": False, "history_catat": []}

    user_data = data_performa[username]
    while True:
        clear()
        peringatan(random.choice(TIPS))
        pilihan = pilih_menu(f" DASHBOARD USER ({username}) ", {
            1 : "Catat Performa Game Baru",
            2 : "Menu Kelola & Statistik Performa (CRUD)",
            3 : "Logout"
        })
        if pilihan == 1:
            catat_game(user_data)
            menu_crud(user_data)
        elif pilihan == 2:
            menu_crud(user_data)
        else:
            break