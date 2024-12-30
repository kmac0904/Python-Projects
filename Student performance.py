import sys
from PyQt5 import QtWidgets, QtGui

class StudentPerformanceApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Student Performance Calculator")
        self.setGeometry(100, 100, 500, 400)

        # Student Name
        self.label_name = QtWidgets.QLabel("Enter student name:", self)
        self.label_name.setGeometry(50, 30, 150, 30)
        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_name.setGeometry(200, 30, 200, 30)

        # Student Score
        self.label_score = QtWidgets.QLabel("Enter student score:", self)
        self.label_score.setGeometry(50, 80, 150, 30)
        self.lineEdit_score = QtWidgets.QLineEdit(self)
        self.lineEdit_score.setGeometry(200, 80, 200, 30)

        # Attendance Score
        self.label_attendance = QtWidgets.QLabel("Enter attendance score:", self)
        self.label_attendance.setGeometry(50, 130, 150, 30)
        self.lineEdit_attendance = QtWidgets.QLineEdit(self)
        self.lineEdit_attendance.setGeometry(200, 130, 200, 30)

        # Calculate Button
        self.button_calculate = QtWidgets.QPushButton("Calculate student performance", self)
        self.button_calculate.setGeometry(150, 180, 220, 40)
        self.button_calculate.clicked.connect(self.calculate_performance)

        # Result Labels
        self.label_grade = QtWidgets.QLabel("Grade:", self)
        self.label_grade.setGeometry(50, 250, 300, 30)
        self.label_grade.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        self.label_pass_fail = QtWidgets.QLabel("Pass/Fail:", self)
        self.label_pass_fail.setGeometry(50, 290, 300, 30)
        self.label_pass_fail.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        self.label_deans_list = QtWidgets.QLabel("Dean's List:", self)
        self.label_deans_list.setGeometry(50, 330, 300, 30)
        self.label_deans_list.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

    def calculate_performance(self):
        try:
            # Get inputs
            student_name = self.lineEdit_name.text().strip()
            student_score = float(self.lineEdit_score.text().strip())
            attendance_score = float(self.lineEdit_attendance.text().strip())

            # Calculate Grade
            if student_score >= 90:
                grade = "A"
                pass_fail = "Pass"
                deans_list = "Yes" if attendance_score >= 90 else "No"
            elif student_score >= 80:
                grade = "B"
                pass_fail = "Pass"
                deans_list = "No"
            elif student_score >= 70:
                grade = "C"
                pass_fail = "Pass"
                deans_list = "No"
            elif student_score >= 60:
                grade = "D"
                pass_fail = "Pass"
                deans_list = "No"
            else:
                grade = "F"
                pass_fail = "Fail"
                deans_list = "No"

            # Display Results
            self.label_grade.setText(f"Grade: {grade}")
            self.label_pass_fail.setText(f"Pass/Fail: {pass_fail}")
            self.label_deans_list.setText(f"Dean's List: {deans_list}")

        except ValueError:
            self.label_grade.setText("Grade: Invalid input!")
            self.label_pass_fail.setText("Pass/Fail: Invalid input!")
            self.label_deans_list.setText("Dean's List: Invalid input!")

# Main function
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = StudentPerformanceApp()
    mainWin.show()
    sys.exit(app.exec_())
