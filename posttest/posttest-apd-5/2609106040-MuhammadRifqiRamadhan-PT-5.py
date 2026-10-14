import os

# Format: [username, password, role]
accounts = [
    ["adminvlao", "admin123", "admin"],
    ["aja", "041", "user"],
    ["bang lari", "068", "user"]
]

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
        