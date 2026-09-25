biayaLangganan = 1500000
nama = "haha"
nim = 11

# Input Login
print("=" * 45)
print("   LAYANAN STREAMING MUSIK 'ANGKASA'   ")
print("=" * 45)
inputNama = input("Masukkan Nama Anda              : ")
inputNim = int(input("Masukkan 2 Digit Terakhir NIM   : "))

statusLogin = False
if inputNama == nama and inputNim == nim:
    statusLogin = True

# Data Paket Langganan
paketLangganan = [
    {
        "paket": "Paket Orbit",
        "biayaAdmin": 0.01,
        "benefit": "Akses dasar ke lagu-lagu populer",
    }, 
    {
        "paket": "Paket Nebula",
        "biayaAdmin": 0.03,
        "benefit": "Akses lagu premium dan playlist kustom",
    },
    {
        "paket": "Paket Galaxy",
        "biayaAdmin": 0.05,
        "benefit": "Akses lagu premium, playlist kustom, dan mode offline",
    },
    {
        "paket": "Paket Supernova",
        "biayaAdmin": 0.07,
        "benefit": "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis",
    },
]

if statusLogin:
    print("\n" + "=" * 45)
    print(f" LOGIN BERHASIL! Selamat datang, {inputNama}.")
    print("=" * 45)
    print(" PILIHAN PAKET LANGGANAN ANGKASA:")
    print(" 1. Paket Orbit     (Admin 1%)")
    print(" 2. Paket Nebula    (Admin 3%)")
    print(" 3. Paket Galaxy    (Admin 5%)")
    print(" 4. Paket Supernova (Admin 7%)")
    print("-" * 45)
    
    inputPaLang = int(input("Pilih Paket Langganan Anda [1/2/3/4]: "))
    
    if inputPaLang == 1:
        namaPaket = paketLangganan[0]["paket"]
        biayaAdmin = paketLangganan[0]["biayaAdmin"]
        benefit = paketLangganan[0]["benefit"]
    elif inputPaLang == 2:
        namaPaket = paketLangganan[1]["paket"]
        biayaAdmin = paketLangganan[1]["biayaAdmin"]
        benefit = paketLangganan[1]["benefit"]
    elif inputPaLang == 3:        
        namaPaket = paketLangganan[2]["paket"]
        biayaAdmin = paketLangganan[2]["biayaAdmin"]
        benefit = paketLangganan[2]["benefit"]
    elif inputPaLang == 4:        
        namaPaket = paketLangganan[3]["paket"]
        biayaAdmin = paketLangganan[3]["biayaAdmin"]
        benefit = paketLangganan[3]["benefit"]
    else:
        print("\n Pilihan tidak valid. Program dihentikan.")
        exit()
        
    # Perhitungan Nominal
    biayaAdmin = int(biayaLangganan * biayaAdmin)
    total_bayar = int(biayaLangganan + biayaAdmin)        
    
    # Tampilan Struk / Output Akhir Rapi
    print("\n" + "=" * 45)
    print("         RINCIAN PEMBAYARAN ANGKASA         ")
    print("=" * 45)
    print(f" Nama Pengguna    : {inputNama}")
    print(f" Paket Dipilih    : {namaPaket}")
    print(f" Biaya Langganan  : Rp {int(biayaLangganan)}")
    print(f" Biaya Admin : Rp {int(biayaAdmin)}")
    print("-" * 45)
    print(f" TOTAL BAYAR      : Rp {int(biayaAdmin)}")
    print("-" * 45)
    print(f" Fitur & Benefit  :\n -> {benefit}")
    print("=" * 45)
    print(" Terima kasih telah berlangganan di ANGKASA! ")
    print("=" * 45)

else:
    print(" LOGIN GAGAL! Nama atau NIM tidak sesuai.")
    print(" Program dihentikan.")
    exit()