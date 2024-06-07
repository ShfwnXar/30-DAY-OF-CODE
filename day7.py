class Tiket:
    def __init__(self, jenis_tiket):
        self.jenis_tiket = jenis_tiket

    def hitung_harga(self, jumlah_tiket):
        raise NotImplementedError("Metode hitung_harga harus diimplementasikan di subclass!")

class TiketBiasa(Tiket):
    def hitung_harga(self, jumlah_tiket):
        harga_per_tiket = 50_000
        total_harga = harga_per_tiket * jumlah_tiket
        return total_harga

class TiketVIP(Tiket):
    def hitung_harga(self, jumlah_tiket):
        harga_per_tiket = 100_000
        total_harga = harga_per_tiket * jumlah_tiket
        return total_harga

class TiketGold(Tiket):
    def hitung_harga(self, jumlah_tiket):
        harga_per_tiket = 150_000
        total_harga = harga_per_tiket * jumlah_tiket
        return total_harga

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ")
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket.lower() == "biasa":
        tiket = TiketBiasa(jenis_tiket)
    elif jenis_tiket.lower() == "vip":
        tiket = TiketVIP(jenis_tiket)
    elif jenis_tiket.lower() == "gold":
        tiket = TiketGold(jenis_tiket)
    else:
        print("Jenis tiket tidak valid. Harap masukkan 'biasa', 'vip', atau 'gold'.")
        return

    total_harga = tiket.hitung_harga(jumlah_tiket)
    print(f"Total Harga Tiket: Rp {total_harga}")

if __name__ == "__main__":
    main()
