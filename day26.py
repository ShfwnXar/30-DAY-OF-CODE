import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contoh PyQt5")
        self.setGeometry(100, 100, 300, 200)

        self.input_label = QLabel("Masukkan jumlah anak bebek:", self)
        self.input_label.move(20, 20)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(20, 50, 260, 20)

        self.result_label = QLabel("", self)
        self.result_label.setGeometry(20, 110, 260, 60)

        self.button = QPushButton("Jalankan", self)
        self.button.setGeometry(20, 80, 260, 30)
        self.button.clicked.connect(self.calculate)

    def calculate(self):
        r = int(self.input_field.text())
        result = ""
        if r >= 2:
            while r > 1:
                result += f"Anak bebek turun {r}, mati 1, tinggal {r-1}\n"
                r = r - 1

        if r == 1:
            result += "Anak bebek turun 1, mati 1, tinggal induknya"

        self.result_label.setText(result)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
