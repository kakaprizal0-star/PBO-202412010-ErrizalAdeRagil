class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info(self):
        return f"{self.merk} berwarna {self.warna}, tahun {self.tahun}"


# Membuat object
mobil1 = Kendaraan("Toyota", "Hitam", 2020)
mobil2 = Kendaraan("Honda", "Merah", 2022)

# Akses instance attribute
print(mobil1.info())
print(mobil2.info())

# Akses class attribute
print(f"Bahan bakar (dari class): {Kendaraan.bahan_bakar}")
print(f"Bahan bakar (dari object 1): {mobil1.bahan_bakar}")
print(f"Bahan bakar (dari object 2): {mobil2.bahan_bakar}")
