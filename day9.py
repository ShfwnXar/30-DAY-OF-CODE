import math

def volume_kubus(sisi):
    return sisi ** 3

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def volume_silinder(jari_jari, tinggi):
    return math.pi * (jari_jari ** 2) * tinggi

def volume_bola(jari_jari):
    return (4/3) * math.pi * (jari_jari ** 3)

def main():
    print("Pilih bentuk wadah:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Silinder")
    print("4. Bola")

    pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        volume = volume_kubus(sisi)
        print(f"Volume kubus adalah: {volume} unit kubik")

    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = volume_balok(panjang, lebar, tinggi)
        print(f"Volume balok adalah: {volume} unit kubik")

    elif pilihan == 3:
        jari_jari = float(input("Masukkan jari-jari silinder: "))
        tinggi = float(input("Masukkan tinggi silinder: "))
        volume = volume_silinder(jari_jari, tinggi)
        print(f"Volume silinder adalah: {volume} unit kubik")

    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari bola: "))
        volume = volume_bola(jari_jari)
        print(f"Volume bola adalah: {volume} unit kubik")

    else:
        print("Pilihan tidak valid. Silakan jalankan ulang program.")

if __name__ == "__main__":
    main()
