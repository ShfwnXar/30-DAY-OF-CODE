def binary_to_decimal(binary_str):
    try:
        # Menggunakan fungsi built-in int() untuk konversi biner ke desimal
        decimal_number = int(binary_str, 2)
        return decimal_number
    except ValueError:
        return "Input bukan biner yang valid"

def decimal_to_binary(decimal_number):
    try:
        # Menggunakan fungsi built-in bin() untuk konversi desimal ke biner
        binary_str = bin(decimal_number).replace("0b", "")
        return binary_str
    except TypeError:
        return "Input bukan desimal yang valid"

def main():
    while True:
        print("\nPilih jenis konversi:")
        print("1. Biner ke Desimal")
        print("2. Desimal ke Biner")
        print("3. Keluar")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            binary_str = input("Masukkan angka biner: ")
            result = binary_to_decimal(binary_str)
            print(f"Hasil konversi: {result}")
        elif choice == '2':
            try:
                decimal_number = int(input("Masukkan angka desimal: "))
                result = decimal_to_binary(decimal_number)
                print(f"Hasil konversi: {result}")
            except ValueError:
                print("Input bukan desimal yang valid.")
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
