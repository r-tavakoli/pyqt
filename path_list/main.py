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

        # model
        self.model = QFileSystemModel()

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
        self.path_txt = QLineEdit()
        self.path_txt.setPlaceholderText('add your path here...')

        self.list_btn = QPushButton('List')
        self.list_btn.clicked.connect(self.list_files)
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(self.clear_text)

        self.tree = QTreeView()
        self.tree.setModel(self.model)

        # add widget to layout
        path_layout.addWidget(self.path_txt)
        path_layout.addWidget(self.clear_btn)
        path_layout.addWidget(self.list_btn)
        main_layout.addWidget(self.tree)

        # set window layout
        self.setLayout(main_layout)

    def list_files(self):
        # get path from text box
        path = self.path_txt.text()

        # check if path is correct.
        dir_ = Path(path)
        if dir_.exists() and dir_.is_dir():
            self.model.setRootPath(path)
            self.tree.setRootIndex(self.model.index(path))
        else:
            self.path_txt.setText(f'WARNING: "{path}" directory does not exist')

    def clear_text(self):
        self.path_txt.setText('')

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
