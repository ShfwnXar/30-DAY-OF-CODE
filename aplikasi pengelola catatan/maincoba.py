
import sys
from PyQt5 import QtWidgets
from pbo3 import Ui_PengelolaCatatan  # Pastikan untuk mengganti 'pbo3_ui' dengan nama file .py yang benar

class MainDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.ui = Ui_PengelolaCatatan()
        self.ui.setupUi(self)


        # Sambungkan sinyal ke slot yang sesuai di sini
        self.ui.tambahkancatatan.clicked.connect(self.add_note)
        self.ui.hapuscatatan.clicked.connect(self.remove_selected_note)

    def add_note(self):
        # Fungsi untuk menambahkan catatan ke list
        note_text = self.ui.MAsukkancatatan.text()
        if note_text:  # Pastikan teks catatan tidak kosong
            self.ui.listcatatan.addItem(note_text)
            self.ui.MAsukkancatatan.clear()  # Bersihkan line edit setelah menambahkan

    def remove_selected_note(self):
    # Mengambil item yang dipilih
        selected_item = self.ui.listcatatan.currentItem()
        if selected_item is not None:
            # Menghapus item yang dipilih
            self.ui.listcatatan.takeItem(self.ui.listcatatan.row(selected_item))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    sys.exit(app.exec_())
