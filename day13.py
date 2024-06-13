# Input jarak tempuh dalam kilometer
jarak_tempuh = float(input("Masukkan jarak tempuh dalam kilometer: "))

# Menghitung BBM terbakar (dengan asumsi konsumsi BBM 1:7)
bbm_terbakar = jarak_tempuh / 7

# Input harga BBM per liter
harga_bbm = float(input("Masukkan harga BBM per liter: "))

# Menghitung total biaya
total_biaya = bbm_terbakar * harga_bbm

# Menampilkan hasil
print(f"BBM terbakar: {bbm_terbakar:.2f} liter")
print(f"Total biaya: Rp {total_biaya:.2f}")
