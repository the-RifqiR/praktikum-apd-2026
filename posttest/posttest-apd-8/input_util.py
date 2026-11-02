from InquirerPy import inquirer
from tampilan import error

def input_angka(pesan, minimum=0, maksimum=None):
    while True:
        try:
            angka = int(input(pesan).strip())
            if angka < minimum:
                raise ValueError(f"Angka minimal {minimum}.")
            if maksimum is not None and angka > maksimum:
                raise ValueError(f"Angka maksimal {maksimum}.")
        except ValueError as e:
            error(f"Input tidak valid: {e}")
        else:
            return angka

def input_teks(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            error(str(e))
        else:
            return teks

pilihan_ya = ("y", "ya")
pilihan_tidak = ("t", "tidak")
def konfirmasi(pesan):
    while True:
        try:
            jawaban = input(pesan).strip().lower()
            if jawaban not in pilihan_ya + pilihan_tidak:
                raise ValueError("Jawab y/ya atau t/tidak!")
        except ValueError as e:
            error(str(e))
        else:
            return jawaban in pilihan_ya

def pilih_pilihan(daftar, pesan):
    # Bisa menerima list, tuple, atau dictionary (yang dipakai key-nya)
    return inquirer.select(
        message=pesan,
        choices=list(daftar),
        pointer="➡️ ",
        qmark=""
    ).execute()