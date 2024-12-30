import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class StudentRecordsApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Student Records Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Button to show records
        self.button_show_records = QtWidgets.QPushButton("Show records", self)
        self.button_show_records.setGeometry(320, 50, 150, 40)
        self.button_show_records.clicked.connect(self.display_records)

        # Table to display student records
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(50, 120, 700, 400)
        self.tableWidget.setColumnCount(4)  # Number of columns
        self.tableWidget.setHorizontalHeaderLabels(["Student ID", "First Name", "Last Name", "Current GPA"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Example student data
        self.student_data = [
            {"id": "1001", "first_name": "Alice", "last_name": "Johnson", "gpa": 3.9},
            {"id": "1002", "first_name": "Bob", "last_name": "Smith", "gpa": 3.5},
            {"id": "1003", "first_name": "Charlie", "last_name": "Brown", "gpa": 3.8},
            {"id": "1004", "first_name": "Diana", "last_name": "Green", "gpa": 4.0},
        ]

    def display_records(self):
        # Populate the table with student data
        self.tableWidget.setRowCount(len(self.student_data))  # Set number of rows
        for row, student in enumerate(self.student_data):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student["id"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student["first_name"]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student["last_name"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{student['gpa']:.2f}"))

# Main function to run the app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = StudentRecordsApp()
    mainWin.show()
    sys.exit(app.exec_())
