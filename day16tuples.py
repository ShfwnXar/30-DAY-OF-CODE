# Contoh Program Pengenalan Tuples

# Membuat sebuah tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple asli:", my_tuple)

# Mengakses elemen-elemen dari tuple
print("Elemen pertama:", my_tuple[0])
print("Elemen terakhir:", my_tuple[-1])

# Mengiris (slicing) sebuah tuple
print("Elemen kedua hingga keempat:", my_tuple[1:4])

# Menggabungkan dua tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Tuple gabungan:", combined_tuple)

# Mengulang elemen dalam tuple
repeated_tuple = tuple1 * 3
print("Tuple berulang:", repeated_tuple)

# Memeriksa keberadaan elemen dalam tuple
print("Apakah 3 ada dalam tuple?", 3 in my_tuple)

# Menghitung jumlah elemen dalam tuple
print("Jumlah elemen dalam my_tuple:", len(my_tuple))

# Contoh penggunaan tuple dalam fungsi
def min_max(numbers):
    return (min(numbers), max(numbers))

numbers = (10, 20, 30, 40, 50)
minimum, maximum = min_max(numbers)
print("Nilai minimum:", minimum)
print("Nilai maksimum:", maximum)

# Tuple bersarang
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Tuple bersarang:", nested_tuple)
print("Elemen pertama dari tuple kedua:", nested_tuple[1][0])

# Tuple dan unpacking
person = ("John", 25, "Engineer")
name, age, profession = person
print("Nama:", name)
print("Umur:", age)
print("Profesi:", profession)

# Contoh praktis penggunaan tuple dalam list
list_of_tuples = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
for name, age in list_of_tuples:
    print(f"Nama: {name}, Umur: {age}")

# Menggunakan tuple sebagai kunci dalam dictionary
dictionary = {(1, 2): "a", (3, 4): "b"}
print("Nilai dari kunci (1, 2):", dictionary[(1, 2)])
print("Nilai dari kunci (3, 4):", dictionary[(3, 4)])
