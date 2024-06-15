class NotaBelanja:
    def __init__(self):
        self.items = []

    def tambah_item(self, nama, harga, jumlah):
        item = {
            'nama': nama,
            'harga': harga,
            'jumlah': jumlah,
            'total': harga * jumlah
        }
        self.items.append(item)

    def cetak_nota(self):
        total_harga = 0
        print("\n--- Nota Belanja ---")
        print("       Toko Shafwan       ")
        print(f"{'Nama Item':20} {'Harga':10} {'Jumlah':10} {'Total':10}")
        print("-" * 50)
        for item in self.items:
            print(f"{item['nama']:20} {item['harga']:10.2f} {item['jumlah']:10} {item['total']:10.2f}")
            total_harga += item['total']
        print("-" * 50)
        print(f"{'Total Belanja':>42} {total_harga:10.2f}")

def main():
    nota = NotaBelanja()
    
    while True:
        nama = input("Masukkan nama item (atau 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break
        harga = float(input("Masukkan harga item: "))
        jumlah = int(input("Masukkan jumlah item: "))
        nota.tambah_item(nama, harga, jumlah)
    
    nota.cetak_nota()

if __name__ == "__main__":
    main()
