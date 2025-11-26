# Class Definitions
class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"
class Nilai:
    def __init__(self, mata_kuliah, nilai):
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.nilai_list = []

    def tambah_nilai(self, nilai):
        self.nilai_list.append(nilai)

    def tampilkan_nilai(self):
        print(f"\nDaftar Nilai Mahasiswa: {self.nama} ({self.nim})")
        if not self.nilai_list:
            print("Belum ada nilai.")
        else:
            for n in self.nilai_list:
                print(f"- {n.mata_kuliah.nama}: {n.nilai}")

    def rata_rata(self):
        if not self.nilai_list:
            return 0
        total = sum(n.nilai for n in self.nilai_list)
        return total / len(self.nilai_list)
class ProgramStudi:
    def __init__(self, nama_prodi):
        self.nama_prodi = nama_prodi
        self.mata_kuliah = []

    def tambah_mk(self, mk):
        self.mata_kuliah.append(mk)

    def tampilkan_mk(self):
        print(f"\nDaftar Mata Kuliah Program Studi {self.nama_prodi}:")
        for mk in self.mata_kuliah:
            print(f"- {mk}")

    def report_program(self):
        print(f"\n=== REPORT PROGRAM STUDI {self.nama_prodi.upper()} ===")
        for mk in self.mata_kuliah:
            print(f"* {mk.nama} ({mk.sks} SKS)")
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.program_studi = []

    def tambah_prodi(self, prodi):
        self.program_studi.append(prodi)

# a. Tambahkan 2 Program Studi
kampus = Universitas("Universitas Teknologi Nusantara")

prodi_ti = ProgramStudi("Teknik Informatika")
prodi_si = ProgramStudi("Sistem Informasi")

kampus.tambah_prodi(prodi_ti)
kampus.tambah_prodi(prodi_si)

# b. Tambahkan minimal 2 Mata Kuliah per Prodi
mk_ti1 = MataKuliah("TI101", "Algoritma dan Pemrograman", 3)
mk_ti2 = MataKuliah("TI102", "Struktur Data", 3)

mk_si1 = MataKuliah("SI201", "Analisis Sistem", 3)
mk_si2 = MataKuliah("SI202", "Basis Data", 3)

prodi_ti.tambah_mk(mk_ti1)
prodi_ti.tambah_mk(mk_ti2)

prodi_si.tambah_mk(mk_si1)
prodi_si.tambah_mk(mk_si2)

# c. Buat 3 Mahasiswa + Tambah Nilai
mhs1 = Mahasiswa("23001", "Rizal")
mhs2 = Mahasiswa("23002", "Putra")
mhs3 = Mahasiswa("23003", "Sinta")

mhs1.tambah_nilai(Nilai(mk_ti1, 85))
mhs1.tambah_nilai(Nilai(mk_si2, 90))

mhs2.tambah_nilai(Nilai(mk_ti2, 75))
mhs2.tambah_nilai(Nilai(mk_si1, 80))

mhs3.tambah_nilai(Nilai(mk_si1, 88))
mhs3.tambah_nilai(Nilai(mk_si2, 92))

# d. Tampilkan daftar mata kuliah tiap Prodi
prodi_ti.tampilkan_mk()
prodi_si.tampilkan_mk()

# e. Tampilkan daftar nilai tiap mahasiswa
mhs1.tampilkan_nilai()
mhs2.tampilkan_nilai()
mhs3.tampilkan_nilai()

# f. Tampilkan rata-rata tiap mahasiswa
print("\n=== RATA-RATA NILAI MAHASISWA ===")
print(f"{mhs1.nama}: {mhs1.rata_rata():.2f}")
print(f"{mhs2.nama}: {mhs2.rata_rata():.2f}")
print(f"{mhs3.nama}: {mhs3.rata_rata():.2f}")

# g. Panggil report_program
prodi_ti.report_program()
prodi_si.report_program()
