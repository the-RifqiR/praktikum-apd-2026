from tampilan import clear, jeda, pilih_menu, sukses
from auth import login
from registrasi import register
from admin_menu import menu_admin
from menu_user import menu_user

def sambutan():
    clear()
    print("Selamat datang di VlaoTracker!")
    print('''Halo, halo, Selamat Pagi, Hidup Mahasiswa, Hidup Rakyat Indonesia, Hidup Perempuan Yang Melawan, Hidup Teknik! Selamat datang di program paling epik abad ini: VLAOTRACKER 

Dibuat sebelum menuju TA huhuhuhu, secangkir esteh yang membuat semangat sebentar, dan dipersembahkan untuk aslab:
-> NLG'25 (068) (Ketua)
-> R'25   (106)
-> SNA'25 (016)
-> YAP'25 (017)
Well... Well... Well. Posttest APD terakhir:D 

Program ini didedikasikan buat nilai 100 dan menambah pengetahuan.

Intinya: Catat performa, tampilin stat. 
semoga lulus posttest, dan jangan lupa senyum ya Aslab Aslab Aslab Aslab sibuk banget kaya \033[9mpenjabat\033[0m guah (ermmm ini dari stiker btw bukan saya yang ngomong :D) Yey! 🎉
time to lock in''')
    jeda()

def menu_utama():
    sambutan()
    while True:
        clear()
        pilihan = pilih_menu(" SELAMAT DATANG DI VLAOTRACKER ",{ 
            1 : "Admin",
            2: "Lu Member",
            3: "Belum Punya Akun? (Register)",
            4 : "Keluar Program"
        })
        if pilihan == 1:
            username = login("admin")
            if username is not None:
                menu_admin(username)
        elif pilihan == 2:
            username = login("user")
            if username is not None:
                menu_user(username)
        elif pilihan == 3:
            register()
        else:
            sukses("Terima kasih sudah menggunakan VlaoTracker!")
            break

if __name__ == "__main__":
    menu_utama()