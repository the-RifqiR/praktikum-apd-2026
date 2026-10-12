# usia = 16

# x = "Boleh Masuk" if usia > 16 else "Dilarang Masuk"

# print(x)

# angka = 6

# if angka < 10: # Kondisi percabangan IF
#     print("Angka kurang dari 10")

# umur = int(input("Masukkan umur: ")) # Input umur
# # Misalkan, umur = 17
# if umur >= 17:
#     print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena kondisi True
# else:
#     print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan kalau kondisinya true, dijalankan kalau kondisi awal false

# kendaraan = input("Masukkan jenis kendaraan anda: ")

# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000
# # Menampilkan tarif parkir yang harus dibayar
# print(f"Tarif parkir kendaraan {kendaraan} yang harus dibayar:", tarif_parkir)

# nilai = int(input("Masukan Nilai: "))

# if nilai > 90:
#     print("A")
# elif nilai > 80:
#     print("B")
# elif nilai >= 70:
#     print("C")
# elif nilai >= 50 and nilai <= 69:
#     print("D")
# else:
#     print("E")
    
# umur = int(input("Masukan Umur: "))

# status = "Boleh Masuk" if umur >= 16 else "Tidak Boleh Masuk"
# print(status)

# total_belanja = 100001

# if total_belanja > 200000:
#     diskon = 0.3
#     total_bayar = total_belanja * diskon
#     print("Dapat diskon", diskon)
# elif total_belanja > 100000:
#     diskon = 0.1
#     total_bayar = total_belanja * diskon
#     print("Dapat diskon", diskon)
# else:
#     diskon = 0
#     print("Dapat diskon", diskon)
#     total_bayar = total_belanja
    
    
# print(total_bayar)

# hujan = True
# mendung = False

# if hujan:
#     if mendung:
#         print("Bawa payung")
# else:
#     print("Jalan biasa")

nilai = 88
kehadiran = 74

if nilai >= 88:
    print("Dapat Mengikuti Ujian")
    if kehadiran >= 90:
        print("Lulus")
    else:
        print("Tanya ujian susulan")
else:
    print("DO")
    