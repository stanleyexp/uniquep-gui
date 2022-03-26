from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    # QVBoxLayout,
    # QHBoxLayout,
    # QPushButton,
    # QMainWindow,
    # QLabel,
    # QLineEdit,
    # QMenu,
    # QAction,
    # QCheckBox,
    # QComboBox,
    # QDoubleSpinBox,
    QProgressBar,
    # QRadioButton,
    # QSpinBox,
    # QGridLayout,
    # QStackedLayout,
    # QTabWidget,
    QFileDialog,
    QHeaderView
)
from os.path import exists
import sqlite3
from UniquepUI import Ui_Form
import sys
        
class MainWindow(QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.search_btn.clicked.connect(self.search)
        self.download_btn.clicked.connect(self.download)
        self.select_file_btn.clicked.connect(self.open_file)
        self.upload_btn.clicked.connect(self.upload)
        self.prev_btn.clicked.connect(self.prev_page)
        self.next_btn.clicked.connect(self.next_page)
        self.jump_btn.clicked.connect(self.jump_page)
        self.load_data()
        self.total_page = None
        self.total_count = None
        self.count_per_page = 10
        self.curr_page = 1
    def jump_page(self):
        pass
    def prev_page(self):
        self.curr_page = self.curr_page - 1
        pass
    def next_page(self):
        pass
    def uppate_page_status(self):
        self.page_label.setText(f'curr:{str(self.curr_page)} total{str(self.total_page)}')
        if self.curr_page < 2:
            self.prev_btn.setEnabled(False)
        else:
            self.prev_btn.setEnabled(True)

        if self.curr_page > self.total_page:
            self.next_btn.setEnabled(False)
        else:
            self.next_btn.setEnabled(True)

    def table_view_setup(self):
        header = self.table_view.horizontalHeader()     
        # column 1
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        # column 2
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # column 3
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    
    def search(self):
        print("query db")
    def download(self):
        print("download search result")
    def connect_db(self):
        if not exists("uniquep.db"):
            # init db
            connection = sqlite3.connect("uniquep.db")
            cursor = connection.cursor()
            """
            column
            url, descr, income
            """

            cursor.execute("""
                CREATE TABLE uniquep_table
                (url TEXT, descr TEXT, income INTEGER)
            """)
        
            cursor.execute("""INSERT INTO uniquep_table VALUES 
                ('giraffes.io', 'Uber, but with giraffes', 1900),
                ('dronesweaters.com', 'Clothes for cold drones', 3000),
                ('hummingpro.io', 'Online humming courses', 120000)
            """)
            connection.commit()
            # print("File projects.db does not exist. Please run initdb.py.")
            # sys.exit()
        self.conn = QSqlDatabase.addDatabase("QSQLITE")
        self.conn.setDatabaseName("uniquep.db")
        if not self.conn.open():
            sys.exit(1)
        
    def disconnect_db(self):
        if not self.conn.isOpen():
            sys.exit(1)
        self.conn.close()
        QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())

    def load_data(self):
        self.connect_db()
        self.table_model = QSqlQueryModel()
        # self.table_model.setTable("uniquep_table")
        # self.table_model.select()
        self.table_model.setQuery("select * from uniquep_table")
        self.table_view.setModel(self.table_model)
        self.table_view_setup()
        # self.table_view.show()

    # from: https://stackoverflow.com/a/44076057
    def open_file(self):   
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.upload_file_label.setText(fileName)
        # if fileName:
        #     print(fileName)
    def upload(self):
        # upload is a background job
        # use QProgressBar to show progress
        print(QProgressBar)
        # get input (check csv format)
        print(self.upload_input.toPlainText())
        # get current select file (check file(.csv) format and check csv format)
        print(self.upload_file_label.text())
        # parsing with uniquep
        # insert into db
        
def main():
    # only one QApplication instance per application
    # app = QApplication([])
    app = QApplication(sys.argv)

    # window = uic.loadUi("uniquep.ui")
    window = MainWindow()
    # Windows are hidden by default
    window.show()

    # start event loop
    app.exec()

if __name__ == "__main__":
    main()
