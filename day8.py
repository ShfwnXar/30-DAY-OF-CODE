class Item:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

class Kasir:
    def __init__(self):
        self.keranjang = []

    def tambah_item(self, nama, harga, jumlah):
        item = Item(nama, harga, jumlah)
        self.keranjang.append(item)
        print(f"Ditambahkan {jumlah} {nama} dengan harga {harga} per item ke keranjang.")

    def hitung_total(self):
        total = 0
        for item in self.keranjang:
            total += item.harga * item.jumlah
        return total

    def cetak_struk(self):
        print("\nStruk Belanja:")
        print("----------------------------")
        for item in self.keranjang:
            print(f"{item.nama} - {item.jumlah} x {item.harga} = {item.harga * item.jumlah}")
        print("----------------------------")
        print(f"Total: {self.hitung_total()}")
        print("----------------------------")
        print("Terima kasih telah berbelanja!")

def main():
    kasir = Kasir()
    
    while True:
        print("\n1. Tambah item ke keranjang")
        print("2. Lihat keranjang dan checkout")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            nama = input("Masukkan nama item: ")
            harga = float(input("Masukkan harga item: "))
            jumlah = int(input("Masukkan jumlah item: "))
            kasir.tambah_item(nama, harga, jumlah)
        elif pilihan == '2':
            kasir.cetak_struk()
        elif pilihan == '3':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
