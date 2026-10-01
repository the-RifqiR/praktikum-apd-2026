# batas = 5

# for i in range(batas):
#     print(f"Pertemuan: {i}")
    
# game = ["genshin", 7.0, True]

# for i in game:
#     print(i)

# for i in range(1, 10, 3):
#     print(i)

# for i in range(1,3):
#     for j in range(1,4):
#         print(f"{i} x {j} = {i * j}")
#     print("") 
    
# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak?")
    
# print(f"Total perulangan: {hitung}")

# for i in range(10):
#     if i == 5:
#         break    
#     print(i)
    
# for i in range(20):
#     if i == 12:
#         break    
#     print(i)
    
angka_benar = 7

while True:
    print("=== Game tebak angka ===")
    
    
    angka_input = (input("MAsukan angka (1-10): "))
    
    if not angka_input.isdigit():
        continue
    
    angka_input = int(angka_input)
    
    if angka_input < 0 or angka_input > 10:
        print("masukan angka yang benar")
        angka_input = int(input("MAsukan angka (1-10): "))
    elif angka_benar == angka_input:
        print("angka benar yey")
        break
    else:
        print("salahhhhh")