daftar_mahasiswa = []

def tambah_mahasiswa(nama, nim):
    daftar_mahasiswa.append({"nama": nama, "nim": nim})
    print(f"Data {nama} ({nim}) berhasil disimpan!")
def lihat_mahasiswa():
    print("\nDaftar Mahasiswa Terdaftar:")
    for i, mhs in enumerate(daftar_mahasiswa):
        print(f"{i + 1}. {mhs['nama']} - NIM: {mhs['nim']}")