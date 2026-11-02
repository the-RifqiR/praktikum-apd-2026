import random
from data import data_performa
from tampilan import clear, judul, jeda, pilih_menu, peringatan

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
            # catat_game(user_data)
            # menu_crud(user_data)
            break
        elif pilihan == 2:
            # menu_crud(user_data)
            break
        else:
            break