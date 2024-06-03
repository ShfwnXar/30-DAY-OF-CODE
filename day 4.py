# Contoh penggunaan class (kelas) dalam Python

# Mendefinisikan kelas
class Shafwan:
    # Konstruktor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Metode untuk menampilkan informasi
    def tampil_info(self):
        print("Nama:", self.name)
        print("Usia:", self.age)

# Membuat objek dari kelas Person
person1 = Shafwan("Shafwan", 20)
person2 = Shafwan("Halena", 19)

# Memanggil metode untuk menampilkan informasi
print("Informasi Person 1:")
person1.tampil_info()

print("\nInformasi Person 2:")
person2.tampil_info()
