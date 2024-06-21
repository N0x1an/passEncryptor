import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Creating the main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window title
        self.setWindowTitle("Password Encryption")
        
        # Window size
        self.setGeometry(100, 100, 400, 300)
        
# create application and main window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    
    # start event loop
    sys.exit(app.exec_())