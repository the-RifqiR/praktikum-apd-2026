import os
accounts = {
    "adminvlao" : {
        "password" : "admin123",
        "role" : "admin",
        },
    "aja" : {
        "password" : "041",
        "role" : "user",
        },
    "mbarisma" : {
        "password" : "106",
        "role" : "user",
        },
}

daftar_rank = {
    1: "Iron",
    2: "Bronze",
    3: "Silver",
    4: "Gold",
    5: "Platinum",
    6: "Diamond",
    7: "Ascendant",
    8: "Immortal",
    9: "Radiant",
}

daftar_map = {
    "Ascent": True,
    "Bind": True,
    "Haven": True,
    "Split": True,
    "Lotus": True,
    "Sunset": True,
    "Abyss": True,
    "Corrode": True,
    "Icebox": True,
    "Summit": True,
    "Pearl": True,
    "Fracture": True,
    "Breeze": True,
}

agents = {
    "Duelist": {"Jett": True, "Phoenix": True, "Raze": True, "Reyna": True, "Yoru": True, "Neon": True, "Iso": True, "Waylay": True, "Hush": True},
    "Initiator": {"Breach": True, "Sova": True, "Skye": True, "Kayo": True, "Fade": True, "Gekko": True, "Tejo": True},
    "Controller": {"Brimstone": True, "Omen": True, "Viper": True, "Astra": True, "Harbor": True, "Clove": True, "Miks": True},
    "Sentinel": {"Sage": True, "Cypher": True, "Killjoy": True, "Chamber": True, "Deadlock": True, "Vyse": True},
}

data_performa = {}

