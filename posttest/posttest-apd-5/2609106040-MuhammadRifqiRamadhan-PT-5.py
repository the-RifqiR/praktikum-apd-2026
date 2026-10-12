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
                print("Masukan Yang Benar-Benar Aja lah (1/2/3)")
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
            