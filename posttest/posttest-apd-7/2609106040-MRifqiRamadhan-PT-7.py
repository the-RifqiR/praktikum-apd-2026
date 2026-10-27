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
        username = input_teks("Masukkan username baru: ")
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
    username = input_teks("Username: ")
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
    nama_data_baru_sementara = input_teks("Masukkan nama map data_baru_sementara: ")
    for nama_map in daftar_map:
        if nama_map.lower() == nama_data_baru_sementara.lower():
            print("Map sudah terdaftar!")
            jeda()
            return
    daftar_map[nama_data_baru_sementara] = True
    print(f"Map '{nama_data_baru_sementara}' berhasil ditambahkan.")
    jeda()
    
def tambah_agent():
    clear()
    judul(" TAMBAH AGENT ")
    role = pilih_dari_dictionary(agents, "Pilih nomor role: ")
    nama_data_baru_sementara = input_teks("Masukkan nama agent data_baru_sementara: ")
    for nama_role, daftar_agent in agents.items():
        for nama_agent in daftar_agent:
            if nama_agent.lower() == nama_data_baru_sementara.lower():
                print(f"Agent sudah terdaftar pada role {nama_role}!")
                jeda()
                return
    agents[role][nama_data_baru_sementara] = True
    print(f"Agent '{nama_data_baru_sementara}' berhasil ditambahkan ke {role}.")
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
def pilih_dari_dictionary(data, pesan):
    pilihan = {}
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

def input_map():
    print("\nDaftar Map:")
    return pilih_dari_dictionary(daftar_map, "Pilih nomor map: ")


def input_agent():
    print("\nPilih Role Agent:")
    role = pilih_dari_dictionary(agents, "Pilih nomor role: ")
    print(f"\nDaftar Agent {role}:")
    return pilih_dari_dictionary(agents[role], "Pilih nomor agent: ")

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

def input_data_game():
    nama_map = input_map()
    nama_agent = input_agent()
    round_w, round_l = input_score()
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
        # Cari nomor kda_terbesar agar nomor game tidak menimpa data data_lama_sementara.
        nomor_data_baru_sementara = 1
        if len(history) > 0:
            nomor_data_baru_sementara = max(history.keys()) + 1
        history[nomor_data_baru_sementara] = data
    print("\nSemua data game berhasil dicatat!")
    jeda()

def menu_crud(user_data):
    while True:
        clear()
        tampil_menu_crud()
        pilihan = input_angka("Pilih menu (1-6): ", 1, 6)
        if pilihan == 1:
            break
        elif pilihan == 2:
            catat_game(user_data)
        elif pilihan == 3:
            break
        elif pilihan == 4:
            break
        elif pilihan == 5:
            break
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
-> YPA'25 (049)
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
