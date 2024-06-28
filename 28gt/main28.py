import sys
from PyQt5.QtWidgets import QApplication, QDialog
from day28_ui import Ui_Dialog

class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.power_on = False

        # Set range for temperature dial
        self.ui.pengatursuhu.setMinimum(16)
        self.ui.pengatursuhu.setMaximum(30)

        # Connect signals and slots
        self.ui.tombolpower.clicked.connect(self.toggle_power)
        self.ui.pengatursuhu.valueChanged.connect(self.update_temperature)
        self.ui.pengaturkecepatanfan.valueChanged.connect(self.update_fan_speed)

    def toggle_power(self):
        self.power_on = not self.power_on
        if self.power_on:
            self.ui.tombolpower.setText("Off")
        else:
            self.ui.tombolpower.setText("Power")
            self.ui.penampilsuhu.display(0)
            self.ui.penampilkecepatanfan.setValue(0)

    def update_temperature(self, value):
        if self.power_on:
            self.ui.penampilsuhu.display(value)

    def update_fan_speed(self, value):
        if self.power_on:
            self.ui.penampilkecepatanfan.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyApp()
    mainWindow.show()
    sys.exit(app.exec_())
