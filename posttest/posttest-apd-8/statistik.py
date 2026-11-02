from data import daftar_rank, daftar_map, rankTertinggi
from tampilan import clear, judul, jeda, cetak_tabel, peringatan
from crud import hitung_total_game, hitung_rank_rr

def statistik(user_data):
    clear()
    judul(" REKAPITULASI STATISTIK PERFORMA ")
    history = user_data["history_catat"]
    if len(history) == 0:
        peringatan("Belum ada data rekap untuk dihitung.")
        jeda()
        return

    total_game = hitung_total_game(history)

    hasil_list = [match["hasil"] for match in history]
    kills = [match["kill"] for match in history]
    deaths = [match["death"] for match in history]
    assists = [match["assist"] for match in history]

    menang = hasil_list.count("W")
    kalah = hasil_list.count("L")
    seri = hasil_list.count("T")

    map_hitung = {}
    agent_hitung = {}
    for match in history:
        map_hitung[match["map"]] = map_hitung.get(match["map"], 0) + 1
        agent_hitung[match["agent"]] = agent_hitung.get(match["agent"], 0) + 1
    map_tersering = max(map_hitung, key=map_hitung.get)
    agent_tersering = max(agent_hitung, key=agent_hitung.get)

    # SET: map/agent unik dan map yang belum pernah dicoba (selisih himpunan)
    map_dimainkan = set(match["map"] for match in history)
    agent_unik = set(match["agent"] for match in history)
    map_belum = sorted(set(daftar_map) - map_dimainkan)

    rank, rr = hitung_rank_rr(user_data)
    if rank == rankTertinggi:
        rr_butuh = "Sudah rank tertinggi (Radiant)"
    else:
        rr_butuh = f"{100 - rr} RR lagi menuju {daftar_rank[rank + 1]}"

    baris = [
        ["Total Game Dimainkan", total_game],
        ["Tanggal Game Terakhir", history[-1]["tanggal"]],
        ["Menang / Kalah / Seri", f"{menang} / {kalah} / {seri}"],
        ["Total KDA", f"{sum(kills)} / {sum(deaths)} / {sum(assists)}"],
        ["Rata-rata KDA per Game", f"{round(sum(kills)/total_game, 1)} / {round(sum(deaths)/total_game, 1)} / {round(sum(assists)/total_game, 1)}"],
    ]

    for label, daftar in zip(("Kill", "Death", "Assist"), (kills, deaths, assists)):
        i_max = daftar.index(max(daftar))
        i_min = daftar.index(min(daftar))
        baris.append([f"{label} Terbanyak", f"{daftar[i_max]} - {history[i_max]['map']} ({history[i_max]['agent']})"])
        baris.append([f"{label} Terdikit", f"{daftar[i_min]} - {history[i_min]['map']} ({history[i_min]['agent']})"])

    baris += [
        ["Map Paling Sering Main", f"{map_tersering} ({map_hitung[map_tersering]}x)"],
        ["Agent Paling Sering", f"{agent_tersering} ({agent_hitung[agent_tersering]}x)"],
        ["Variasi Map / Agent", f"{len(map_dimainkan)} dari {len(daftar_map)} map / {len(agent_unik)} agent berbeda"],
        ["Map Belum Pernah Dimainkan", ", ".join(map_belum) if map_belum else "Semua map sudah dicoba"],
        ["Rank Saat Ini", f"{daftar_rank[rank]} (RR: {rr})"],
        ["Sisa RR Menuju Rank Naik", rr_butuh],
    ]
    cetak_tabel(["Statistik", "Nilai"], baris, rata="l", lebar_maks=60)
    jeda()