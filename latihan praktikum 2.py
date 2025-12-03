import math

class Bentuk:
    def luas(self):
        return 0


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2


# Demonstrasi pemanggilan
b = Bentuk()
p = Persegi(4)
l = Lingkaran(7)

print("Luas Bentuk:", b.luas())
print("Luas Persegi:", p.luas())
print("Luas Lingkaran:", l.luas())
