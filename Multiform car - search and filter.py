from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
)
import sys

# Sample data for cars
CARS = [
    {"model": "Toyota Corolla", "price": 20000},
    {"model": "Honda Civic", "price": 22000},
    {"model": "Ford Focus", "price": 18000},
    {"model": "Tesla Model 3", "price": 35000},
    {"model": "BMW 3 Series", "price": 40000},
]


class CarDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wolfpack Cars")
        self.setGeometry(100, 100, 600, 400)

        # Main Navigation - Stacked Widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Screens
        self.main_screen = QWidget()
        self.search_screen = QWidget()
        self.filter_screen = QWidget()

        # Add Screens to Stacked Widget
        self.stacked_widget.addWidget(self.main_screen)
        self.stacked_widget.addWidget(self.search_screen)
        self.stacked_widget.addWidget(self.filter_screen)

        # Build Screens
        self.build_main_screen()
        self.build_search_screen()
        self.build_filter_screen()

    def build_main_screen(self):
        """Builds the main dashboard screen."""
        layout = QVBoxLayout()
        self.main_screen.setLayout(layout)

        # Welcome Label
        layout.addWidget(QLabel("Welcome to Wolfpack Cars!", alignment=0x0004))

        # Buttons
        search_button = QPushButton("Search")
        filter_button = QPushButton("Filter")
        exit_button = QPushButton("Exit")

        layout.addWidget(search_button)
        layout.addWidget(filter_button)
        layout.addWidget(exit_button)

        # Button Actions
        search_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.search_screen))
        filter_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.filter_screen))
        exit_button.clicked.connect(self.close)

    def build_search_screen(self):
        """Builds the car search screen."""
        layout = QVBoxLayout()
        self.search_screen.setLayout(layout)

        # Dropdown for car model
        layout.addWidget(QLabel("Select Car Model:"))
        self.model_dropdown = QComboBox()
        self.model_dropdown.addItems([car["model"] for car in CARS])
        layout.addWidget(self.model_dropdown)

        # Label to display the average price
        self.average_price_label = QLabel("Average Model Price: ")
        layout.addWidget(self.average_price_label)

        # Back Button
        back_button = QPushButton("Back to Dashboard")
        layout.addWidget(back_button)
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_screen))

        # Dropdown action
        self.model_dropdown.currentIndexChanged.connect(self.update_average_price)

    def update_average_price(self):
        """Updates the average price label based on the selected car model."""
        selected_model = self.model_dropdown.currentText()
        prices = [car["price"] for car in CARS if car["model"] == selected_model]
        if prices:
            self.average_price_label.setText(f"Average Model Price: ${prices[0]:,.2f}")

    def build_filter_screen(self):
        """Builds the car filter screen."""
        layout = QVBoxLayout()
        self.filter_screen.setLayout(layout)

        # Filter Input and Button
        input_layout = QHBoxLayout()
        self.price_input = QLineEdit()
        filter_button = QPushButton("Filter")
        back_button = QPushButton("Go to Dashboard")

        input_layout.addWidget(QLabel("Enter Price:"))
        input_layout.addWidget(self.price_input)
        input_layout.addWidget(filter_button)
        input_layout.addWidget(back_button)
        layout.addLayout(input_layout)

        # Table for results
        self.filter_table = QTableWidget()
        self.filter_table.setColumnCount(2)
        self.filter_table.setHorizontalHeaderLabels(["Model", "Price"])
        layout.addWidget(self.filter_table)

        # Button Actions
        filter_button.clicked.connect(self.apply_filter)
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_screen))

    def apply_filter(self):
        """Filters the car data based on the entered price."""
        try:
            max_price = float(self.price_input.text())
            filtered_cars = [car for car in CARS if car["price"] <= max_price]

            self.filter_table.setRowCount(len(filtered_cars))
            for row, car in enumerate(filtered_cars):
                self.filter_table.setItem(row, 0, QTableWidgetItem(car["model"]))
                self.filter_table.setItem(row, 1, QTableWidgetItem(f"${car['price']:,.2f}"))
        except ValueError:
            # Handle invalid input
            self.filter_table.setRowCount(0)
            self.filter_table.setColumnCount(1)
            self.filter_table.setHorizontalHeaderLabels(["Error"])
            self.filter_table.setItem(0, 0, QTableWidgetItem("Please enter a valid number."))


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarDashboard()
    window.show()
    sys.exit(app.exec_())
