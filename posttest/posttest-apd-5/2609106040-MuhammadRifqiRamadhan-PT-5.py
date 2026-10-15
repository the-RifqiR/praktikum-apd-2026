import os

# Format: [username, password, role]
accounts = [
    ["adminvlao", "admin123", "admin"],
    ["aja", "041", "user"],
    ["bang lari", "068", "user"]
]

daftar_map = ["Ascent", "Bind", "Haven", "Split", "Lotus", "Sunset", "Abyss", "Corrode", "Icebox", "Summit", "Pearl"]
daftar_role = ["Duelist", "Initiator", "Controller", "Sentinel"]
daftar_agents = [
    ["Jett", "Phoenix", "Raze", "Reyna", "Yoru", "Neon", "Iso", "Waylay"],  # Duelist
    ["Breach", "Sova", "Skye", "Kayo", "Fade", "Gekko", "Tejo"], # Initiator
    ["Brimstone", "Omen", "Viper", "Astra", "Harbor", "Clove", "Miks"], # Controller
    ["Sage", "Cypher", "Killjoy", "Chamber", "Deadlock", "Vyse"]  # Sentinel
]

data_performa = []

bintang = "=" * 45
while True:
    os.system('cls')
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
        os.system('cls')
        print(bintang)
        print(" REGISTER AKUN BARU ".center(45, "="))
        print(bintang)
        
        while True:
            new_username = input("Masukan Username baru: ")
            # Cek duplikasi username
            sudah_ada = False
            for acc in accounts:
                print(acc)
                if acc[0] == new_username:
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
                
        accounts.append([new_username, new_password, "user"])
        print("Registrasi Berhasil, Silakan Login.")
        input("Tekan ENTER untuk kembali...")
        continue
    
    os.system('cls')
    if menu_awal == 1:
        print(" LOGIN ADMIN ".center(45, "="))
        target_role = "admin"
    else:
        print(" LOGIN PENGGUNA ".center(45, "="))
        target_role = "user"    
        
    inputUsername = input("Username: ")
    inputPassword = input("Password: ")
    
    login_sukses = False
    for account in accounts:
        # kalau username sama dan password sama dan role sama
        if  inputUsername == account[0] and inputPassword == account[1] and  target_role == account[2]:
            login_sukses = True
            break
        
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
                map_baru = input("Masukkan nama map baru: ").strip().upper()
                if map_baru == "":
                    print("Nama map tidak boleh kosong!")
                    
                elif map_baru in [nama.upper() for nama in daftar_map]:
                    print("Map tersebut sudah terdaftar!")
                    
                else:
                    daftar_map.append(map_baru)
                    print(f"\nMap '{map_baru}' berhasil tambah")
                input("\nTekan ENTER untuk lanjut...")
            elif inputPilih == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== TAMBAH AGENT ===")
                print("Pilih Role Agent: ")
                for i in range(len(daftar_role)):
                    print(f"{i+1}. {daftar_role[i]}")
                
                input_role = input("Pilih nomor role (1-4): ").strip()
                if input_role.isdigit() and 1 <= int(input_role) <= len(daftar_agents):
                    idx_r = int(input_role) - 1
                    agent_baru = input(f"Masukkan nama agent untuk {daftar_role[idx_r]}: ").strip().upper()
                    if agent_baru == "":
                        print("Nama agent tidak boleh kosong!")
                    elif agent_baru in [nama.upper() for nama in daftar_agents[idx_r]]:
                        print("Agent tersebut sudah terdaftar pada role ini!")
                    else:
                        daftar_agents[idx_r].append(agent_baru)
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
                    for data in data_performa:
                        print(f"Username: {data[0]} | Total Game Tercatat: {len(data[3])}")
                input("\nTekan ENTER untuk lanjut...")
                
            elif inputPilih == "4":
                break
            else:
                print("Pilihan gak ada")
                input("Tekan ENTER...")
                
    elif target_role == "user":
        user_data_index = -1
        for i in range(len(data_performa)):
            if data_performa[i][0] == inputUsername:
                user_data_index = i
                break

        if user_data_index == -1:
            # formatnya username, rank, rr, [data game]
            data_performa.append([inputUsername, 0, 0, []])
            user_data_index = len(data_performa) - 1
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
                if len(data_performa[user_data_index][3]) == 0:
                    while True:
                        print("\nPilih Rank Saat Ini:")
                        for rank in range(len(daftar_rank)):
                            print(f"{rank+1}. {daftar_rank[rank]}")
                        inputRank = input("Pilih nomor rank (1-9): ").strip()
                        if inputRank.isdigit() and 1 <= int(inputRank) <= len(daftar_rank):
                            data_performa[user_data_index][1] = int(inputRank) - 1
                            break
                        print("Pilihan tidak valid!")
                    rank_awal_user = data_performa[user_data_index][1]
                    rank_tertinggi = len(daftar_rank) - 1
                    while True:
                        if rank_awal_user == rank_tertinggi:
                            rr_awal = input("Masukkan RR saat ini (minimal 0, tanpa batas atas): ").strip()
                        else:
                            rr_awal = input("Masukkan RR saat ini (0-99): ").strip()
                        if rr_awal == "":
                            print("RR tidak boleh kosong!")
                        elif not rr_awal.isdigit():
                            print("RR harus berupa angka bulat dan tidak boleh negatif!")
                        elif rank_awal_user != rank_tertinggi and int(rr_awal) > 99:
                            print("RR maksimal 99! RR 100 ke atas hanya untuk rank Radiant.")
                        else:
                            data_performa[user_data_index][2] = int(rr_awal)
                            break
                        
                for gim in range(jumlah_gim):
                    print(f"\n--- GAME KE-{gim + 1} DARI {jumlah_gim} ---")
                    print("\nDaftar Map:")
                # ==========    ==============================================
                    for peta in range(len(daftar_map)):
                        print(f"{peta+1}. {daftar_map[peta]}")
                    while True:
                        inputMap = input("Pilih nomor map: ").strip()
                        if inputMap.isdigit() and 1 <= int(inputMap) <= len(daftar_map):
                            nama_map = daftar_map[int(inputMap)-1]
                            break
                        print("Nomor map tidak valid!")
                    # ==========    ============================================== 
                    print("\nPilih Role Agent:")
                    for no_role_agent in range(len(daftar_role)):
                        print(f"{no_role_agent + 1}. {daftar_role[no_role_agent]}")
                    while True:
                        input_role = input("Pilih nomor role (1-4): ").strip()
                        if input_role.isdigit() and 1 <= int(input_role) <= 4:
                            no_role = int(input_role) - 1
                            break
                        print("Role tidak valid!")
                    # ==========    ======================================================
                    print(f"\nDaftar Agent {daftar_role[no_role]}:")
                    agents_list = daftar_agents[no_role]
                    for agent in range(len(agents_list)):
                        print(f"{agent + 1}. {agents_list[agent]}")
                    while True:
                        pilihAgent = input("Pilih nomor agent: ").strip()
                        if pilihAgent.isdigit() and 1 <= int(pilihAgent) <= len(agents_list):
                            nama_agent = agents_list[int(pilihAgent)-1]
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

                        # nama map[0], nama agen[1], round w[2], round l[3], hasil[4], kill[5],death[6], asist[7], rr yang didapat[8]
                    match_item = [nama_map, nama_agent, round_w, round_l, hasil, k, d, a, rr_change]
                    data_performa[user_data_index][3].append(match_item)
                print("\n\033[92mSemua data Game berhasil dicatat!\033[0m")
                input("Tekan ENTER untuk kembali...")