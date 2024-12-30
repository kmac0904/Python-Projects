from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import mysql.connector
import sys


class DBApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Button to display data
        self.display_button = QtWidgets.QPushButton("Display Data", self)
        self.display_button.setGeometry(350, 50, 100, 30)
        self.display_button.clicked.connect(self.display_data)

        # Table widget to show database records
        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setGeometry(50, 100, 700, 400)
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

    def display_data(self):
        """Fetch and display data from the database."""
        connection = self.establish_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM student"
            cursor.execute(query)
            records = cursor.fetchall()

            # Populate table widget
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
    window = DBApp()
    window.show()
    sys.exit(app.exec_())
