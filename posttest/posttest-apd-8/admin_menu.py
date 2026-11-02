from data import daftar_map, agents, data_performa, daftar_rank
from tampilan import clear, judul, jeda, cetak_tabel, sukses, error, peringatan, pilih_menu
from input_util import input_teks, pilih_pilihan
from crud import hitung_total_game, hitung_rank_rr

def tambah_map():
    clear()
    judul(" TAMBAH MAP ")
    nama_map_baru = input_teks("Masukkan nama map: ")
    # SET: cek duplikat tanpa peduli huruf besar/kecil
    map_terdaftar = {nama.lower() for nama in daftar_map}
    if nama_map_baru.lower() in map_terdaftar:
        error("Map sudah terdaftar!")
    else:
        daftar_map.append(nama_map_baru)
        sukses(f"Map '{nama_map_baru}' berhasil ditambahkan.")
    jeda()

def tambah_agent():
    clear()
    judul(" TAMBAH AGENT ")
    role = pilih_pilihan(agents, "Pilih role:")
    nama_agent_baru = input_teks("Masukkan nama agent: ")
    # SET: gabungkan semua agent dari semua role untuk cek duplikat
    agent_terdaftar = set()
    for daftar_agent in agents.values():
        agent_terdaftar.update(nama.lower() for nama in daftar_agent)
    if nama_agent_baru.lower() in agent_terdaftar:
        error("Agent sudah terdaftar!")
    else:
        agents[role].append(nama_agent_baru)
        sukses(f"Agent '{nama_agent_baru}' berhasil ditambahkan ke {role}.")
    jeda()

def rekap_pengguna():
    clear()
    judul(" REKAP SEMUA PENGGUNA ")
    if len(data_performa) == 0:
        peringatan("Belum ada data performa pengguna.")
    else:
        baris = []
        for nomor, (username, data) in enumerate(data_performa.items(), start=1):
            history = data["history_catat"]
            total = hitung_total_game(history)
            map_unik = len(set(m["map"] for m in history))
            
            if total == 0:
                rank_teks = "-"
            else:
                rank, rr = hitung_rank_rr(data)
                rank_teks = f"{daftar_rank[rank]} ({rr} RR)"
            baris.append([nomor, username, total, map_unik, rank_teks])
        cetak_tabel(["No", "Username", "Total Game", "Map Unik", "Rank Saat Ini"], baris)
    jeda()

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
            tambah_map()
        elif pilihan == 2:
            tambah_agent()
        elif pilihan == 3:
            rekap_pengguna()
        else:
            break