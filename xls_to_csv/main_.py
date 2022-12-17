from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout
from PyQt5.QtWidgets import (
    QFileSystemModel,
    QTreeView,
    QVBoxLayout,
    QLineEdit,
    QPushButton
)
import style
from pathlib import Path

class MainWindow(QWidget):
    height = 500
    width = 700

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

        # create, style and show ui
        self.setup_ui()
        self.set_style()
        self.show()

    def setup_ui(self):
        # layout
        main_layout = QVBoxLayout()
        path_layout = QHBoxLayout()
        main_layout.addLayout(path_layout)

        # widgets


        self.tree = QTreeView()
        self.tree.setModel(self.model)

        # add widget to layout
        path_layout.addWidget(self.path_txt)
        path_layout.addWidget(self.clear_btn)
        path_layout.addWidget(self.list_btn)
        main_layout.addWidget(self.tree)

    def set_style(self):
        # text box
        self.path_txt.setStyleSheet(style.LINE_EDIT_STYLE)

        # tree
        self.tree.setStyleSheet(style.TREE_VIEW_STYLE)
        self.tree.setColumnWidth(0, 300)
        self.tree.setAlternatingRowColors(True)

        # button
        self.list_btn.setStyleSheet(style.LIST_BUTTON_STYLE)
        self.clear_btn.setStyleSheet(style.CLEAR_BUTTON_STYLE)


def main():
    app = QApplication([])
    ui = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()

