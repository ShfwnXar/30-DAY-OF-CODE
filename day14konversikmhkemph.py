def kmh_to_mph(kmh):
    """Konversi dari KM/H ke MPH."""
    mph = 0.6214 * kmh
    return mph

def mph_to_kmh(mph):
    """Konversi dari MPH ke KM/H."""
    kmh = mph / 0.6214
    return kmh

def main():
    print("Pilih operasi:")
    print("1. Konversi dari KM/H ke MPH")
    print("2. Konversi dari MPH ke KM/H")
    pilihan = int(input("Masukkan nomor operasi: "))

    if pilihan == 1:
        kmh = float(input("Masukkan kecepatan dalam km/h: "))
        mph = kmh_to_mph(kmh)
        print(f"Kecepatan: {kmh} KM/H = {mph:.2f} MPH")
    elif pilihan == 2:
        mph = float(input("Masukkan kecepatan dalam MPH: "))
        kmh = mph_to_kmh(mph)
        print(f"Kecepatan: {mph} MPH = {kmh:.2f} KM/H")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

if __name__ == "__main__":
    main()
