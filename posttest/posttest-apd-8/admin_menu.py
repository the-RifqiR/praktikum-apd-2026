from data import daftar_map, agents, data_performa, daftar_rank
from tampilan import clear, judul, jeda, cetak_tabel, sukses, error, peringatan, pilih_menu
from input_util import input_teks, pilih_pilihan

def menu_admin(username):
    while True:
        clear()
        pilihan = pilih_menu(f" ADMIN ({username}) ", {
            1 : "Tambah Map Baru",
            2 : "Tambah Agent Baru",
            3 : "Lihat Rekap Pengguna",
            4 : "Logout"
        })
        if pilihan == 1:
            # tambah_map()
            break
        elif pilihan == 2:
            # tambah_agent()
            break
        elif pilihan == 3:
            # rekap_pengguna()
            break
        else:
            break