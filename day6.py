# Program Kalkulator Sederhana

# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y == 0:
        return "Error: Tidak bisa dibagi dengan nol!"
    else:
        return x / y

print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari pengguna
choice = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))

if choice == '1':
    print("Hasil:", tambah(angka1, angka2))
elif choice == '2':
    print("Hasil:", kurang(angka1, angka2))
elif choice == '3':
    print("Hasil:", kali(angka1, angka2))
elif choice == '4':
    print("Hasil:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid")
