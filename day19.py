import csv

def display_menu():
    print("\nMenu Buku Telepon")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Hapus Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

def add_contact(filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        name = input("Masukkan nama: ")
        phone = input("Masukkan nomor telepon: ")
        writer.writerow([name, phone])
        print("Kontak berhasil ditambahkan!")

def search_contact(filename):
    name = input("Masukkan nama yang ingin dicari: ")
    found = False
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name.lower():
                print(f"Nama: {row[0]}, Nomor Telepon: {row[1]}")
                found = True
                break
        if not found:
            print("Kontak tidak ditemukan.")

def delete_contact(filename):
    name = input("Masukkan nama yang ingin dihapus: ")
    lines = []
    found = False
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() != name.lower():
                lines.append(row)
            else:
                found = True

    if found:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
            print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")

def display_all_contacts(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        print("\nDaftar Kontak:")
        for row in reader:
            print(f"Nama: {row[0]}, Nomor Telepon: {row[1]}")

def main():
    filename = "buku_telepon.csv"
    while True:
        display_menu()
        choice = input("Pilih menu (1-5): ")
        if choice == '1':
            add_contact(filename)
        elif choice == '2':
            search_contact(filename)
        elif choice == '3':
            delete_contact(filename)
        elif choice == '4':
            display_all_contacts(filename)
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
