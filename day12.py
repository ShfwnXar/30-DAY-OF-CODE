def hitung_pajak(tapera_persen, pbb_persen, bpjs_persen, nilai_aset):
    # Menghitung masing-masing pajak
    pajak_tapera = nilai_aset * (tapera_persen / 100)
    pajak_pbb = nilai_aset * (pbb_persen / 100)
    pajak_bpjs = nilai_aset * (bpjs_persen / 100)
    
    # Menghitung total pajak
    total_pajak = pajak_tapera + pajak_pbb + pajak_bpjs
    
    # Mengembalikan hasil perhitungan
    return pajak_tapera, pajak_pbb, pajak_bpjs, total_pajak

# Persentase pajak
tapera_persen = 3
pbb_persen = 5
bpjs_persen = 2

# Nilai aset (misalnya nilai properti atau penghasilan)
nilai_aset = float(input("Masukkan nilai aset: "))

# Menghitung pajak
pajak_tapera, pajak_pbb, pajak_bpjs, total_pajak = hitung_pajak(tapera_persen, pbb_persen, bpjs_persen, nilai_aset)

# Menampilkan hasil perhitungan
print(f"Pajak Tapera: Rp {pajak_tapera:,.2f}")
print(f"Pajak Bumi Bangunan (PBB): Rp {pajak_pbb:,.2f}")
print(f"BPJS: Rp {pajak_bpjs:,.2f}")
print(f"Total Pajak: Rp {total_pajak:,.2f}")
