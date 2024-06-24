

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PengelolaCatatan(object):
    def setupUi(self, PengelolaCatatan):
        PengelolaCatatan.setObjectName("PengelolaCatatan")
        PengelolaCatatan.resize(427, 437)
        self.gridLayout = QtWidgets.QGridLayout(PengelolaCatatan)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MAsukkancatatan = QtWidgets.QLineEdit(PengelolaCatatan)
        self.MAsukkancatatan.setText("")
        self.MAsukkancatatan.setObjectName("MAsukkancatatan")
        self.verticalLayout.addWidget(self.MAsukkancatatan)
        self.listcatatan = QtWidgets.QListWidget(PengelolaCatatan)
        self.MAsukkancatatan.setPlaceholderText("Tambahkan Catatan")
        self.listcatatan.setObjectName("listcatatan")
        self.verticalLayout.addWidget(self.listcatatan)
        self.tambahkancatatan = QtWidgets.QPushButton(PengelolaCatatan)
        self.tambahkancatatan.setObjectName("tambahkancatatan")
        self.verticalLayout.addWidget(self.tambahkancatatan)
        self.hapuscatatan = QtWidgets.QPushButton(PengelolaCatatan)
        self.hapuscatatan.setObjectName("hapuscatatan")
        self.verticalLayout.addWidget(self.hapuscatatan)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PengelolaCatatan)
        self.hapuscatatan.clicked.connect(self.listcatatan.clearSelection) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PengelolaCatatan)

    def retranslateUi(self, PengelolaCatatan):
        _translate = QtCore.QCoreApplication.translate
        PengelolaCatatan.setWindowTitle(_translate("PengelolaCatatan", "Pengelola Catatan"))
        self.tambahkancatatan.setText(_translate("PengelolaCatatan", "Tambahkan Catatan"))
        self.hapuscatatan.setText(_translate("PengelolaCatatan", "Hapus Catatan"))
