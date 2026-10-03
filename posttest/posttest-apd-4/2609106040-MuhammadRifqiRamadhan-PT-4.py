username = "Haha"
password = "041"
headerfooter = "="* 40


while True:
    inputUsn = input("Masukan Username: ").strip()
    inputPass = input("Masukan 3 digit terakhir NIM: ").strip()

    if inputUsn == username and inputPass == password:
        print(f"{"\033[92m"}Berhasil login{"\033[0m"}")
        break
    elif inputUsn != username and inputPass != password:
        print("Username dan Password salah atau kosong. Coba lagi")
    elif inputUsn != username:
        print("Username salah")
    else:
        print("Password salah")
    
kalimantanGambut = 0
kalimantanMineral = 0
sumateraGambut = 0
sumateraMineral = 0
# While 1 Start
while True:   
    pulau = ""
    jenisLahan = ""
    # While 2 start
    while pulau != "KALIMANTAN" and pulau != "SUMATERA":
        
        print(f"{headerfooter}\nLIST PULAU\n1. KALIMANTAN\n2. SUMATERA\n{headerfooter}")
        inputPulau = input("Masukan Pulau (KALIMANTAN/SUMATERA): ").strip().upper()
        print(f"{headerfooter}\nLIST JENSI LAHAN\n1. GAMBUT\n2. MINERAL\n{headerfooter}")


        if inputPulau == "KALIMANTAN":
            pulau = inputPulau
            print(f"Anda memilih pulau {pulau}\n")

            jenisLahan = ""
            # while 3 kalimantan start
            while jenisLahan != "GAMBUT" and jenisLahan != "MINERAL": 
                inputJenisLahan = input("Masukan Jenis Lahan (GAMBUT/MINERAL): ").strip().upper()
                if inputJenisLahan == "GAMBUT":
                    jenisLahan = inputJenisLahan            
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                elif inputJenisLahan == "MINERAL": 
                    jenisLahan = inputJenisLahan           
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                else:
                    print("Input salah atau kosong, masukan ulang") 
            # WHile 3 kalimantan end
            
        elif inputPulau == "SUMATERA":
            pulau = inputPulau
            print(f"Anda memilih pulau {pulau}\n")
            # While 3 sumatera start 
            while jenisLahan != "GAMBUT" and jenisLahan != "MINERAL": 
                inputJenisLahan = input("Masukan Jenis Lahan (GAMBUT/MINERAL): ").strip().upper()

                if inputJenisLahan == "GAMBUT":
                    jenisLahan = inputJenisLahan
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                elif inputJenisLahan == "MINERAL": 
                    jenisLahan = inputJenisLahan
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                else:

                    print("Output: Input salah atau kosong, masukan ulagng")
            # while 3 sumatera end 

        else:
            print("Output: Inputmu kosong atau beda, masukan ulang")
        # while 2 end

    print(f"{pulau}-{jenisLahan}")
    # while 4
    while True:
        angka = input("Masukan Jumlah Titik Api: ")

        if angka == "":
            print("Input kosong")
        elif not angka.isdigit():
            print("Angka harus input hah... oh input harus angka")
        else:
            angka = int(angka)
            hektareLahan = angka * 5
            break
    if pulau == "KALIMANTAN":
        if jenisLahan == "GAMBUT":
            kalimantanGambut += hektareLahan
        elif jenisLahan == "MINERAL":
            kalimantanMineral += hektareLahan
    elif pulau == "SUMATERA":
        if jenisLahan == "GAMBUT":
            sumateraGambut += hektareLahan
        elif jenisLahan == "MINERAL":
            sumateraMineral += hektareLahan
            
    # while 4 end
    print(f"{headerfooter}")
    print("RINGKASAN DATA")
    print(f"Lokasi Lahan            : {pulau} Jenis-{jenisLahan}")
    print(f"Titik Api               : {angka} titik")
    print(f"Estimasi Luas Kebakaran : {hektareLahan} Hektare")
    # TURUNKAN PRAB- Ini Kahutla ya Bang/Mba :D
    print(f"{headerfooter}\n")

    # while 5
    while True:
        konfirmasi = input("Apakah anda masih mau input data titik api lagi? (Y/T)").strip().upper()
        if konfirmasi == "Y":
            print("Isi ulang\n")
            break
    # while 5 end
        elif konfirmasi == "T":
            break
    # while 5 end
        else:
            print("Pilihan hanya Y atau T")
    
    if konfirmasi == "T":
        break
    # while 1 end
print(headerfooter)
print(f"Kalimantan - Gambut  : {kalimantanGambut} hektare")
print(f"Kalimantan - Mineral : {kalimantanMineral} hektare")
print(f"Sumatera   - Gambut  : {sumateraGambut} hektare")
print(f"Sumatera   - Mineral : {sumateraMineral} hektare")
print(headerfooter)
