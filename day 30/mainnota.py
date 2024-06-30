import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from nota import Ui_MainWindow

class CashierApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.items = []
        self.total_price = 0

        # Connect buttons to functions
        self.menambahbarang.clicked.connect(self.add_item)
        self.hapussemuabarang.clicked.connect(self.clear_items)
        self.cetaknota.clicked.connect(self.print_receipt)

    def add_item(self):
        item_name = self.namabarang.text()
        item_price = float(self.hargabarang.text())
        item_qty = int(self.jumlahbarang.text())

        if item_name and item_price and item_qty:
            total_item_price = item_price * item_qty
            self.items.append((item_name, item_price, item_qty, total_item_price))
            self.total_price += total_item_price
            self.namabarang.clear()
            self.hargabarang.clear()
            self.jumlahbarang.clear()
            self.update_receipt_preview()
        else:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields")

    def clear_items(self):
        self.items = []
        self.total_price = 0
        self.listjumlahbarangnamabaranghargatotal.clear()

    def update_receipt_preview(self):
        self.listjumlahbarangnamabaranghargatotal.clear()
        self.listjumlahbarangnamabaranghargatotal.addItem("Toko Shafwan")

        for item in self.items:
            self.listjumlahbarangnamabaranghargatotal.addItem(
                f"{item[2]} x {item[0]} @ {item[1]} = {item[3]}"
            )
        total = self.total_price
        self.listjumlahbarangnamabaranghargatotal.addItem(f"\nTotal: {total}")

    def print_receipt(self):
        receipt_text = "Toko Shafwan\n"


        for item in self.items:
            receipt_text += f"{item[2]} x {item[0]} @ {item[1]} = {item[3]}\n"

        total = self.total_price

        receipt_text += f"\nTotal: {total}\n"

        with open("receipt.txt", "w") as file:
            file.write(receipt_text)
        QMessageBox.information(self, "Receipt Printed", "Receipt has been printed to receipt.txt")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CashierApp()
    window.show()
    sys.exit(app.exec_())
