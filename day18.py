# Fungsi untuk menghitung perbandingan resep
def hitung_perbandingan_resep(bahan_asli, porsi_asli, porsi_baru):
    bahan_baru = {}
    for bahan, jumlah in bahan_asli.items():
        bahan_baru[bahan] = jumlah * (porsi_baru / porsi_asli)
    return bahan_baru

# Fungsi utama untuk menjalankan program
def main():
    print("Program Menghitung Perbandingan Resep")
    
    # Meminta input dari pengguna
    porsi_asli = float(input("Masukkan jumlah porsi asli: "))
    
    # Membuat kamus untuk menyimpan bahan dan jumlahnya dalam resep asli
    bahan_asli = {}
    while True:
        bahan = input("Masukkan nama bahan (atau ketik 'selesai' untuk berhenti): ")
        if bahan.lower() == 'selesai':
            break
        jumlah = float(input(f"Masukkan jumlah {bahan} dalam resep asli (dalam gram atau ml): "))
        bahan_asli[bahan] = jumlah
    
    porsi_baru = float(input("Masukkan jumlah porsi yang diinginkan: "))
    
    # Menghitung jumlah bahan untuk porsi baru
    bahan_baru = hitung_perbandingan_resep(bahan_asli, porsi_asli, porsi_baru)
    
    # Menampilkan hasil perhitungan
    print("\nJumlah bahan untuk porsi baru:")
    for bahan, jumlah in bahan_baru.items():
        print(f"{bahan}: {jumlah:.2f} gram/ml")

# Menjalankan program utama
if __name__ == "__main__":
    main()
