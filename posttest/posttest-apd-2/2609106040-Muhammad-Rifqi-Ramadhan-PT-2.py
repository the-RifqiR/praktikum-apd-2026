# Tugas: Menghitung Total Belanja Sarapan Mba Taylor Swift
# Warung "Gizi Rendah" - dipesan lewat aplikasi "Go-Cek"

import os

# bersihin terminal
clear = lambda: os.system('cls')
 
# Langsung saja dihardcode apa itu input
# Deklarasi dan memasukan nilai
#1. Mba Taylor Swift beli ini 
makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000
 
# variabel penampung semua harga ke list
harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]
biaya_admin = 5000
 
#2. hitung total bayar
total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + biaya_admin
 
#3. perhitungan rata-rata harga dengan banyak data harga 
rata_rata = total_bayar / len(harga_makanan)
 
#4. 2 digit nim terakhir 
nim = 40
 
#5. variabel bolean, mengecek boolean? gktau gunanya buat apa 
bolean = nim != rata_rata
 
# konversi ke euro, kurs asal2an dulu 1 euro = 17000
kurs_euro = 17000
total_bayar_euro = total_bayar / kurs_euro
 
# 6. Menampilkan semua variabel menggunakan print()
clear()
print("=================================================")
print("               Pembelian Makanan                 ")
print("=================================================")
print("Makanan 1   =", makanan_1)
print("Makanan 2   =", makanan_2)
print("Makanan 3   =", makanan_3)
print("Makanan 4   =", makanan_4)
print("Makanan 5   =", makanan_5)
print("Makanan 6   =", makanan_6)
print("List Harga Makanan=", harga_makanan)

print("=================================================")
print("                 Hasil Perhitungan               ")
print("=================================================")
print("Biaya Admin                                =", biaya_admin)
print(f"Perhitungan Total Biaya                    = {makanan_1} + {makanan_2} + {makanan_3} + {makanan_4} + {makanan_5} + {makanan_6} + {biaya_admin}")
print("Total Bayar (Rupiah)                       =", total_bayar)
print(f"Perhitungan Total Biaya (Euro)             = {total_bayar} / {kurs_euro}")
print("Total Bayar (Euro)                         =", total_bayar_euro)
print("Rata-rata                                  =", rata_rata)
print("NIM                                        =", nim)
print("Bolean (NIM != Rata)                       =", bolean)
print("=================================================")