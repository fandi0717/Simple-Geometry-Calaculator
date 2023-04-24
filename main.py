import sys
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from objek2 import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create SplashScreen instance
    splash_pix = QPixmap('D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/splashScreen_800_600.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()

    # Create instance of MainWindow
    window = MainWindow()
    window.hide()

    # Timer to show SplashScreen for 3 seconds (3000 milliseconds)
    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(lambda: show_main_window(splash, window))
    timer.start(3000)

    def show_main_window(splash, window):
        # Close SplashScreen
        splash.close()

        # Show MainWindow
        window.show()

    sys.exit(app.exec())
