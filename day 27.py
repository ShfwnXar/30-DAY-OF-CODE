import random

# Fungsi untuk menghasilkan list angka acak
def generate_random_numbers(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers

# Fungsi untuk mengurutkan list menggunakan Bubble Sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Fungsi untuk mengurutkan list menggunakan Selection Sort
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

# Fungsi untuk mengurutkan list menggunakan Insertion Sort
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

# Fungsi untuk menampilkan list angka
def print_numbers(numbers):
    print("List angka:")
    print(numbers)

# Contoh penggunaan
if __name__ == "__main__":
    n = 10  # Jumlah angka acak yang akan di-generate
    numbers = generate_random_numbers(n)

    # Menampilkan list angka sebelum diurutkan
    print("Sebelum diurutkan:")
    print_numbers(numbers)

    # Menggunakan Bubble Sort untuk mengurutkan
    bubble_sorted = numbers.copy()
    bubble_sort(bubble_sorted)
    print("\nSetelah diurutkan menggunakan Bubble Sort:")
    print_numbers(bubble_sorted)

    # Menggunakan Selection Sort untuk mengurutkan
    selection_sorted = numbers.copy()
    selection_sort(selection_sorted)
    print("\nSetelah diurutkan menggunakan Selection Sort:")
    print_numbers(selection_sorted)

    # Menggunakan Insertion Sort untuk mengurutkan
    insertion_sorted = numbers.copy()
    insertion_sort(insertion_sorted)
    print("\nSetelah diurutkan menggunakan Insertion Sort:")
    print_numbers(insertion_sorted)
