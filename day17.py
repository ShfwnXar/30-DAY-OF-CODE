tasks = []

def tambah_tugas():
    task = input("Masukkan tugas: ")
    tasks.append(task)
    print("Tugas ditambahkan.")

def lihat_tugas():
    print("Daftar Tugas:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def hapus_tugas():
    lihat_tugas()
    index = int(input("Masukkan nomor tugas yang akan dihapus: ")) - 1
    del tasks[index]
    print("Tugas dihapus.")

while True:
    print("\nAplikasi Todo List")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4): ")

    if pilihan == '1':
        tambah_tugas()
    elif pilihan == '2':
        lihat_tugas()
    elif pilihan == '3':
        hapus_tugas()
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid")