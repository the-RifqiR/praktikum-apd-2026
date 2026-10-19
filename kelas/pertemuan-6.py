#  kartu = ("kartu merah", "kartu merah", "kartu hijau", "kartu biru")

#        kartuku = set(kartu)
#        print(kartuku)

#       angka_ganjil = {1,3,5,7,9}
#       for i in angka_ganjil:
#           print(i)
    
#      kelas = {"a", "b", "c"}
#      kelas.add("d")

#      print(kelas)

#     kelas_b1 = {"juna", "mia", "ilyas", "falih"}
#     print(kelas_b1)
#     kelas_b1.discard("juna")
#     print(kelas_b1)

#     aslab1 = {"fina", "shasha", "risma"}
#     aslab2 = {"larry", "attar", "haekal"}
#     gabung = aslab1.union(aslab2)
#     print(gabung)

#    angka1 = {1,2,3,4,5}
#    print(angka1)
#    angka2 = {2,4,6,8,10}
#    angka1.update(angka2)
#    print(angka1)

#   praktikum = {
#       "apd" : "belajar dictionary",
#       "orsikom" : "belajar logisim"
#   }

#   print(praktikum['orsikom'])
#   print(praktikum)


# biodata = {
#     "nama" : "larry",
#     "umur" : "068",
#     "pacar" : ["laptop", "hp"],
#     "sosmed" : "@mhdilyaass",
# }

#  print(biodata)
#  print(biodata['pacar'][0])
#  print(biodata.get("alamat", "gk ada"))

#   for i in biodata:
#       print(f"{i} = {biodata[i]}")
#  for i in biodata.keys():
#      print(f"{i}")
    
#   for i in biodata.values():
#       print(f"{i}")
    
#  for i, j in biodata.items():
#      print(i)
#      print(j)
        
# game = {"pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))
# # print(game)


# game = {"pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }


# game_baru = game.copy()
# game_baru["valorant"] = "gore"
# print(game)
# print(game_baru)

# key = "a", "b", "c",
# value = "anak infor"
# akt26 = dict.fromkeys(key, value)
# print(akt26)
# print(len(game))
# cache = game.pop("valorant")
# game.clear()
# print(cache)
# print(game)
# print(game)
# game.update({"minecraft" : "fps"})
# print(game)

# del game["valorant"]
# print(game)
# print(game.get("valorant", "Halo halo"))
# game["valorant"] = "horror"
# print(game)


# menu = {
# "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
# "nasi" : ["nasi goreng", "nasi uduk"],
# "mie" : ["mie goreng rendang", "mie goreng aceh"],
# "kuah" : ["soto", "rawon", "sop iga"]
# }


# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#         print(kategori)
#     print("")