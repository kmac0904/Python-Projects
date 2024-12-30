import sys
from PyQt5 import QtWidgets, QtGui

class SalesReportApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Monthly Sales Report")
        self.setGeometry(100, 100, 400, 300)

        # Dropdown for Month Selection
        self.label_select_month = QtWidgets.QLabel("Select Month:", self)
        self.label_select_month.setGeometry(50, 50, 100, 30)
        self.comboBox_month = QtWidgets.QComboBox(self)
        self.comboBox_month.setGeometry(150, 50, 150, 30)
        self.comboBox_month.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])

        # Get Sales Button
        self.button_get_sales = QtWidgets.QPushButton("Get Sales", self)
        self.button_get_sales.setGeometry(120, 100, 150, 40)
        self.button_get_sales.clicked.connect(self.display_sales)

        # Label to Display Sales
        self.label_sales = QtWidgets.QLabel("Monthly Sales: ", self)
        self.label_sales.setGeometry(50, 160, 300, 30)
        self.label_sales.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        # Sample sales data (can be replaced with a database or file lookup)
        self.sales_data = {
            "January": 10000,
            "February": 15000,
            "March": 12000,
            "April": 13000,
            "May": 11000,
            "June": 14000,
            "July": 17000,
            "August": 16000,
            "September": 19000,
            "October": 20000,
            "November": 21000,
            "December": 22000
        }

    def display_sales(self):
        # Get selected month
        selected_month = self.comboBox_month.currentText()
        # Retrieve sales data
        sales = self.sales_data.get(selected_month, "No data available")
        # Display result
        self.label_sales.setText(f"Monthly Sales: ${sales:,}")

# Main function
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = SalesReportApp()
    mainWin.show()
    sys.exit(app.exec_())
