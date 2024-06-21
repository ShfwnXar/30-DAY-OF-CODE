def hitung_target_tabungan(total_tabungan, periode, frekuensi):
    # Menghitung jumlah periode berdasarkan frekuensi
    if frekuensi == "harian":
        jumlah_periode = periode * 365
    elif frekuensi == "mingguan":
        jumlah_periode = periode * 52
    elif frekuensi == "bulanan":
        jumlah_periode = periode * 12
    else:
        print("Frekuensi tidak valid. Harap masukkan 'harian', 'mingguan', atau 'bulanan'.")
        return None

    # Menghitung jumlah tabungan per periode
    tabungan_per_periode = total_tabungan / jumlah_periode
    return tabungan_per_periode

def main():
    print("Selamat datang di Program Penghitung Target Tabungan!")
    
    # Meminta input dari pengguna
    total_tabungan = float(input("Masukkan jumlah total tabungan yang diinginkan: "))
    periode = float(input("Masukkan periode waktu yang diinginkan (dalam tahun): "))
    frekuensi = input("Masukkan frekuensi menabung (harian, mingguan, bulanan): ").lower()
    
    # Menghitung tabungan per periode
    hasil = hitung_target_tabungan(total_tabungan, periode, frekuensi)
    
    if hasil is not None:
        print(f"Anda perlu menabung sebesar {hasil:.2f} setiap {frekuensi} untuk mencapai target tabungan Anda.")
    else:
        print("Perhitungan tidak dapat dilakukan karena input tidak valid.")

if __name__ == "__main__":
    main()
