class ManajerInventori:
    def __init__(self):
        self.inventori = {}  # menyimpan barang dalam bentuk dictionary

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah
            return f"Berhasil menambah {jumlah} {nama_barang}. Total: {self.inventori[nama_barang]}"
        return "Jumlah harus lebih dari 0"

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            if 0 < jumlah <= self.inventori[nama_barang]:
                self.inventori[nama_barang] -= jumlah

                if self.inventori[nama_barang] == 0:
                    del self.inventori[nama_barang]

                return f"{jumlah} {nama_barang} berhasil dihapus."
            return "Jumlah tidak valid atau melebihi stok."
        return "Barang tidak ditemukan dalam inventori."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        return f"Inventori saat ini: {self.inventori}"


# Demonstrasi penggunaan class
manager = ManajerInventori()

print(manager.tambah_barang("Laptop", 10))
print(manager.tambah_barang("Mouse", 20))
print(manager.tambah_barang("Laptop", 5))

print(manager.hapus_barang("Mouse", 5))
print(manager.hapus_barang("Laptop", 12))

print(manager.lihat_inventori())
