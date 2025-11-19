class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan diri
    def perkenalan_diri(self):
        return (f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, "
                f"IPK: {self.ipk}, Universitas: {Mahasiswa.universitas}")

    # Method update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK mahasiswa {self.nama} diperbarui menjadi: {self.ipk}"

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"

mhs1 = Mahasiswa("Budi Santoso", "TI001", "Teknik Informatika", 3.7)
mhs2 = Mahasiswa("Siti Aminah", "TI002", "Teknik Informatika", 3.2)
mhs3 = Mahasiswa("Joko Pratama", "TI003", "Teknik Informatika", 2.3)

# Demonstrasi semua method
print(mhs1.perkenalan_diri())
print(mhs1.predikat_kelulusan())

print(mhs2.perkenalan_diri())
print(mhs2.predikat_kelulusan())

print(mhs3.perkenalan_diri())
print(mhs3.predikat_kelulusan())

# Update IPK lalu tampilkan ulang
print(mhs3.update_ipk(2.8))
print(mhs3.predikat_kelulusan())
