from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
import mysql.connector
import sys


class StudentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Database Manager")
        self.setGeometry(100, 100, 800, 600)

        # Input Fields for Student Data
        self.label_id = QtWidgets.QLabel("Enter Student ID", self)
        self.label_id.setGeometry(50, 50, 150, 30)
        self.lineEdit_id = QtWidgets.QLineEdit(self)
        self.lineEdit_id.setGeometry(200, 50, 200, 30)

        self.label_name = QtWidgets.QLabel("Enter Student Name", self)
        self.label_name.setGeometry(50, 100, 150, 30)
        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_name.setGeometry(200, 100, 200, 30)

        self.label_age = QtWidgets.QLabel("Enter Student Age", self)
        self.label_age.setGeometry(50, 150, 150, 30)
        self.lineEdit_age = QtWidgets.QLineEdit(self)
        self.lineEdit_age.setGeometry(200, 150, 200, 30)

        # Insert Button
        self.insert_button = QtWidgets.QPushButton("Insert Data", self)
        self.insert_button.setGeometry(50, 200, 150, 30)
        self.insert_button.clicked.connect(self.insert_data)

        # Display Data Button
        self.display_button = QtWidgets.QPushButton("Display Data", self)
        self.display_button.setGeometry(250, 200, 150, 30)
        self.display_button.clicked.connect(self.display_data)

        # Table Widget for Displaying Data
        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setGeometry(50, 250, 700, 300)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Student ID", "Student Name", "Student Age"])

    def establish_connection(self):
        """Establish connection to the MySQL database."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                database="student_db",
                user="root",
                password="Km@2002/09/04"
            )
            return connection
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Could not connect to the database: {e}")
            return None

    def insert_data(self):
        """Insert data into the database."""
        student_id = self.lineEdit_id.text().strip()
        student_name = self.lineEdit_name.text().strip()
        student_age = self.lineEdit_age.text().strip()

        if not student_id or not student_name or not student_age:
            QMessageBox.warning(self, "Input Error", "All fields are required!")
            return

        connection = self.establish_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()

            # Check if the Student ID already exists
            cursor.execute("SELECT * FROM student WHERE studentid = %s", (student_id,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Duplicate Entry", "Student ID already exists!")
                return

            # Insert the new record
            query = "INSERT INTO student (studentid, studentname, studentage) VALUES (%s, %s, %s)"
            cursor.execute(query, (student_id, student_name, student_age))
            connection.commit()
            QMessageBox.information(self, "Success", "Data inserted successfully!")

            # Clear input fields
            self.lineEdit_id.clear()
            self.lineEdit_name.clear()
            self.lineEdit_age.clear()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Failed to insert data: {e}")
        finally:
            cursor.close()
            connection.close()

    def display_data(self):
        """Fetch and display data from the database."""
        connection = self.establish_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM student")
            records = cursor.fetchall()

            # Populate the table widget
            self.table_widget.setRowCount(len(records))
            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Failed to retrieve data: {e}")
        finally:
            cursor.close()
            connection.close()


# Main Execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec_())
