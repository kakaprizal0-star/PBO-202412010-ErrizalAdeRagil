# Class Buku
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok                   # protected
        self.__lokasi_rak = lokasi_rak      # private

    # Getter & Setter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah > self._stok:
            raise ValueError("Stok buku tidak mencukupi.")
        self._stok -= jumlah

# Class Peminjaman
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali, status):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return f"{
            self.kode_buku
            } | Pinjam: {self.tanggal_pinjam
            } | Kembali: {self.tanggal_kembali
            } | Status: {self.status
            }"

# Class Anggota
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam, status_aktif=True):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam
        self.__status_aktif = status_aktif
        self.daftar_peminjaman = []          # aggregation

    # Getter & Setter status
    def get_status(self):
        return self.__status_aktif

    def set_status(self, status):
        self.__status_aktif = status

    def pinjam_buku(self, buku: Buku, tanggal_pinjam, tanggal_kembali):
        if not self.__status_aktif:
            print("Anggota tidak aktif.")
            return
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Batas peminjaman tercapai.")
            return
        if buku._stok <= 0:
            print(f"Stok buku '{buku.judul}' habis.")
            return

        buku.kurangi_stok(1)
        p = Peminjaman(buku.kode_buku, tanggal_pinjam, tanggal_kembali, "Dipinjam")
        self.daftar_peminjaman.append(p)

    def kembalikan_buku(self, kode_buku, buku_objek):
        for p in self.daftar_peminjaman:
            if p.kode_buku == kode_buku and p.status == "Dipinjam":
                p.status = "Kembali"
                buku_objek.tambah_stok(1)
                return
        print("Buku tidak ditemukan atau sudah dikembalikan.")

# Class Perpustakaan (Composition)
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []

    def tambah_buku(self, judul, penulis, kode_buku, stok, lokasi_rak):
        buku = Buku(judul, penulis, kode_buku, stok, lokasi_rak)
        self.koleksi_buku.append(buku)
        return buku

# INSTANSIASI & DEMONSTRASI PROGRAM
if __name__ == "__main__":
    lib = Perpustakaan("Perpustakaan Kota")

    # Buku
    b1 = lib.tambah_buku("Python Dasar", "Andi", "B001", 3, "Rak A1")
    b2 = lib.tambah_buku("Struktur Data", "Budi", "B002", 2, "Rak B3")
    b3 = lib.tambah_buku("Basis Data", "Cici", "B003", 1, "Rak C2")

    # Anggota
    a1 = Anggota("A101", "Rizal", maks_pinjam=3)
    a2 = Anggota("A102", "Dewi", maks_pinjam=2)

    # Pemijaman
    a1.pinjam_buku(b1, "2025-01-10", "2025-01-17")
    a1.pinjam_buku(b2, "2025-01-10", "2025-01-17")
    a2.pinjam_buku(b3, "2025-01-11", "2025-01-18")

    # Pengembalian
    a1.kembalikan_buku("B001", b1)

    # Output
    print("\n=== INFORMASI BUKU ===")
    for b in lib.koleksi_buku:
        print(f"{b.kode_buku} - {b.judul} | Stok: {b._stok} | Rak: {b.get_lokasi_rak()}")

    print("\n=== INFORMASI ANGGOTA ===")
    print(f"{a1.id_anggota} - {a1.nama} | Status: {a1.get_status()}")
    print(f"{a2.id_anggota} - {a2.nama} | Status: {a2.get_status()}")

    print("\n=== PEMINJAMAN A1 ===")
    for p in a1.daftar_peminjaman:
        print(" -", p.info_peminjaman())

    print("\n=== PEMINJAMAN A2 ===")
    for p in a2.daftar_peminjaman:
        print(" -", p.info_peminjaman())
