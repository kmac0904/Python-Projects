import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class UnityIDApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Unity ID Generator")
        self.setGeometry(100, 100, 400, 300)

        # First Name
        self.label_first_name = QtWidgets.QLabel("Enter First Name:", self)
        self.label_first_name.setGeometry(50, 30, 120, 30)
        self.lineEdit_first_name = QtWidgets.QLineEdit(self)
        self.lineEdit_first_name.setGeometry(180, 30, 150, 30)

        # Middle Name
        self.label_middle_name = QtWidgets.QLabel("Enter Middle Name:", self)
        self.label_middle_name.setGeometry(50, 80, 120, 30)
        self.lineEdit_middle_name = QtWidgets.QLineEdit(self)
        self.lineEdit_middle_name.setGeometry(180, 80, 150, 30)

        # Last Name
        self.label_last_name = QtWidgets.QLabel("Enter Last Name:", self)
        self.label_last_name.setGeometry(50, 130, 120, 30)
        self.lineEdit_last_name = QtWidgets.QLineEdit(self)
        self.lineEdit_last_name.setGeometry(180, 130, 150, 30)

        # Button to Generate Unity ID
        self.button_generate = QtWidgets.QPushButton("Generate Unity ID", self)
        self.button_generate.setGeometry(100, 180, 200, 40)
        self.button_generate.clicked.connect(self.generate_unity_id)

        # Label to Display Unity ID
        self.label_display_unity = QtWidgets.QLabel("Unity ID:", self)
        self.label_display_unity.setGeometry(50, 240, 300, 30)
        self.label_display_unity.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

    def generate_unity_id(self):
        # Get input values
        first_name = self.lineEdit_first_name.text().strip().lower()
        middle_name = self.lineEdit_middle_name.text().strip().lower()
        last_name = self.lineEdit_last_name.text().strip().lower()

        # Generate Unity ID
        if first_name and last_name:
            unity_id = first_name[0] + middle_name[0] + last_name[:6]
            self.label_display_unity.setText(f"Unity ID: {unity_id}")
        else:
            self.label_display_unity.setText("Please enter valid names!")


# Main function to run the app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UnityIDApp()
    mainWindow.show()
    sys.exit(app.exec_())
