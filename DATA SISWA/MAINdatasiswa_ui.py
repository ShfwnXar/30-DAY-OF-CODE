import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datasiswa_ui import Ui_MainWindow

class DataSiswaApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data_siswa = []

        # Connect buttons to their functions
        self.MENYIMPANDATA.clicked.connect(self.save_data)
        self.HAPUSDATA.clicked.connect(self.delete_data)
        self.PERBARUIDATA.clicked.connect(self.update_data)
        self.TUTUPMENU.clicked.connect(self.clear_inputs)
        self.CEK.clicked.connect(self.check_data)

    def save_data(self):
        nama = self.DATANAMA.toPlainText()
        kelas = self.DATAKELAS.toPlainText()
        asal = self.DATAASAL.toPlainText()
        alamat = self.DATAALAMAT.toPlainText()
        no_hp = self.DATANOHP.toPlainText()

        if nama and kelas and asal and alamat and no_hp:
            self.data_siswa.append({
                "nama": nama,
                "kelas": kelas,
                "asal": asal,
                "alamat": alamat,
                "no_hp": no_hp
            })
            self.show_message("Sukses", "Data berhasil disimpan!")
            self.clear_inputs()
        else:
            self.show_message("Error", "Semua field harus diisi!")

    def delete_data(self):
        nama = self.DATANAMA.toPlainText()
        self.data_siswa = [siswa for siswa in self.data_siswa if siswa["nama"] != nama]
        self.show_message("Sukses", "Data berhasil dihapus!")
        self.clear_inputs()

    def update_data(self):
        nama = self.DATANAMA.toPlainText()
        for siswa in self.data_siswa:
            if siswa["nama"] == nama:
                siswa["kelas"] = self.DATAKELAS.toPlainText()
                siswa["asal"] = self.DATAASAL.toPlainText()
                siswa["alamat"] = self.DATAALAMAT.toPlainText()
                siswa["no_hp"] = self.DATANOHP.toPlainText()
                self.show_message("Sukses", "Data berhasil diperbarui!")
                self.clear_inputs()
                return
        self.show_message("Error", "Data tidak ditemukan!")

    def clear_inputs(self):
        self.DATANAMA.clear()
        self.DATAKELAS.clear()
        self.DATAASAL.clear()
        self.DATAALAMAT.clear()
        self.DATANOHP.clear()

    def check_data(self):
        nama = self.DATANAMA.toPlainText()
        for siswa in self.data_siswa:
            if siswa["nama"] == nama:
                self.DATAKELAS.setText(siswa["kelas"])
                self.DATAASAL.setText(siswa["asal"])
                self.DATAALAMAT.setText(siswa["alamat"])
                self.DATANOHP.setText(siswa["no_hp"])
                return
        self.show_message("Error", "Data tidak ditemukan!")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataSiswaApp()
    window.show()
    sys.exit(app.exec_())
