from datetime import datetime
from data import daftar_rank, daftar_map, agents, rankTertinggi
from tampilan import clear, judul, jeda, cetak_tabel, sukses, error, peringatan
from input_util import input_angka, konfirmasi, pilih_pilihan

header_judul = ["No", "Tanggal", "Map", "Agent", "Hasil", "Score", "KDA", "RR"]

def hitung_total_game(history, indeks=0):
    if indeks >= len(history):
        return 0
    return 1 + hitung_total_game(history, indeks + 1)

def baris_game(nomor, m):
    return [nomor, m["tanggal"], m["map"], m["agent"], m["hasil"],
            f"{m['round_w']}-{m['round_l']}",
            f"{m['kill']}/{m['death']}/{m['assist']}", f"{m['rr']:+}"]

def tampil_daftar_game(history):
    if len(history) == 0:
        peringatan("Belum ada data game yang dimasukkan.")
        return
    baris = [baris_game(nomor, items) for nomor, items in enumerate(history, start=1)]
    cetak_tabel(header_judul, baris)

def atur_rank_awal(user_data):
    if user_data["rank_sudah_diisi"]:
        return
    nama_rank = pilih_pilihan(daftar_rank, "Pilih rank saat ini:")
    rank = daftar_rank.index(nama_rank)
    
    if rank == rankTertinggi:
        rr = input_angka("RR Radiant saat ini (minimal 0): ", 0)
    else:
        rr = input_angka("RR saat ini (0-99): ", 0, 99)
        
    user_data["rank"] = rank
    user_data["rr_awal"] = rr
    user_data["rank_sudah_diisi"] = True

def input_map():
    return pilih_pilihan(daftar_map, "Pilih map:")

def input_agent():
    role = pilih_pilihan(agents, "Pilih role agent:")
    return pilih_pilihan(agents[role], f"Pilih agent {role}:")

def input_score():
    round_w = input_angka("Jumlah Round Menang: ", 0)
    round_l = input_angka("Jumlah Round Kalah: ", 0)
    return round_w, round_l

def input_kda():
    k = input_angka("Total Kill: ", 0)
    d = input_angka("Total Death: ", 0)
    a = input_angka("Total Assist: ", 0)
    return k, d, a

def tentukan_hasil(round_w, round_l):
    if round_w > round_l:
        return "W"
    elif round_w < round_l:
        return "L"
    return "T"

def input_rr(hasil):
    if hasil == "W":
        return input_angka("RR Yang Didapat (minimal 1): ", 1, 100)
    elif hasil == "L":
        return -input_angka("RR Yang Didapat (minimal 1): ", 1, 100)
    return input_angka("RR Yang Didapat: ", -100, 100)

def input_data_game():
    nama_map = input_map()
    nama_agent = input_agent()
    round_w, round_l = input_score()
    hasil = tentukan_hasil(round_w, round_l)
    print(f"Hasil game: {hasil}")
    k, d, a = input_kda()
    rr = input_rr(hasil)

    return {"tanggal": datetime.now().strftime("%d/%m/%Y"),
            "map": nama_map, "agent": nama_agent,
            "round_w": round_w, "round_l": round_l, "hasil": hasil,
            "kill": k, "death": d, "assist": a, "rr": rr}

def catat_game(user_data):
    clear()
    judul(" CATAT PERFORMA GAME ")
    jumlah = input_angka("Jumlah game yang ingin dicatat: ", 1)
    atur_rank_awal(user_data)
    history = user_data["history_catat"]
    for gim in range(jumlah):
        print(f"\n--- GAME KE-{gim + 1} DARI {jumlah} ---")
        history.append(input_data_game())
    sukses("\nSemua data game berhasil dicatat!")
    jeda()

def pilih_nomor_game(history, aksi):
    while True:
        teks = input(f"\nNomor game untuk {aksi} (atau 'kembali'): ").strip().lower()
        if teks == "kembali":
            return None
        try:
            nomor = int(teks)
            if nomor < 1 or nomor > len(history):
                raise IndexError(f"Game #{nomor} tidak ditemukan!")
        except ValueError:
            error("ValueError: masukkan nomor berupa angka atau ketik 'kembali'.")
        except IndexError as e:
            error(f"IndexError: {e}")
        else:
            return nomor - 1

def update_game(user_data):
    clear()
    judul(" UPDATE DATA GAME ")
    history = user_data["history_catat"]
    if len(history) == 0:
        peringatan("Belum ada data untuk diubah.")
        jeda()
        return

    tampil_daftar_game(history)
    idx = pilih_nomor_game(history, "diubah")
    if idx is None:
        return

    lama = history[idx]
    baru = lama.copy()

    print(f"\nMengubah Game #{idx + 1}")
    if konfirmasi(f"Ganti Map ({lama['map']})? (y/t): "):
        baru["map"] = input_map()
    if konfirmasi(f"Ganti Agent ({lama['agent']})? (y/t): "):
        baru["agent"] = input_agent()
    if konfirmasi(f"Ganti Score ({lama['round_w']}-{lama['round_l']})? (y/t): "):
        baru["round_w"], baru["round_l"] = input_score()
        baru["hasil"] = tentukan_hasil(baru["round_w"], baru["round_l"])
    if konfirmasi(f"Ganti KDA ({lama['kill']}/{lama['death']}/{lama['assist']})? (y/t): "):
        baru["kill"], baru["death"], baru["assist"] = input_kda()

    if baru["hasil"] != lama["hasil"]:
        peringatan(f"Hasil berubah {lama['hasil']} menjadi {baru['hasil']}; RR wajib diisi ulang.")
        baru["rr"] = input_rr(baru["hasil"])
    elif konfirmasi(f"Ganti RR ({lama['rr']:+})? (y/t): "):
        baru["rr"] = input_rr(baru["hasil"])

    print("\n--- RINGKASAN DATA YANG DIPERBARUI ---")
    cetak_tabel(header_judul, [baris_game(idx + 1, baru)])

    if konfirmasi("Simpan perubahan? (y/t): "):
        history[idx] = baru
        sukses("Data game berhasil diupdate")
    else:
        peringatan("Perubahan dibatalkan.")
    jeda()

def hapus_game(user_data):
    clear()
    judul(" HAPUS DATA GAME ")
    history = user_data["history_catat"]
    if len(history) == 0:
        peringatan("Belum ada data untuk dihapus.")
        jeda()
        return

    tampil_daftar_game(history)
    idx = pilih_nomor_game(history, "dihapus")
    if idx is None:
        return
    if konfirmasi(f"Yakin hapus Game #{idx + 1}? (y/t): "):
        history.pop(idx)
        sukses("Data game berhasil dihapus!")
    else:
        peringatan("Hapus data dibatalkan.")
    jeda()

def hitung_rank_rr(user_data):
    rank = user_data["rank"]
    rr = user_data["rr_awal"]
    for match in user_data["history_catat"]:
        rr += match["rr"]
        while rr >= 100 and rank < rankTertinggi:
            rr -= 100
            rank += 1
        while rr < 0 and rank > 0:
            rr += 100
            rank -= 1
        if rank == 0 and rr < 0:
            rr = 0
    return rank, rr