bintang = "=" * 45
os.system("cls" if os.name == "nt" else "clear")
# Nama Programnya VlaoTracker, Apa? Typo? Engga memang gitu namanya. Coba aja ketik Valo cepat cepat lewat keyboard layout hp
print('''=====================================================
Halo, halo, Selamat Pagi, Hidup Mahasiswa, Hidup Rakyat Indonesia, Hidup Perempuan Yang Melawan, Hidup Teknik! Selamat datang di program paling epik 
abad ini: VLAOTRACKER 

Dibuat dengan sepenuh hati, secangkir kopi, dan 
sedikit kepanikan (bohong aja padahal panik banget, duh gusti) demi menyelesaikan posttest 
tercinta dari Kakak-kakak....eh salah ya, maksudnya Abang dan Mba Aslab kelas B1 paling 
keren sejagat raya bumi antero galaxy:
-> NLG'25 (068)
-> R'25   (106)
-> SNA'25 (016)
Kesamaannya apa adik adik? benar, sama-sama akt 2025 absennya ada 6, wait... 666 wah well well well
(Ijin tampil)

Program ini didedikasikan buat para pejuang 
Ranked Valorant yang mau nge-track performa 
tanpa kesalahan berfikir, dan tentunya sudah disesuaikan (ekspetasinya tolong dijaga) 
dengan jalur hukum tiba tiba diganti jadi "Dictionary"  biar aman 
sentosa waktu diperiksa (ini mah.. keburu diangkat saber).
NAH INI BARU
MY KARYA GUWEH

Intinya: Catat performa, tampilin stat. 
semoga lulus posttest, dan jangan lupa senyum ya Aslab Aslab Aslab Aslab sibuk banget kaya \033[9mpenjabat\033[0m guah (ermmm ini dari stiker btw bukan saya yang ngomong :D) Yey! 🎉
time to lock in
=====================================================''')
input("Enter Kalau Gak Mau Baca Yappingan")  
print(f"{bintang}")

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(bintang)
    print(" SELAMAT DATANG DI VLAOTRACKER ".center(45, "="))
    print(bintang)
    print("1. Admin")
    print("2. Lu Member")
    print("3. Belum Punya Akun? (Register)")
    print("4. Keluar Program")
    print(bintang)
    while True:
        menu_awal = input("Pilih menu (1-4): ").strip()
        
        if menu_awal == "":
            print("DIISI KOCAK NGAPAIN INPUT KOSONG???")
        elif not menu_awal.isdigit():
            print("Input harus berupa angka!")
        else:
            menu_awal = int(menu_awal)
            if menu_awal < 1 or menu_awal > 4:
                print("Masukan Yang Benar-Benar Aja lah (1/2/3/4)")
            else:
                break
            
    if menu_awal == 4:
        print("\nTerima kasih sudah menggunakan VlaoTracker")
        break
    
    elif menu_awal == 3:
        os.system("cls" if os.name == "nt" else "clear")
        print(bintang)
        print(" REGISTER AKUN BARU ".center(45, "="))
        print(bintang)
        
        while True:
            new_username = input("Masukan Username baru: ")
            # Cek duplikasi username
            sudah_ada = False
            for acc in accounts:
                if acc == new_username:
                    sudah_ada = True
                    
            if new_username == "":
                print("Username tidak boleh kosong!")
            elif sudah_ada:
                print("Username sudah terdaftar")
            else:
                break
                
        while True:
            new_password = input("Masukan Password baru: ")
            if new_password == "":
                print("Password tidak boleh kosong!")
            else:
                break
                
        accounts.update({new_username : {
            "password" : new_password,
            "role" : "user",
        }})
        print("Registrasi Berhasil, Silakan Login.")
        input("Tekan ENTER untuk kembali...")
        continue
    
    os.system("cls" if os.name == "nt" else "clear")
    if menu_awal == 1:
        print(" LOGIN ADMIN ".center(45, "="))
        target_role = "admin"
    else:
        print(" LOGIN PENGGUNA ".center(45, "="))
        target_role = "user"    
        
    inputUsername = input("Username: ")
    inputPassword = input("Password: ")
    
    login_sukses = False
    daftar_akun = accounts[inputUsername]
    
    # kalau username sama dan password sama dan role sama maka masuk
    if daftar_akun is not None and inputPassword == daftar_akun.get("password") and target_role == daftar_akun.get("role"):
        login_sukses = True
        
    if not login_sukses:
        print("\n\033[91mLogin Gagal, Username atau Password salah.\033[0m")
        input("Tekan ENTER untuk kembali...")
        continue
        
    if target_role == "admin":
        while True:
            os.system("cls" if os.name == "nt" else "clear") 
            print(bintang)
            print(f" SELAMAT DATANG ADMIN ({inputUsername}) ".center(45, "="))
            print(bintang)
            print("1. Tambah Map Baru")
            print("2. Tambah Agent Baru")
            print("3. Lihat Rekap Pengguna")
            print("4. Logout (Kembali ke Beranda)")
            print(bintang)
            
            inputPilih = input("Pilih menu (1-4): ").strip()
            
            if inputPilih == "":
                print("Input tidak boleh kosong")
                input("\nTekan ENTER untuk lanjut...")
                
            elif not inputPilih.isdigit():
                print("Input harus angka")
                input("\nTekan ENTER untuk lanjut...")
                
            elif inputPilih == "1":
                os.system("cls" if os.name == "nt" else "clear")
                
                print("=== TAMBAH MAP ===")
                map_baru = input("Masukkan nama map baru: ").strip()
                map_sudah_ada = False
                
                for nama_map in daftar_map:
                    if nama_map.upper() == map_baru.upper():
                        map_sudah_ada = True
                if map_baru == "":
                    print("Nama map tidak boleh kosong!")
                elif map_sudah_ada:
                    print("Map tersebut sudah terdaftar!")
                else:
                    daftar_map[map_baru] = True
                    print(f"\nMap '{map_baru}' berhasil tambah")
                input("\nTekan ENTER untuk lanjut...")
                
            elif inputPilih == "2":
                os.system("cls" if os.name == "nt" else "clear")
                
                print("=== TAMBAH AGENT ===")
                print("Pilih Role Agent: ")
                pilihan_role = {}
                nomor = 1
                for nama_role in agents:
                    pilihan_role[nomor] = nama_role
                    print(f"{nomor}. {nama_role}")
                    nomor += 1
                
                input_role = input("Pilih nomor role (1-4): ").strip()
                if input_role.isdigit() and int(input_role) in pilihan_role:
                    nama_role = pilihan_role[int(input_role)]
                    
                    agent_baru = input(f"Masukkan nama agent untuk {nama_role}: ").strip()
                    agent_sudah_ada = False
                
                    for idx_nama_agent in agents[nama_role]:
                        if idx_nama_agent.upper() == agent_baru.upper():
                            agent_sudah_ada = True
                    if agent_baru == "":
                        print("Nama agent tidak boleh kosong!")
                    elif agent_sudah_ada:
                        print("Agent tersebut sudah terdaftar pada role ini!")
                    else:
                        agents[nama_role][agent_baru] = True
                        print(f"\nAgent '{agent_baru}' berhasil tambah")
                else:
                    print("\nPilihan role gak ada")
                input("\nTekan ENTER untuk lanjut...")

            elif inputPilih == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== REKAP PERFORMA SEMUA PENGGUNA ===\n")
                if len(data_performa) == 0:
                    print("Belum ada data rekap performa dari user.")
                else:
                    for username, data_user in data_performa.items():
                        print(f"Username: {username} | Total Game Tercatat: {len(data_user['history_catat'])}")
                input("\nTekan ENTER untuk lanjut...")
                
            elif inputPilih == "4":
                break
            else:
                print("Pilihan gak ada")
                input("Tekan ENTER...")
                
    elif target_role == "user":
        # akun ini punya data?
        if inputUsername not in data_performa:
            data_performa[inputUsername] = {
                "rank" : 1,
                "rr_awal" : 0,
                "history_catat" : {}
            }

        user_data = data_performa[inputUsername]
        langsung_ke_crud = False
        
        while True:
            if langsung_ke_crud:
                inputUserMenu = "2"
                langsung_ke_crud= False
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(bintang)
                print(f" DASHBOARD USER ({inputUsername}) ".center(45, "="))
                print(bintang)
                print("1. Catat Performa Game Baru")
                print("2. Menu Kelola & Statistik Performa (CRUD)")
                print("3. Logout (Kembali ke Beranda)")
                print(bintang)

                inputUserMenu = input("Pilih menu (1-3): ").strip()

            if inputUserMenu == "1":
                os.system("cls" if os.name == "nt" else "clear")
                
                print("=== PENCATATAN PERFORMA VALORANT DI VLAOTRACKER ===\n")
                # Input jumlah game
                while True:
                    jumlah_gim = input("Masukkan jumlah game yang ingin dicatat: ").strip()
                    if jumlah_gim.isdigit() and int(jumlah_gim) > 0:
                        jumlah_gim = int(jumlah_gim)
                        break
                    print("Masukkan angka bulat positif!")
                    
                if len(user_data["history_catat"]) == 0:
                    while True:
                        print("\nPilih Rank Saat Ini:")
                        # daftarnya
                        for nomor, nama_rank in daftar_rank.items():
                            print(f"{nomor}. {nama_rank}")
                        
                        # inputnya
                        inputRank = input("Pilih nomor rank (1-9): ").strip()
                        if inputRank.isdigit() and 1 <= int(inputRank) <= len(daftar_rank):
                            user_data["rank"] = int(inputRank)
                            break
                        print("Pilihan tidak valid!")
                    rank_awal_user = user_data["rank"]
                    rank_tertinggi = len(daftar_rank)
                    while True:
                        if rank_awal_user == rank_tertinggi:
                            input_rr_awal = input("Masukkan RR saat ini (minimal 0, tanpa batas atas): ").strip()
                        else:
                            input_rr_awal = input("Masukkan RR saat ini (0-99): ").strip()
                            
                        if input_rr_awal == "":
                            print("RR tidak boleh kosong!")
                        elif not input_rr_awal.isdigit():
                            print("RR harus berupa angka bulat dan tidak boleh negatif!")
                        elif rank_awal_user != rank_tertinggi and int(input_rr_awal) > 99:
                            print("RR maksimal 99! RR 100 ke atas hanya untuk rank Radiant.")
                        else:
                            user_data["rr_awal"] = int(input_rr_awal)
                            break
                        
                for gim in range(jumlah_gim):
                    print(f"\n--- GAME KE-{gim + 1} DARI {jumlah_gim} ---")
                    # daftar map
                    pilihan_map = {}
                    nomor_map = 1
                    print("\nDaftar Map:")
                    for nama_map in daftar_map:
                        pilihan_map[nomor_map] = nama_map
                        print(f"{nomor_map}. {nama_map}")
                        nomor_map += 1
                        
                    # input map
                    while True:
                        inputMap = input("Pilih nomor map: ").strip()
                        if inputMap.isdigit() and int(inputMap) in pilihan_map:
                            nama_map_terpilih = pilihan_map[int(inputMap)]
                            break
                        print("Nomor map tidak valid!")
                    # ==========    ============================================== 
                    # daftarnya
                    print("\nPilih Role Agent:")
                    pilihan_role = {}
                    nomor_role = 1
                    
                    for nama_role in agents:
                        pilihan_role[nomor_role] = nama_role
                        print(f"{nomor_role}. {nama_role}")
                        nomor_role += 1
                        
                    # inputnya
                    while True:
                        input_role = input("Pilih nomor role (1-4): ").strip()
                        if input_role.isdigit() and int(input_role) in pilihan_role:
                            role_agent = pilihan_role[int(input_role)]
                            break
                        print("Role tidak valid!")
                    # ==========    ======================================================
                        # daftar
                    pilihan_agent = {}
                    nomor_agent = 1
                    print(f"\nDaftar Agent Role {role_agent}:")
                    for idx_nama_agent in agents[role_agent]:
                        pilihan_agent[nomor_agent] = idx_nama_agent
                        print(f"{nomor_agent}. {idx_nama_agent}")
                        nomor_agent += 1
                    
                    # inputnya
                    while True:
                        pilihAgent = input("Pilih nomor agent: ").strip()
                        if pilihAgent.isdigit() and int(pilihAgent) in pilihan_agent:
                            nama_agent_terpilih = pilihan_agent[int(pilihAgent)]
                            break
                        print("Nomor agent tidak valid!")
                    # ==========    ======================================================
                    while True:
                        round_w = input("Jumlah Round Menang (Win Round): ").strip()
                        round_l = input("Jumlah Round Kalah (Lose Round): ").strip()
                        if round_w.isdigit() and round_l.isdigit():
                            round_w = int(round_w)
                            round_l = int(round_l)
                            break
                        print("Score round harus berupa angka!")
                    # Tentukan hasil otomatis (W / L / T)
                    if round_w > round_l:
                        hasil = "W"
                    elif round_l > round_w:
                        hasil = "L"
                    else:
                        hasil = "T"
                    # 6. Input KDA
                    while True:
                        k = input("Total Kill: ").strip()
                        d = input("Total Death: ").strip()
                        a = input("Total Assist: ").strip()
                        if k.isdigit() and d.isdigit() and a.isdigit():
                            k, d, a = int(k), int(d), int(a)
                            break
                        print("KDA harus berupa angka!")
                   
                    while True:
                        if hasil == "W":
                            inputRR = input("RR Yang Didapat, tanpa simbol (+/-): ").strip()
                        elif hasil == "L":    
                            inputRR = input("RR Yang Didapat, tanpa simbol (+/-): ").strip()
                        else:
                            inputRR = input("RR Yang Didapat: ").strip()
                            
                        if inputRR == "":
                            print("Gak boleh kosong")
                        elif hasil != "T" and not inputRR.isdigit():
                            print("Hanya angka")
                        elif hasil == "T" and not (inputRR.isdigit() or (inputRR.startswith("-") and inputRR[1:].isdigit())):
                            print("Format salah")
                        elif hasil != "T" and int(inputRR) == 0:
                            print("Lah memangnya RR gak + atau - 🐧? minimal 1 RR lah")
                        else:
                            break
                    
                    if hasil == "W":
                        rr_change = int(inputRR)
                    elif hasil == "L":
                        rr_change = -int(inputRR)
                    else:
                        rr_change = int(inputRR)

                    match_item = {  "map": nama_map_terpilih, "agent": nama_agent_terpilih, "round_w": round_w, "round_l": round_l, "hasil": hasil, "kill": k, "death": d, "assist": a, "rr": rr_change}
                    user_data["history_catat"][len(user_data["history_catat"]) + 1] = match_item
                    
                print("\n\033[92mSemua data Game berhasil dicatat!\033[0m")
                input("Tekan ENTER untuk kembali...")
                langsung_ke_crud = True
                
            elif inputUserMenu == "2":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(bintang)
                    print(" KELOLA & STATISTIK PERFORMA ".center(45, "="))
                    print(bintang)
                    print("1. Lihat Data Per Game (List Game)")
                    print("2. Tambah Data Game")
                    print("3. Update Data Game")
                    print("4. Delete (Hapus) Data Game")
                    print("5. Lihat Statistik & Rekap Lengkap")
                    print("6. Kembali ke Dashboard")
                    print(bintang)
                    pilih_crud = input("Pilih menu (1-6): ").strip().lower()
                    
                    # variabelnya nampung data pergame
                    user_matches = user_data["history_catat"]
                    
                    if pilih_crud == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== DAFTAR GAME TERCATAT ===\n")
                        if len(user_matches) == 0:
                            print("Belum ada data Game yang dimasukkan.")
                        else:
                            for nomor, match in user_matches.items():
                                print(f"Game #{nomor} | Map: {match['map']} | Agent: {match['agent']} | Hasil: {match['hasil']} ({match['round_w']}-{match['round_l']}) | KDA: {match['kill']}/{match['death']}/{match['assist']} | RR: {match['rr']}")
                        input("\nTekan ENTER untuk kembali...")
                      
                    elif pilih_crud == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print(bintang)
                        print("MENU TAMBAH DATA GAME")
                        print(bintang + "\n")
                        if len(user_matches) == 0:
                            print("Belum ada data Game")
                        else:
                            while True:
                                jumlah_gim = input("Masukkan jumlah game yang ingin dicatat: ").strip()
                                if jumlah_gim.isdigit() and int(jumlah_gim) > 0:
                                    jumlah_gim = int(jumlah_gim)
                                    break
                                print("Masukkan angka bulat positif!")

                            for gim in range(jumlah_gim):
                                print(f"\n--- GAME KE-{gim + 1} DARI {jumlah_gim} ---")
                                # daftar map
                                pilihan_map = {}
                                nomor_map = 1
                                print("\nDaftar Map:")
                                for nama_map in daftar_map:
                                    pilihan_map[nomor_map] = nama_map
                                    print(f"{nomor_map}. {nama_map}")
                                    nomor_map += 1

                                # input map
                                while True:
                                    inputMap = input("Pilih nomor map: ").strip()
                                    if inputMap.isdigit() and int(inputMap) in pilihan_map:
                                        nama_map_terpilih = pilihan_map[int(inputMap)]
                                        break
                                    print("Nomor map tidak valid!")
                                # ==========    ============================================== 
                                # daftarnya
                                print("\nPilih Role Agent:")
                                pilihan_role = {}
                                nomor_role = 1

                                for nama_role in agents:
                                    pilihan_role[nomor_role] = nama_role
                                    print(f"{nomor_role}. {nama_role}")
                                    nomor_role += 1

                                # inputnya
                                while True:
                                    input_role = input("Pilih nomor role (1-4): ").strip()
                                    if input_role.isdigit() and int(input_role) in pilihan_role:
                                        role_agent = pilihan_role[int(input_role)]
                                        break
                                    print("Role tidak valid!")
                                # ==========    ======================================================
                                    # daftar
                                pilihan_agent = {}
                                nomor_agent = 1
                                print(f"\nDaftar Agent Role {role_agent}:")
                                for idx_nama_agent in agents[role_agent]:
                                    pilihan_agent[nomor_agent] = idx_nama_agent
                                    print(f"{nomor_agent}. {idx_nama_agent}")
                                    nomor_agent += 1

                                # inputnya
                                while True:
                                    pilihAgent = input("Pilih nomor agent: ").strip()
                                    if pilihAgent.isdigit() and int(pilihAgent) in pilihan_agent:
                                        nama_agent_terpilih = pilihan_agent[int(pilihAgent)]
                                        break
                                    print("Nomor agent tidak valid!")
                                # ==========    ======================================================
                                while True:
                                    round_w = input("Jumlah Round Menang (Win Round): ").strip()
                                    round_l = input("Jumlah Round Kalah (Lose Round): ").strip()
                                    if round_w.isdigit() and round_l.isdigit():
                                        round_w = int(round_w)
                                        round_l = int(round_l)
                                        break
                                    print("Score round harus berupa angka!")
                                # Tentukan hasil otomatis (W / L / T)
                                if round_w > round_l:
                                    hasil = "W"
                                elif round_l > round_w:
                                    hasil = "L"
                                else:
                                    hasil = "T"
                                # 6. Input KDA
                                while True:
                                    k = input("Total Kill: ").strip()
                                    d = input("Total Death: ").strip()
                                    a = input("Total Assist: ").strip()
                                    if k.isdigit() and d.isdigit() and a.isdigit():
                                        k, d, a = int(k), int(d), int(a)
                                        break
                                    print("KDA harus berupa angka!")

                                while True:
                                    if hasil == "W":
                                        inputRR = input("RR Yang Didapat, tanpa simbol (+/-): ").strip()
                                    elif hasil == "L":    
                                        inputRR = input("RR Yang Didapat, tanpa simbol (+/-): ").strip()
                                    else:
                                        inputRR = input("RR Yang Didapat: ").strip()

                                    if inputRR == "":
                                        print("Gak boleh kosong")
                                    elif hasil != "T" and not inputRR.isdigit():
                                        print("Hanya angka")
                                    elif hasil == "T" and not (inputRR.isdigit() or (inputRR.startswith("-") and inputRR[1:].isdigit())):
                                        print("Format salah")
                                    elif hasil != "T" and int(inputRR) == 0:
                                        print("Lah memangnya RR gak + atau - 🐧? minimal 1 RR lah")
                                    else:
                                        break
                                    
                                if hasil == "W":
                                    rr_change = int(inputRR)
                                elif hasil == "L":
                                    rr_change = -int(inputRR)
                                else:
                                    rr_change = int(inputRR)

                                match_item = {  "map": nama_map_terpilih, "agent": nama_agent_terpilih, "round_w": round_w, "round_l": round_l, "hasil": hasil, "kill": k, "death": d, "assist": a, "rr": rr_change}
                                user_data["history_catat"][len(user_data["history_catat"]) + 1] = match_item
                                
                            print("\n\033[92mSemua data Game berhasil dicatat!\033[0m")
                        input("Tekan ENTER untuk kembali...")
                        
                    elif pilih_crud == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== UPDATE DATA GAME ===\n")
                        if len(user_matches) == 0:
                            print("Belum ada data untuk di Edit")
                            input("\nTekan ENTER untuk kembali...")
                            continue
                        
                        for nomor, match in user_matches.items():
                            print(f"{nomor}. Map: {match['map']}")
                            print(f"   Agent: {match['agent']}")
                            print(f"   Score: {match['round_w']}-{match['round_l']}")
                            print(f"   Hasil: {match['hasil']}")
                            print(f"   KDA: {match['kill']}/{match['death']}/{match['assist']}")
                            print(f"   RR: {match['rr']:+}")                            
                            
                        while True:        
                            input_nomor = input("\nMasukkan nomor game yang ingin diubah (atau 'kembali'): ").strip().lower()
                            if input_nomor == "kembali":
                                print("\nUpdate dibatalkan")
                                break
                            elif input_nomor.isdigit():
                                nomor_game = int(input_nomor)
                                if nomor_game in user_matches:
                                    break
                                else:
                                    print("Data game gk ada")
                            else:
                                print("Masukan nomor yang valid atau ketik kembali")
                        
                        if input_nomor == "kembali":
                            continue
                            
                        match = user_matches[nomor_game]
                        print("\n=== DETAIL GAME YANG DIPILIH ===")
                        print(f"Map   : {match['map']}")
                        print(f"Agent : {match['agent']}")
                        print(f"Score : {match['round_w']}-{match['round_l']}")
                        print(f"Hasil : {match['hasil']}")
                        print(f"KDA   : {match['kill']}/{match['death']}/{match['assist']}")
                        print(f"RR    : {match['rr']:+}")
                        map_baru = match["map"]
                        baru_agent = match["agent"]
                        round_w_baru = match["round_w"]
                        round_l_baru = match["round_l"]
                        hasilBaru = match["hasil"]
                        kill_baru = match["kill"]
                        death_baru = match["death"]
                        assist_baru = match["assist"]
                        rr_baru = match["rr"]
                        
                        print("\nMasukkan data baru:")
                        while True:
                            jawab = input(f"\nGanti Map? (sekarang: {match['map']}) (y/t): ").strip().lower()
                            if jawab in ("y", "ya", "t", "tidak"):
                                    break
                            print("Jawab dengan y/ya atau t/tidak!")
                        if jawab == "y" or jawab == "ya":    
                            print("\nDaftar Map:")
                            pilihan_map = {}
                            nomor_map = 1
                            for nama_map_tersedia in daftar_map:
                                pilihan_map[nomor_map] = nama_map_tersedia
                                print(f"{nomor_map}. {nama_map_tersedia}")
                                nomor_map += 1
                                
                            while True:
                                input_map_baru = input("Pilih nomor map baru: ").strip()
                                if input_map_baru.isdigit() and int(input_map_baru) in pilihan_map:
                                    map_baru = pilihan_map[int(input_map_baru)]
                                    break
                                print("Nomor map tidak valid!")
                                
                        while True:
                            jawab = input(f"\nGanti Agent? (sekarang: {match['agent']}) (y/t): ").strip().lower()
                            if jawab in ("y", "ya", "t", "tidak"):
                                    break
                            print("Jawab dengan y/ya atau t/tidak!")
                        if jawab == "y" or jawab == "ya":
                            pilihan_role = {}
                            nomor_role = 1
                            print("\nDaftar Role:")
                            for nama_role in agents:
                                pilihan_role[nomor_role] = nama_role
                                print(f"{nomor_role}. {nama_role}")
                                nomor_role += 1
                                
                            while True:
                                input_role_baru = input("Pilih nomor role agent: ").strip()
                                if input_role_baru.isdigit() and int(input_role_baru) in pilihan_role:
                                    role_agent = pilihan_role[int(input_role_baru)]
                                    break
                                print("Nomor role tidak valid!")
                            pilihan_agent = {}
                            nomor_agent = 1

                            print(f"\nDaftar Agent {role_agent}:")
                            for nama_agent in agents[role_agent]:
                                pilihan_agent[nomor_agent] = nama_agent
                                print(f"{nomor_agent}. {nama_agent}")
                                nomor_agent += 1
                            while True:
                                pilih_agent_baru = input("Pilih nomor agent baru: ").strip()
                                if pilih_agent_baru.isdigit() and int(pilih_agent_baru) in pilihan_agent:
                                    baru_agent = pilihan_agent[int(pilih_agent_baru)]
                                    break
                                print("Nomor agent tidak valid!")

                        while True:
                            jawab = input(f"\nGanti Score? (sekarang: {match['round_w']}-{match['round_l']}) (y/t): ").strip().lower()
                            if jawab in ("y", "ya", "t", "tidak"):
                                    break
                            print("Jawab dengan y/ya atau t/tidak!")
                        if jawab == "y" or jawab == "ya":
                            while True:
                                input_baru_round_w = input("Jumlah Round Menang baru: ").strip()
                                input_baru_round_l = input("Jumlah Round Kalah baru: ").strip()
                                if input_baru_round_w.isdigit() and input_baru_round_l.isdigit():
                                    round_w_baru = int(input_baru_round_w)
                                    round_l_baru = int(input_baru_round_l)
                                    break
                                print("Jumlah round harus berupa angka bulat positif atau 0!")
                                
                            if round_w_baru > round_l_baru:
                                hasilBaru = "W"
                            elif round_w_baru < round_l_baru:
                                hasilBaru = "L"
                            else:
                                hasilBaru = "T"
                        while True:
                            jawab = input(f"\nGanti KDA? (sekarang: {match['kill']}/{match['death']}/{match['assist']}) (y/t): ").strip().lower()
                            if jawab in ("y", "ya", "t", "tidak"):
                                    break
                            print("Jawab dengan y/ya atau t/tidak!")
                        if jawab == "y" or jawab == "ya":
                            while True:
                                input_baru_k = input("Kill baru: ").strip()
                                input_baru_d = input("Death baru: ").strip()
                                input_baru_a = input("Assist baru: ").strip()
                                if (input_baru_k.isdigit() and input_baru_d.isdigit() and input_baru_a.isdigit()):
                                    kill_baru = int(input_baru_k)
                                    death_baru = int(input_baru_d)
                                    assist_baru = int(input_baru_a)
                                    break
                                print("Kill, Death, dan Assist harus berupa angka!")

                        if hasilBaru != match["hasil"]:
                            print(f"\nHasil berubah dari {match['hasil']} menjadi {hasilBaru}, RR wajib diisi ulang.")
                            ganti_rr = True
                        else:
                            while True:
                                jawab = input(f"\nGanti RR Yang Didapat? (sekarang: {match['rr']:+}) (y/t): ").strip().lower()
                                if jawab in ("y", "ya", "t", "tidak"):
                                    break
                                print("Jawab dengan y/ya atau t/tidak!")
                            ganti_rr = (jawab == "y" or jawab == "ya")

                        if ganti_rr:
                            while True:
                                if hasilBaru == "W":
                                    inputRR = input("RR yang didapat (angka saja, otomatis +): ").strip()
                                elif hasilBaru == "L":
                                    inputRR = input("RR yang hilang (angka saja, otomatis -): ").strip()
                                else:
                                    inputRR = input("RR seri (0 = tidak berubah, boleh juga 10 atau -10): ").strip()
 
                                if inputRR == "":
                                    print("Jangan kosong")
                                elif hasilBaru != "T" and not inputRR.isdigit():
                                    print("Ketik angkanya aja tanpa tanda + atau -, tandanya otomatis")
                                elif hasilBaru == "T" and not (inputRR.isdigit() or (inputRR.startswith("-") and inputRR[1:].isdigit())):
                                    print("Format RR salah")
                                elif hasilBaru != "T" and int(inputRR) == 0:
                                    print("Minimal dapat 1 rr lah kalau gk draw")
                                else:
                                    break
 
                            if hasilBaru == "W":
                                rr_baru = int(inputRR)
                            elif hasilBaru == "L":
                                rr_baru = -int(inputRR)
                            else:
                                rr_baru = int(inputRR)
                        print("\n--- RINGKASAN DATA BARU ---")
                        print(f"Map   : {map_baru}")
                        print(f"Agent : {baru_agent}")
                        print(f"Score : {round_w_baru}-{round_l_baru} ({hasilBaru})")
                        print(f"KDA   : {kill_baru}/{death_baru}/{assist_baru}")
                        print(f"RR    : {rr_baru}")
                        while True:
                            simpan = input("\nSimpan perubahan ini? (y/t): ").strip().lower()
                            if simpan in ("y", "ya", "t", "tidak"):
                                break
                            print("Jawab dengan y/ya atau t/tidak!")
                        if simpan == "y" or simpan == "ya":
                            user_matches[nomor_game]["map"] = map_baru
                            user_matches[nomor_game]["agent"] = baru_agent
                            user_matches[nomor_game]["round_w"] = round_w_baru
                            user_matches[nomor_game]["round_l"] = round_l_baru
                            user_matches[nomor_game]["hasil"] = hasilBaru
                            user_matches[nomor_game]["kill"] = kill_baru
                            user_matches[nomor_game]["death"] = death_baru
                            user_matches[nomor_game]["assist"] = assist_baru
                            user_matches[nomor_game]["rr"] = rr_baru
                            print("\n\033[92mData game berhasil diperbarui!\033[0m")
                        else:
                            print("\nPerubahan dibatalkan, data tidak diubah.")
                        input("\nTekan ENTER untuk kembali...")
                        
                    elif pilih_crud == "4":
                        os.system("cls" if os.name == "nt" else "clear")        
                        print("=== HAPUS DATA Game ===\n")
                        if len(user_matches) == 0:
                            print("Belum ada data untuk dihapus.")
                            input("\nTekan ENTER untuk kembali...")
                            continue
                        
                        for nomor, match in user_matches.items():
                            print(
                                f"{nomor}. Map: {match['map']} | "
                                f"Agent: {match['agent']} | "
                                f"Hasil: {match['hasil']} | "
                                f"KDA: {match['kill']}/{match['death']}/{match['assist']}")
                        while True:
                            inputDelete = input("\nMasukkan nomor game yang ingin dihapus (atau 'kembali'): ").strip().lower()

                            if inputDelete == "kembali":
                                    print("Hapus data dibatalkan.")
                                    input("Tekan ENTER untuk kembali...")
                                    break
                            
                            elif inputDelete.isdigit():
                                if int(inputDelete) in user_matches:
                                    idx_delete = int(inputDelete)
                                    break
                                else:
                                    print("Data game ga ada")
                            else:
                                print("Masukkan nomor data game yang valid atau ketik 'kembali'!")
                        
                        if inputDelete == "kembali":
                            continue
                            
                        konfirm = input(f"Yakin ingin menghapus Game #{idx_delete}? (y/t): ").strip().lower()
                        if konfirm == "y" or konfirm == "ya":
                            del user_matches[idx_delete]
                            history_baru = {}
                            nomor = 1
                            for isi_baru in user_matches.values():
                                history_baru[nomor] = isi_baru
                                nomor += 1
                            user_data["history_catat"] = history_baru
                            print("\n\033[92mData game berhasil dihapus!\033[0m")
                        else:
                            print("\nHapus data dibatalkan.")
                    
                        input("\nTekan ENTER untuk kembali...")
                        
                    elif pilih_crud == "5":
                        os.system("cls" if os.name == "nt" else "clear")
                        
                        print("=== REKAPITULASI STATISTIK PERFORMA ===\n")
                        if len(user_matches) == 0:
                            print("Belum ada data rekap untuk dihitung.")
                        else:
                            total_game = len(user_matches)
                            menang = 0
                            kalah = 0
                            seri = 0
                            sum_k = 0
                            sum_d = 0
                            sum_a = 0
                            max_k = -1
                            max_d = -1
                            max_a = -1
                            
                            game_total_k = ""
                            game_total_d = ""
                            game_total_a = ""
                            
                            nama_map_list = []
                            map_hitung_list = []
                            agent_nama_list = []
                            agent_hitung_list = []
                            
                            current_rank = data_performa[user_data_index][1]
                            current_rr = data_performa[user_data_index][2]
                            
                            if len(user_matches) > 0:
                            # nama map[0], nama agen[1], round w[2], round l[3], hasil[4], kill[5],death[6], asist[7], rr yang didapat[8]
                                kill_terdikit = user_matches[0][5]
                                map_k_terdikit = user_matches[0][0]
                                agent_k_terdikit = user_matches[0][1]
                                map_agent_k_terdikit = f"Map {map_k_terdikit} (Agent {agent_k_terdikit})"
                                
                                death_terdikit = user_matches[0][6]
                                map_d_terdikit = user_matches[0][0]
                                agent_d_terdikit = user_matches[0][1]
                                map_agent_d_terdikit = f"Map {map_d_terdikit} (Agent {agent_d_terdikit})"
                            
                                a_terdikit = user_matches[0][7]
                                map_a_terdikit = user_matches[0][0]
                                agent_a_terdikit = user_matches[0][1]
                                map_agent_a_terdikit = f"Map {map_a_terdikit} (Agent {agent_a_terdikit})"
                            
                            for match in user_matches:
                                # Hitung W/L/T
                                if match[4] == "W":
                                    menang += 1
                                elif match[4] == "L":
                                    kalah += 1
                                else:
                                    seri += 1
                                    
                                # Akumulasi KDA
                                sum_k += match[5]
                                sum_d += match[6]
                                sum_a += match[7]
                                
                                # Cari Total K, D, A
                                if match[5] > max_k:
                                    max_k = match[5]
                                    game_total_k = f"Map {match[0]} (Agent {match[1]})"
                                if match[6] > max_d:
                                    max_d = match[6]
                                    game_total_d = f"Map {match[0]} (Agent {match[1]})"
                                if match[7] > max_a:
                                    max_a = match[7]
                                    game_total_a = f"Map {match[0]} (Agent {match[1]})"
                                    
                                kill_data_sekarang = match[5]
                                if kill_data_sekarang < kill_terdikit:
                                    kill_terdikit = kill_data_sekarang
                                    map_k_terdikit = match[0]
                                    agent_k_terdikit = match[1]
                                    map_agent_k_terdikit = f"Map {map_k_terdikit} (Agent {agent_k_terdikit})"
                                    
                                death_data_sekarang = match[6]
                                if death_data_sekarang < death_terdikit:
                                    death_terdikit = death_data_sekarang
                                    map_d_terdikit = match[0]
                                    agent_d_terdikit = match[1]
                                    map_agent_d_terdikit = f"Map {map_d_terdikit} (Agent {agent_d_terdikit})"
                                    
                                a_data_sekarang = match[7]
                                if a_data_sekarang < a_terdikit:
                                    a_terdikit = a_data_sekarang
                                    map_a_terdikit = match[0]
                                    agent_a_terdikit = match[1]
                                    map_agent_a_terdikit = f"Map {map_a_terdikit} (Agent {agent_a_terdikit})"
                                    
                                # Hitung Map Terbanyak
                                found_map = False
                                for list_map in range(len(nama_map_list)):
                                    if nama_map_list[list_map] == match[0]:
                                        map_hitung_list[list_map] += 1
                                        found_map = True
                                        break
                                if not found_map:
                                    nama_map_list.append(match[0])
                                    map_hitung_list.append(1)
                                    
                                # Hitung Agent Terbanyak
                                found_ag = False
                                for agi in range(len(agent_nama_list)):
                                    if agent_nama_list[agi] == match[1]:
                                        agent_hitung_list[agi] += 1
                                        found_ag = True
                                        break
                                if not found_ag:
                                    agent_nama_list.append(match[1])
                                    agent_hitung_list.append(1)
                                    
                                # Hitung perubahan RR & Rank Promosi/Demosi
                                current_rr += match[8]
                                while current_rr >= 100 and current_rank < len(daftar_rank) - 1:
                                    current_rr -= 100
                                    current_rank += 1
                                while current_rr < 0 and current_rank > 0:
                                    current_rr += 100
                                    current_rank -= 1
                                if current_rank == 0 and current_rr < 0:
                                    current_rr = 0
                                    
                            # Cari map paling sering dimainkan
                            map_tersering = nama_map_list[0]
                            max_m_val = map_hitung_list[0]
                            for list_map in range(len(nama_map_list)):
                                if map_hitung_list[list_map] > max_m_val:
                                    max_m_val = map_hitung_list[list_map]
                                    map_tersering = nama_map_list[list_map]
                                    
                            # Cari agent paling sering dimainkan
                            ag_tersering = agent_nama_list[0]
                            max_ag_val = agent_hitung_list[0]
                            for agi in range(len(agent_nama_list)):
                                if agent_hitung_list[agi] > max_ag_val:
                                    max_ag_val = agent_hitung_list[agi]
                                    ag_tersering = agent_nama_list[agi]
                                    
                            avg_k = sum_k / total_game
                            avg_d = sum_d / total_game
                            avg_a = sum_a / total_game
                            
                            if current_rank == len(daftar_rank) - 1:
                                rr_butuh = "Sudah rank tertinggi (Radiant)"
                            else:
                                rr_butuh = f"{100 - current_rr} RR lagi menuju {daftar_rank[current_rank + 1]} HIHIHI"
                            
                            print(f"Total Game Dimainkan    : {total_game}")
                            print(f"Menang (W) / Kalah (L)  / Seri (T): {menang} Menang | {kalah} Kalah | {seri} Seri")
                            print(f"Total KDA               : {sum_k} / {sum_d} / {sum_a}")
                            print(f"Rata-rata KDA per Game  : {avg_k:.1f} / {avg_d:.1f} / {avg_a:.1f}")
                            
                            print(f"Kill Terbanyak          : {max_k} ({game_total_k})")
                            print(f"Kill Terdikit          : {kill_terdikit} ({map_agent_k_terdikit})")
                            
                            print(f"Death Terbanyak         : {max_d} ({game_total_d})")
                            print(f"Death Terdikit          : {death_terdikit} ({map_agent_d_terdikit})")
                            
                            print(f"Assist Terbanyak        : {max_a} ({game_total_a})")
                            print(f"Assist Terdikit          : {a_terdikit} ({map_agent_a_terdikit})")
                            
                            print(f"Map Paling Sering Main  : {map_tersering} ({max_m_val}x)")
                            print(f"Agent Paling Sering Pakai: {ag_tersering} ({max_ag_val}x)")
                            print(f"Rank Saat Ini           : {daftar_rank[current_rank]} (RR: {current_rr})")
                            print(f"Sisa RR Menuju Rank Naik: {rr_butuh}")
                            print("="*45)
                        input("\nTekan ENTER untuk kembali...")
                    elif pilih_crud == "6" or pilih_crud == "kembali":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan ENTER...")
            elif inputUserMenu == "3":
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan ENTER...")