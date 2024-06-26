import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QMessageBox, QStackedWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from password_storing import PasswordAccess

class StartScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.title = QLabel("Password Manager")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont('Arial', 24))
        
        self.start_button = QPushButton("Start")
        self.start_button.setFont(QFont('Arial', 18))
        self.start_button.clicked.connect(parent.show_main_screen)
        
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.start_button)
        
        self.setStyleSheet("background-color: #2c3e50; color: white;")
        self.title.setStyleSheet("margin-bottom: 50px;")
        self.start_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 15px; border-radius: 10px;")

class MainScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.password_manager = PasswordAccess()
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter your password or search term")
        self.layout.addWidget(self.input_field)
        
        self.store_button = QPushButton("Store Password", self)
        self.store_button.clicked.connect(self.store_password)
        self.layout.addWidget(self.store_button)
        
        self.view_button = QPushButton("View All Passwords", self)
        self.view_button.clicked.connect(self.view_passwords)
        self.layout.addWidget(self.view_button)
        
        self.search_button = QPushButton("Search Password", self)
        self.search_button.clicked.connect(self.search_password)
        self.layout.addWidget(self.search_button)
        
        self.delete_button = QPushButton("Delete Password", self)
        self.delete_button.clicked.connect(self.delete_password)
        self.layout.addWidget(self.delete_button)
        
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.layout.addWidget(self.output_area)
        
        self.setStyleSheet("""
            background-color: #34495e;
            color: white;
            QLineEdit, QTextEdit {
                background-color: #ecf0f1;
                color: black;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin-top: 10px;
            }
        """)
        
    def store_password(self):
        password = self.input_field.text()
        if password:
            self.password_manager.write_password(password)
            self.output_area.append("Password stored successfully")
            self.input_field.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a password to store")
    
    def view_passwords(self):
        passwords = self.password_manager.view_passwords()
        if passwords == []:
            self.output_area.append("No passwords stored")
            return
        self.output_area.append("Viewing all passwords:")
        for password in passwords:
            self.output_area.append(password[0] + " : " + password[1])
    
    def search_password(self):
        password = self.input_field.text()
        if password:
            result = self.password_manager.search_passwords(password)
            self.output_area.append("Search results:")
            self.output_area.append(result)
            self.input_field.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a password to search for")
    
    def delete_password(self):
        password = self.input_field.text()
        if password:
            self.password_manager.delete_entry(password)
            self.output_area.append("Password deleted successfully")
            self.input_field.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a password to delete")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Password Encryption")
        self.setGeometry(100, 100, 600, 400)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.start_screen = StartScreen(self)
        self.main_screen = MainScreen(self)
        
        self.stacked_widget.addWidget(self.start_screen)
        self.stacked_widget.addWidget(self.main_screen)
        
        self.show_start_screen()
        
    def show_start_screen(self):
        self.stacked_widget.setCurrentWidget(self.start_screen)
        
    def show_main_screen(self):
        self.stacked_widget.setCurrentWidget(self.main_screen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
