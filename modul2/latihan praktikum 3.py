class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        # Public
        self.nim = nim
        self.nama = nama

        # Protected
        self._semester = semester

        # Private
        self.__ipk = ipk

    # Getter protected
    def get_semester(self):
        return self._semester

    # Setter protected
    def set_semester(self, sem_baru):
        if sem_baru <= 0:
            raise ValueError("Semester tidak boleh kurang dari 1.")
        self._semester = sem_baru

    # Getter private
    def get_ipk(self):
        return self.__ipk

    # Setter private
    def set_ipk(self, ipk_baru):
        if ipk_baru < 0 or ipk_baru > 4:
            raise ValueError("IPK harus 0–4.")
        self.__ipk = ipk_baru


# === Membuat 2 objek Mahasiswa ===
m1 = Mahasiswa("23001", "Budi", 2, 3.5)
m2 = Mahasiswa("23002", "Siti", 4, 3.8)

# Output awal
print("=== DATA AWAL ===")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())

# === Mengganti semester & IPK ===
m1.set_semester(3)
m1.set_ipk(3.7)

m2.set_semester(5)
m2.set_ipk(3.9)

# Output setelah perubahan
print("\n=== DATA SETELAH PERUBAHAN ===")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
