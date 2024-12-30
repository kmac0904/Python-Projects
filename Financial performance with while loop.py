import sys
from PyQt5 import QtWidgets, QtGui

class FinancialPlannerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Financial Planner")
        self.setGeometry(100, 100, 500, 300)

        # Annual Amount
        self.label_annual = QtWidgets.QLabel("Annual amount:", self)
        self.label_annual.setGeometry(50, 30, 150, 30)
        self.lineEdit_annual = QtWidgets.QLineEdit(self)
        self.lineEdit_annual.setGeometry(200, 30, 200, 30)

        # Target Amount
        self.label_target = QtWidgets.QLabel("Target amount:", self)
        self.label_target.setGeometry(50, 80, 150, 30)
        self.lineEdit_target = QtWidgets.QLineEdit(self)
        self.lineEdit_target.setGeometry(200, 80, 200, 30)

        # Retirement Plan Dropdown
        self.label_plan = QtWidgets.QLabel("Retirement Plan:", self)
        self.label_plan.setGeometry(50, 130, 150, 30)
        self.comboBox_plan = QtWidgets.QComboBox(self)
        self.comboBox_plan.setGeometry(200, 130, 200, 30)
        self.comboBox_plan.addItems(["Retirement Plan 2050", "Standard Plan"])

        # Calculate Button
        self.button_calculate = QtWidgets.QPushButton("How long?", self)
        self.button_calculate.setGeometry(150, 180, 200, 40)
        self.button_calculate.clicked.connect(self.calculate_how_long)

        # Result Label
        self.label_result = QtWidgets.QLabel("Years to Target amount: ", self)
        self.label_result.setGeometry(50, 240, 400, 30)
        self.label_result.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

    def calculate_how_long(self):
        try:
            # Get input values
            annual_amount = float(self.lineEdit_annual.text().strip())
            target_amount = float(self.lineEdit_target.text().strip())
            selected_plan = self.comboBox_plan.currentText()

            # Determine rate of return
            if selected_plan == "Retirement Plan 2050":
                rate_of_return = 6.0 / 100  # 6%
            else:
                rate_of_return = 5.0 / 100  # 5%

            # Calculate number of years to reach target amount
            years = 0
            current_amount = 0
            while current_amount < target_amount:
                current_amount += annual_amount
                current_amount += current_amount * rate_of_return
                years += 1

            # Display result
            self.label_result.setText(f"Years to Target amount: {years}")

        except ValueError:
            self.label_result.setText("Please enter valid numerical inputs.")

# Main function
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = FinancialPlannerApp()
    mainWin.show()
    sys.exit(app.exec_())
