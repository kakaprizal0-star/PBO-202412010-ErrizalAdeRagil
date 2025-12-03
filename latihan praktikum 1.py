class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Person: {self.nama}, Umur: {self.umur}"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)  # Memanggil constructor dari Person
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi
p = Person("Budi", 30)
m = Mahasiswa("Andi", 20, "2022001")

# Output
print(p.info())
print(m.info())
