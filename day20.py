def balik_kata(kalimat):
    # Memisahkan kalimat menjadi daftar kata
    kata = kalimat.split()
    # Membalikkan setiap kata dalam daftar
    kata_terbalik = [k[::-1] for k in kata]
    # Menggabungkan kata-kata yang sudah dibalik menjadi satu kalimat
    kalimat_terbalik = ' '.join(kata_terbalik)
    return kalimat_terbalik

# Meminta pengguna untuk memasukkan kalimat
kalimat = input("Masukkan kalimat: ")
kalimat_terbalik = balik_kata(kalimat)
print("Kalimat dengan kata terbalik:", kalimat_terbalik)
