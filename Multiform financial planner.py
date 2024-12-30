from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
)
import sys


class FinancialGoalCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Goal Calculator")
        self.setGeometry(100, 100, 600, 400)

        # Main Navigation - Stacked Widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Screens
        self.main_screen = QWidget()
        self.result_screen = QWidget()

        # Add Screens to Stacked Widget
        self.stacked_widget.addWidget(self.main_screen)
        self.stacked_widget.addWidget(self.result_screen)

        # Build Screens
        self.build_main_screen()
        self.build_result_screen()

    def build_main_screen(self):
        """Builds the main input screen."""
        layout = QVBoxLayout()
        self.main_screen.setLayout(layout)

        # Input Fields
        layout.addWidget(QLabel("Yearly Investment:"))
        self.yearly_investment = QLineEdit()
        layout.addWidget(self.yearly_investment)

        layout.addWidget(QLabel("Rate of Return (%):"))
        self.rate_of_return = QLineEdit()
        layout.addWidget(self.rate_of_return)

        layout.addWidget(QLabel("Financial Goal:"))
        self.financial_goal = QLineEdit()
        layout.addWidget(self.financial_goal)

        # Buttons
        self.calculate_button = QPushButton("How Long?")
        self.exit_button = QPushButton("Exit Application")
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.exit_button)

        # Button Actions
        self.calculate_button.clicked.connect(self.calculate_goal)
        self.exit_button.clicked.connect(self.close)

    def build_result_screen(self):
        """Builds the results display screen."""
        layout = QVBoxLayout()
        self.result_screen.setLayout(layout)

        # Table for results
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(2)
        self.results_table.setHorizontalHeaderLabels(["Year", "Current Balance"])
        layout.addWidget(self.results_table)

        # Back Button
        self.back_button = QPushButton("Go Back")
        layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.go_back_to_main)

    def calculate_goal(self):
        """Calculates the years needed to reach the financial goal."""
        try:
            # Fetch user input
            yearly_investment = float(self.yearly_investment.text())
            rate_of_return = float(self.rate_of_return.text()) / 100
            financial_goal = float(self.financial_goal.text())

            # Initialize variables
            current_balance = 0
            year = 0
            results = []

            # Calculation loop
            while current_balance < financial_goal:
                current_balance += yearly_investment
                current_balance += current_balance * rate_of_return
                year += 1
                results.append((year, round(current_balance, 2)))

            # Display results
            self.display_results(results)
        except ValueError:
            # Handle invalid input
            self.show_error_message("Invalid input. Please enter numeric values.")

    def display_results(self, results):
        """Displays the results in the results screen."""
        self.results_table.setRowCount(len(results))

        for row, (year, balance) in enumerate(results):
            self.results_table.setItem(row, 0, QTableWidgetItem(str(year)))
            self.results_table.setItem(row, 1, QTableWidgetItem(f"${balance:,.2f}"))

        # Navigate to results screen
        self.stacked_widget.setCurrentWidget(self.result_screen)

    def go_back_to_main(self):
        """Navigates back to the main screen."""
        self.stacked_widget.setCurrentWidget(self.main_screen)

    def show_error_message(self, message):
        """Shows an error message (extend for additional error handling)."""
        error_label = QLabel(message)
        error_label.setStyleSheet("color: red; font-size: 14px;")
        self.main_screen.layout().addWidget(error_label)


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinancialGoalCalculator()
    window.show()
    sys.exit(app.exec_())
