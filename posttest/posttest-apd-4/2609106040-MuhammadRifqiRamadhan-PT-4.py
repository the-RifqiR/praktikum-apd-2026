username = "Haha"
password = "041"
headerfooter = "="* 40


while True:
    inputUsn = input("Masukan Username: ")
    inputPass = input("Masukan 3 digit terakhir NIM: ")

    if inputUsn == username and inputPass == password:
        print("Berhasil login")
        break
    elif inputUsn != username and inputPass != password:
        print("Username dan Password salah atau kosong. Coba lagi")
    elif inputUsn != username:
        print("Username salah")
    else:
        print("Password salah")
    

while True:   
    pulau = ""
    jenisLahan = ""
    while pulau != "KALIMANTAN" and pulau != "SUMATERA":
        print(f"{headerfooter}\nLIST PULAU\n1. KALIMANTAN\n2. SUMATERA\n{headerfooter}")
        inputPulau = input("Masukan Pulau (KALIMANTAN/SUMATERA): ").strip().upper()
        print(f"{headerfooter}\nLIST JENSI LAHAN\n1. GAMBUT\n2. MINERAL\n{headerfooter}")


        if inputPulau == "KALIMANTAN":
            pulau = inputPulau
            print(f"Anda memilih pulau {pulau}\n")

            jenisLahan = ""
            while jenisLahan != "GAMBUT" and jenisLahan != "MINERAL": 
                inputJenisLahan = input("Masukan Jenis Lahan (GAMBUT/MINERAL): ").strip().upper()
                if inputJenisLahan == "GAMBUT":
                    jenisLahan = inputJenisLahan            
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                elif inputJenisLahan == "MINERAL": 
                    jenisLahan = "MINERAL"            
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                else:
                    print("Input salah atau kosong masukan kembali") 
        elif inputPulau == "SUMATERA":
            pulau = inputPulau
            print(f"Anda memilih pulau {pulau}\n")

            jenisLahan = ""
            while jenisLahan != "GAMBUT" and jenisLahan != "MINERAL": 
                inputJenisLahan = input("Masukan Jenis Lahan (GAMBUT/MINERAL): ").strip().upper()

                if inputJenisLahan == "GAMBUT":
                    jenisLahan = inputJenisLahan
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                elif inputJenisLahan == "MINERAL": 
                    jenisLahan = inputJenisLahan
                    print(f"Anda memilih jenis lahan {jenisLahan}\n")
                else:

                    print("Output: Input salah atau kosong masukan kembali") 

        else:
            print("Output: Inputmu kosong atau tidak sesuai")

    print(f"{pulau}-{jenisLahan}")
    while True:
        angka = input("Masukan Jumlah Titik Api: ")

        if angka == "":
            print("Input kosong")
        elif not angka.isdigit():
            print("Angka harus dikit")
        else:
            angka = int(angka)
            hektareLahan = angka * 5
            break
            
    while True:
        konfirmasi = input("Apakah anda masih mau input data titik api lagi? (Y/T)").strip().upper()
        if konfirmasi == "Y":
            print("")
            break
        elif konfirmasi == "T":
            break
        else:
            print("Yas")
    
    if konfirmasi == "T":
        print("Terimakasih datanya")
        break

