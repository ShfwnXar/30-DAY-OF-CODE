# Contoh penggunaan pewarisan (inheritance) dalam Python

# Kelas Induk atau Superclass
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        print("Bunyi hewan")

# Pewarisan atau Subclass
class Anjing(Hewan):
    def __init__(self, nama, jenis, ras):
        super().__init__(nama, jenis)
        self.ras = ras

    def bersuara(self):
        print("Guk guk guk auuuuu")

# Pewarisan atau Subclass lain
class Kucing(Hewan):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna

    def bersuara(self):
        print("Maw maw maw")

# Membuat objek dari kelas Anjing dan Kucing
dog = Anjing("Paww", "Anjing", "alaskan")
cat = Kucing("nana", "Kucing", "Abu-abu")

# Memanggil metode bersuara dari objek
print("Anjing", dog.nama, "bersuara:")
dog.bersuara()

print("\nKucing", cat.nama, "bersuara:")
cat.bersuara()
