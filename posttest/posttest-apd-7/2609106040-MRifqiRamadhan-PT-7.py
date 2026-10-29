import os

# atart global variabel
accounts = {
    "adminvlao": {"password": "admin123", "role": "admin"},
    "bangyoga": {"password": "017", "role": "admin"},
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
# end global variabel

bintang = "=" * 45

# prosedur
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# prosedur
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
    
# fungsi pake paramater
def input_angka(pesan, minimum=0, maksimum=None):
    while True:
        try:
            angka = int(input(pesan).strip())
            if angka < minimum:
                raise ValueError(f"Angka minimal {minimum}.")
            if maksimum is not None and angka > maksimum:
                raise ValueError(f"Angka maksimal {maksimum}.")
        except ValueError as error:
            print(f"Input tidak valid: {error}")
        else:
            return angka    

# fungsi pake paramater
def input_teks(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as error:
            print(error)
        else:
            return teks

def cek_login(username, password, role):
    akun = accounts.get(username)
    return akun is not None and akun["password"] == password and akun["role"] == role

def register():
    clear()
    judul(" REGISTER AKUN BARU ")
    while True:
        # lokal variabel 1
        username = input_teks("Masukkan username baru: ")
        # lokal variabel 2
        sudah_ada = False
        for nama_akun in accounts:
            if nama_akun.lower() == username.lower():
                sudah_ada = True
        if sudah_ada:
            print("Username sudah terdaftar!")
        else:
            break
    password = input_teks("Masukkan password baru: ")
    accounts[username] = {"password": password, "role": "user"}
    print("Registrasi berhasil, silakan login.")
    jeda()
    
def login(role):
    clear()
    judul(f" LOGIN {role.upper()} ")
    # lokal variabel 3
    username = input_teks("Username: ")
    # lokal variabel 4 
    password = input_teks("Password: ")
    if cek_login(username, password, role):
        print("Selamat login berhasil")
        jeda()
        return username
    else:
        print("Login gagal, mungkin ada yang salah 🤔")
        jeda()
        return None

# Admin
        
def tambah_map():
    clear()
    judul(" TAMBAH MAP ")
    # lokal variabel 5
    nama_baru = input_teks("Masukkan nama map: ")
    for nama_map in daftar_map:
        if nama_map.lower() == nama_baru.lower():
            print("Map sudah terdaftar!")
            jeda()
            return
    daftar_map[nama_baru] = True
    print(f"Map '{nama_baru}' berhasil ditambahkan.")
    jeda()
    
def tambah_agent():
    clear()
    judul(" TAMBAH AGENT ")
    role = pilih_dari_dictionary(agents, "Pilih nomor role: ")
    nama_baru = input_teks("Masukkan nama agent: ")
    for nama_role, daftar_agent in agents.items():
        for nama_agent in daftar_agent:
            if nama_agent.lower() == nama_baru.lower():
                print(f"Agent sudah terdaftar pada role {nama_role}!")
                jeda()
                return
    agents[role][nama_baru] = True
    print(f"Agent '{nama_baru}' berhasil ditambahkan ke {role}.")
    jeda()
 
# INI rekursinya: menghitung jumlah game dari daftar nomor game.
# Base case: indeks mencapai panjang daftar, hasilnya 0.
# Recursive case: hitung 1 game lalu lanjutkan ke indeks berikutnya.
def hitung_total_game(daftar_nomor, indeks=0):
    if indeks >= len(daftar_nomor):
        return 0
    else:
        return 1 + hitung_total_game(daftar_nomor, indeks + 1)
       
def rekap_pengguna():
    clear()
    judul(" REKAP SEMUA PENGGUNA ")
    if len(data_performa) == 0:
        print("Belum ada data performa pengguna.")
    else:
        for username, data in data_performa.items():
            print(f"Username: {username} | Total Game: {hitung_total_game(list(data['history_catat'].keys()))}")
    jeda()
    
def menu_admin(username):
    while True:
        clear()
        tampil_menu_admin(username)
        pilihan = input_angka("Pilih menu (1-4): ", 1, 4)
        if pilihan == 1:
            tambah_map()
        elif pilihan == 2:
            tambah_agent()
        elif pilihan == 3:
            rekap_pengguna()
        else:
            break

# User
# fungsi dengan parameter
def pilih_dari_dictionary(data, pesan):
    # lokal variabel
    pilihan = {}
    # lokal variabel
    nomor = 1
    for nama in data:
        pilihan[nomor] = nama
        print(f"{nomor}. {nama}")
        nomor += 1
    nomor_pilih = input_angka(pesan, 1, len(pilihan))
    return pilihan[nomor_pilih]

def atur_rank_awal(user_data):
    if user_data["rank_sudah_diisi"]:
        return
    print("\nPilih Rank Saat Ini:")
    for nomor, nama_rank in daftar_rank.items():
        print(f"{nomor}. {nama_rank}")
    rank = input_angka("Pilih nomor rank (1-9): ", 1, len(daftar_rank))
    if rank == len(daftar_rank):
        rr = input_angka("RR Radiant saat ini (minimal 0): ", 0)
    else:
        rr = input_angka("RR saat ini (0-99): ", 0, 99)
    user_data["rank"] = rank
    user_data["rr_awal"] = rr
    user_data["rank_sudah_diisi"] = True
    
# Read
def tampil_daftar_game(history):
    if len(history) == 0:
        print("Belum ada data game yang dimasukkan.")
    else:
        for nomor, match in history.items():
            print(f"Game #{nomor} | Map: {match['map']} | Agent: {match['agent']}")
            print(f"  Hasil: {match['hasil']} ({match['round_w']}-{match['round_l']}) "
                  f"| KDA: {match['kill']}/{match['death']}/{match['assist']} "
                  f"| RR: {match['rr']:+}")

# fungsi tanpa parameter
def input_map():
    print("\nDaftar Map:")
    return pilih_dari_dictionary(daftar_map, "Pilih nomor map: ")

# fungsi tanpa parameter
def input_agent():
    print("\nPilih Role Agent:")
    role = pilih_dari_dictionary(agents, "Pilih nomor role: ")
    print(f"\nDaftar Agent {role}:")
    return pilih_dari_dictionary(agents[role], "Pilih nomor agent: ")

# fungsi tanpa parameter
def input_score():
    round_w = input_angka("Jumlah Round Menang: ", 0)
    round_l = input_angka("Jumlah Round Kalah: ", 0)
    return round_w, round_l

# fungsi tanpa parameter
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
    while True:
        try:
            if hasil == "W":
                input_rr = int(input("RR Yang Didapat: ").strip())
                if input_rr <= 0:
                    raise ValueError("Minimal dapat 1 RR lah.")
                return input_rr
            elif hasil == "L":
                input_rr = int(input("RR Yang Didapat: ").strip())
                if input_rr <= 0:
                    raise ValueError("Minimal dapat 1 RR lah.")
                return -input_rr
            else:
                return int(input("RR seri (boleh negatif, positif, atau 0): ").strip())
        except ValueError as error:
            print(f"RR tidak valid: {error}")

# fungsi tanpa parameter
def input_data_game():
    # lokal variabel
    nama_map = input_map()
    # lokal variabel
    nama_agent = input_agent()
    # lokal variabel
    round_w, round_l = input_score()
    # lokal variabel
    hasil = tentukan_hasil(round_w, round_l)
    print(f"Hasil game: {hasil}")
    k, d, a = input_kda()
    rr = input_rr(hasil)
    return {"map": nama_map, "agent": nama_agent, "round_w": round_w, "round_l": round_l, "hasil": hasil, "kill": k, "death": d, "assist": a, "rr": rr}

def catat_game(user_data):
    clear()
    judul(" CATAT PERFORMA GAME ")
    jumlah = input_angka("Jumlah game yang ingin dicatat: ", 1)
    atur_rank_awal(user_data)
    history = user_data["history_catat"]
    
    for gim in range(jumlah):
        print(f"\n--- GAME KE-{gim + 1} DARI {jumlah} ---")
        data = input_data_game()
        nomor_baru = 1
        
        if len(history) > 0:
            nomor_baru = max(history.keys()) + 1
        history[nomor_baru] = data
    print("\nSemua data game berhasil dicatat!")
    jeda()
    
# fungsi pake parameter
def pilih_nomor_game(history, aksi):
    while True:
        teks = input(f"\nNomor game untuk {aksi} (atau 'kembali'): ").strip().lower()
        
        if teks == "kembali":
            return None
        try:
            nomor = int(teks)
            if nomor not in history:
                raise KeyError(f"Game #{nomor} tidak ditemukan!")
        except ValueError:
            print("ValueError: masukkan nomor berupa angka atau 'kembali'.")
        except KeyError as error:
            print(f"KeyError: {error}")
        else:
            return nomor

def konfirmasi(pesan):
    while True:
        try:
            jawaban = input(pesan).strip().lower()
            if jawaban not in ("y", "ya", "t", "tidak"):
                raise ValueError("Jawab y/ya atau t/tidak!")
        except ValueError as error:
            print(error)
        else:
            return jawaban == "y" or jawaban == "ya"
        


def update_game(user_data):
    clear()
    judul(" UPDATE DATA GAME ")
    history = user_data["history_catat"]
    
    if len(history) == 0:
        print("Belum ada data untuk diubah.")
        jeda()
        return
    
    tampil_daftar_game(history)
    nomor = pilih_nomor_game(history, "diubah")
    
    if nomor is None:
        return

    data_lama_sementara = history[nomor]

    data_baru_sementara = data_lama_sementara.copy()
    
    print(f"\nMengubah Game #{nomor}")
    if konfirmasi(f"Ganti Map ({data_lama_sementara['map']})? (y/t): "):
        data_baru_sementara["map"] = input_map()
        
    if konfirmasi(f"Ganti Agent ({data_lama_sementara['agent']})? (y/t): "):
        data_baru_sementara["agent"] = input_agent()
    
    if konfirmasi(f"Ganti Score ({data_lama_sementara['round_w']}-{data_lama_sementara['round_l']})? (y/t): "):
        data_baru_sementara["round_w"], data_baru_sementara["round_l"] = input_score()
        data_baru_sementara["hasil"] = tentukan_hasil(data_baru_sementara["round_w"], data_baru_sementara["round_l"])
    
    if konfirmasi(f"Ganti KDA ({data_lama_sementara['kill']}/{data_lama_sementara['death']}/{data_lama_sementara['assist']})? (y/t): "):
        data_baru_sementara["kill"], data_baru_sementara["death"], data_baru_sementara["assist"] = input_kda()
    
    if data_baru_sementara["hasil"] != data_lama_sementara["hasil"]:
        print(f"Hasil berubah {data_lama_sementara['hasil']} menjadi {data_baru_sementara['hasil']}; RR wajib diisi ulang.")
        data_baru_sementara["rr"] = input_rr(data_baru_sementara["hasil"])
    
    elif konfirmasi(f"Ganti RR ({data_lama_sementara['rr']:+})? (y/t): "):
        data_baru_sementara["rr"] = input_rr(data_baru_sementara["hasil"])

    print("\n--- RINGKASAN DATA YANG DIPERBARUI ---")
    print(f"Map: {data_baru_sementara['map']} | Agent: {data_baru_sementara['agent']}")
    print(f"Score: {data_baru_sementara['round_w']}-{data_baru_sementara['round_l']} ({data_baru_sementara['hasil']})")
    print(f"KDA: {data_baru_sementara['kill']}/{data_baru_sementara['death']}/{data_baru_sementara['assist']} | RR: {data_baru_sementara['rr']:+}")
    
    if konfirmasi("Simpan perubahan? (y/t): "):
        history[nomor] = data_baru_sementara
        print("Data game berhasil diupdate")
    else:
        print("Perubahan dibatalkan.")
    jeda()


def hapus_game(user_data):
    clear()
    judul(" HAPUS DATA GAME ")
    history = user_data["history_catat"]
    if len(history) == 0:
        print("Belum ada data untuk dihapus.")
        jeda()
        return
    
    tampil_daftar_game(history)
    nomor = pilih_nomor_game(history, "dihapus")
    
    if nomor is None:
        return
    if konfirmasi(f"Yakin hapus Game #{nomor}? (y/t): "):
        del history[nomor]
        history_data_baru_sementara = {}
        nomor_baru = 1
        
        for data in history.values():
            history_data_baru_sementara[nomor_baru] = data
            nomor_baru += 1
        user_data["history_catat"] = history_data_baru_sementara
        print("Data game berhasil dihapus!")
    else:
        print("Hapus data dibatalkan.")
    jeda()

def hitung_rank_rr(user_data):
    rank = user_data["rank"]
    rr = user_data["rr_awal"]
    for match in user_data["history_catat"].values():
        rr += match["rr"]
        while rr >= 100 and rank < len(daftar_rank):
            rr -= 100
            rank += 1
        while rr < 0 and rank > 1:
            rr += 100
            rank -= 1
        if rank == 1 and rr < 0:
            rr = 0
    return rank, rr


def statistik(user_data):
    clear()
    judul(" REKAPITULASI STATISTIK PERFORMA ")
    history = user_data["history_catat"]
    if len(history) == 0:
        print("Belum ada data rekap untuk dihitung.")
        jeda()
        return

    total_game = hitung_total_game(list(history.keys()))
    menang = kalah = seri = 0
    sum_k = sum_d = sum_a = 0
    map_hitung = {}
    agent_hitung = {}
    pertama = True
    kda_terbesar = {}
    kda_terendah = {}
    map_kda_tertinggi = {}
    map_kda_terdikit = {}

    for match in history.values():
        if match["hasil"] == "W":
            menang += 1
        elif match["hasil"] == "L":
            kalah += 1
        else:
            seri += 1
            
        sum_k += match["kill"]
        sum_d += match["death"]
        sum_a += match["assist"]
        teks_map = f"Map {match['map']} (Agent {match['agent']})"
        
        for key_kda in ("kill", "death", "assist"):
            if pertama or match[key_kda] > kda_terbesar[key_kda]:
                kda_terbesar[key_kda] = match[key_kda]
                map_kda_tertinggi[key_kda] = teks_map
            if pertama or match[key_kda] < kda_terendah[key_kda]:
                kda_terendah[key_kda] = match[key_kda]
                map_kda_terdikit[key_kda] = teks_map
        pertama = False
        map_hitung[match["map"]] = map_hitung.get(match["map"], 0) + 1
        agent_hitung[match["agent"]] = agent_hitung.get(match["agent"], 0) + 1


    map_tersering = ""
    max_map = 0
    for nama, jumlah in map_hitung.items():
        if jumlah > max_map:
            max_map = jumlah
            map_tersering = nama
            
    agent_tersering = ""
    max_agent = 0
    for nama, jumlah in agent_hitung.items():
        if jumlah > max_agent:
            max_agent = jumlah
            agent_tersering = nama

    rank, rr = hitung_rank_rr(user_data)
    if rank == len(daftar_rank):
        rr_butuh = "Sudah rank tertinggi (Radiant)"
    else:
        rr_butuh = f"{100 - rr} RR lagi menuju {daftar_rank[rank + 1]}"

    print(f"Total Game Dimainkan    : {total_game}")
    print(f"Menang / Kalah / Seri   : {menang} / {kalah} / {seri}")
    print(f"Total KDA               : {sum_k} / {sum_d} / {sum_a}")
    print(f"Rata-rata KDA per Game  : {sum_k/total_game:.1f} / {sum_d/total_game:.1f} / {sum_a/total_game:.1f}")
    for key_kda, label in (("kill", "Kill"), ("death", "Death"), ("assist", "Assist")):
        print(f"{label} Terbanyak          : {kda_terbesar[key_kda]} ({map_kda_tertinggi[key_kda]})")
        print(f"{label} Terdikit           : {kda_terendah[key_kda]} ({map_kda_terdikit[key_kda]})")
    print(f"Map Paling Sering Main  : {map_tersering} ({max_map}x)")
    print(f"Agent Paling Sering     : {agent_tersering} ({max_agent}x)")
    print(f"Rank Saat Ini           : {daftar_rank[rank]} (RR: {rr})")
    print(f"Sisa RR Menuju Rank Naik: {rr_butuh}")
    jeda()


def menu_crud(user_data):
    while True:
        clear()
        tampil_menu_crud()
        pilihan = input_angka("Pilih menu (1-6): ", 1, 6)
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
        data_performa[username] = {"rank": 1, "rr_awal": 0, "rank_sudah_diisi": False, "history_catat": {}}
        
    user_data = data_performa[username]
    while True:
        clear()
        tampil_menu_user(username)
        pilihan = input_angka("Pilih menu (1-3): ", 1, 3)
        if pilihan == 1:
            catat_game(user_data)
            menu_crud(user_data)
        elif pilihan == 2:
            menu_crud(user_data)
        else:
            break
        
        

def main():
    clear()
    print("Selamat datang di VlaoTracker!")
    print('''Halo, halo, Selamat Pagi, Hidup Mahasiswa, Hidup Rakyat Indonesia, Hidup Perempuan Yang Melawan, Hidup Teknik! Selamat datang di program paling epik abad ini: VLAOTRACKER 

Dibuat sebelum menuju TA huhuhuhu, secangkir esteh yang membuat semangat sebentar, dan dipersembahkan untuk aslab:
-> NLG'25 (068) (Ketua)
-> R'25   (106)
-> SNA'25 (016)
-> YAP'25 (017)
Well... Well... Well. B1 misi cobain semua Aslab :D 

Program ini didedikasikan buat nilai 100 dan menambah pengetahuan.

Intinya: Catat performa, tampilin stat. 
semoga lulus posttest, dan jangan lupa senyum ya Aslab Aslab Aslab Aslab sibuk banget kaya \033[9mpenjabat\033[0m guah (ermmm ini dari stiker btw bukan saya yang ngomong :D) Yey! 🎉
time to lock in''')
    jeda()
    while True:
        clear()
        tampil_menu_awal()
        pilihan = input_angka("Pilih menu (1-4): ", 1, 4)
        if pilihan == 1:
            username = login("admin")
            if username is not None:
                menu_admin(username)
        elif pilihan == 2:
            username = login("user")
            if username is not None:
                menu_user(username)
        elif pilihan == 3:
            register()
        else:
            print("Terima kasih sudah menggunakan VlaoTracker!")
            break


if __name__ == "__main__":
    main()
