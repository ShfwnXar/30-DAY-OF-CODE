def psi_ke_bar(psi):
    """
    Mengkonversi tekanan dari psi ke bar.
    
    1 psi = 0.0689476 bar
    """
    return psi * 0.0689476

def bar_ke_psi(bar):
    """
    Mengkonversi tekanan dari bar ke psi.
    
    1 bar = 14.5038 psi
    """
    return bar * 14.5038

def main():
    print("Konversi Tekanan")
    print("1. Psi ke Bar")
    print("2. Bar ke Psi")
    pilihan = input("Pilih opsi (1/2): ")

    if pilihan == '1':
        psi = float(input("Masukkan nilai tekanan dalam psi: "))
        bar = psi_ke_bar(psi)
        print(f"{psi} psi = {bar:.4f} bar")
    elif pilihan == '2':
        bar = float(input("Masukkan nilai tekanan dalam bar: "))
        psi = bar_ke_psi(bar)
        print(f"{bar} bar = {psi:.4f} psi")
    else:
        print("Opsi tidak valid.")

if __name__ == "__main__":
    main()
