from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MainWindow(QWidget):
    height = 500
    width = 500

    def __init__(self):
        super().__init__()

        # windows properties
        self.setGeometry(100, 100, MainWindow.width, MainWindow.height)
        self.setWindowTitle('Path Lister')

        # fixing the size
        self.setMaximumSize(MainWindow.width, MainWindow.height)
        self.setMinimumSize(MainWindow.width, MainWindow.height)

        # puts window in center of screen
        current_position = self.frameGeometry()
        screen_geometry = QDesktopWidget().availableGeometry().center()
        current_position.moveCenter(screen_geometry)
        self.move(current_position.topLeft())

        # create and show ui
        self.ui()
        self.show()

    def ui(self):
        pass


def main():
    app = QApplication([])
    ui = MainWindow()
    app.exec_()

if __name__ == '__main__':
    main()

