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
    print(headerfooter)
    print("LIST PULAU\n1. KALIMANTAN\n2. SUMATERA")
    print(headerfooter)
    
    inputPulau = input("Masukan Pulau: ")
    
    if inputPulau == "1":
        print("Anda memilih pulau KALIMANTAN\n")
        print(headerfooter)
        print("LIST JENSI LAHAN\n1. GAMBUT\n2. MINERAL")
        print(headerfooter)
        
        inputJenisLahan = input("Masukan Jenis Lahan: ")
    else:
        print("Anda memilih pulau SUMATERA\n")
        print(headerfooter)
        print("LIST JENSI LAHAN\n1. GAMBUT\n2. MINERAL")
        print(headerfooter)
        
        inputJenisLahan = input("Masukan Jenis Lahan: ")