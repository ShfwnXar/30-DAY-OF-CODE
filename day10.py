def konversi_ke_unit(jumlah, satuan):
    """Fungsi untuk mengonversi jumlah dari satuan tertentu ke unit (satuan dasar)."""
    satuan = satuan.lower()
    if satuan == 'lusin':
        return jumlah * 12
    elif satuan == 'kodi':
        return jumlah * 20
    elif satuan == 'gross':
        return jumlah * 144
    else:
        return "Satuan tidak dikenali"

def konversi_dari_unit(jumlah, satuan):
    """Fungsi untuk mengonversi jumlah dari unit (satuan dasar) ke satuan tertentu."""
    satuan = satuan.lower()
    if satuan == 'lusin':
        return jumlah / 12
    elif satuan == 'kodi':
        return jumlah / 20
    elif satuan == 'gross':
        return jumlah / 144
    else:
        return "Satuan tidak dikenali"

# Contoh penggunaan
jumlah = int(input("Masukkan jumlah: "))
satuan = input("Masukkan satuan (lusin/kodi/gross): ")

# Konversi ke unit
jumlah_unit = konversi_ke_unit(jumlah, satuan)
print(f"{jumlah} {satuan} sama dengan {jumlah_unit} unit.")

# Konversi dari unit ke satuan yang sama
jumlah_konversi = konversi_dari_unit(jumlah_unit, satuan)
print(f"{jumlah_unit} unit sama dengan {jumlah_konversi} {satuan}.")
