from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
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
        self.total_page = None
        self.total_count = None
        self.count_per_page = 10
        self.curr_page = 1
        self.setupUi(self)
        self.table_model = QSqlQueryModel()
        self.table_view.setModel(self.table_model)
        self.pagenum_spinbox.setRange(0, 2**31 - 1)
        self.search_btn.clicked.connect(self.search)
        self.download_btn.clicked.connect(self.download)
        self.select_file_btn.clicked.connect(self.open_file)
        self.upload_btn.clicked.connect(self.upload)
        self.prev_btn.clicked.connect(self.prev_page)
        self.next_btn.clicked.connect(self.next_page)
        self.jump_btn.clicked.connect(self.jump_page)
        self.load_data()
        

        # temp test
        self.delete_all_btn.clicked.connect(self.delete_all)
        self.insert_all_btn.clicked.connect(self.insert_all)
    def delete_all(self):
        pass
    def insert_all(self):
        pass
    def jump_page(self):
        if self.pagenum_spinbox.value() > self.total_page:
            self.pagenum_spinbox.setValue(self.total_page)
        self.curr_page = self.pagenum_spinbox.value()
        self.query_page(self.curr_page)
    def prev_page(self):
        self.curr_page = self.curr_page - 1
        self.query_page(self.curr_page)
    def next_page(self):
        self.curr_page = self.curr_page + 1
        self.query_page(self.curr_page)
    def query_page(self, page=1):
        # prevent sql injection
        query = QSqlQuery()
        sql = """
            select * from uniquep_table
            where rowid > ? limit ?
        """
        offset = (page - 1) * self.count_per_page
        query.prepare(sql)
        query.addBindValue(offset)
        query.addBindValue(self.count_per_page)
        query.exec()
        self.table_model.setQuery(query)
        # print(f"offset {offset}")
        # print(f"self.table_model.rowCount() {self.table_model.rowCount()}")
        self.table_view_setup()
        self.uppate_page_status()

    def uppate_page_status(self):
        self.page_label.setText(f'curr:{str(self.curr_page)} total{str(self.total_page)}')
        if self.curr_page < 2:
            self.prev_btn.setEnabled(False)
        else:
            self.prev_btn.setEnabled(True)

        if self.curr_page >= self.total_page:
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
        # self.table_model.setHeaderData(0, Qt.Horizontal, "url")
        # self.table_model.setHeaderData(1, Qt.Horizontal, "descr")
        # self.table_model.setHeaderData(2, Qt.Horizontal, "income")
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
                ('hummingpro.io', 'Online humming courses', 120000),
                ('hummingpro.io', 'Online humming courses', 120001),
                ('hummingpro.io', 'Online humming courses', 120002),
                ('hummingpro.io', 'Online humming courses', 120003),
                ('hummingpro.io', 'Online humming courses', 120004),
                ('hummingpro.io', 'Online humming courses', 120005),
                ('hummingpro.io', 'Online humming courses', 120006),
                ('hummingpro.io', 'Online humming courses', 120007),
                ('hummingpro.io', 'Online humming courses', 120008),
                ('hummingpro.io', 'Online humming courses', 120009),
                ('hummingpro.io', 'Online humming courses', 120010),
                ('hummingpro.io', 'Online humming courses', 120011),
                ('hummingpro.io', 'Online humming courses', 120012),
                ('hummingpro.io', 'Online humming courses', 120013),
                ('hummingpro.io', 'Online humming courses', 120014),
                ('hummingpro.io', 'Online humming courses', 120015),
                ('hummingpro.io', 'Online humming courses', 120016),
                ('hummingpro.io', 'Online humming courses', 120017),
                ('hummingpro.io', 'Online humming courses', 120018),
                ('hummingpro.io', 'Online humming courses', 120019),
                ('hummingpro.io', 'Online humming courses', 120020),
                ('hummingpro.io', 'Online humming courses', 120021),
                ('hummingpro.io', 'Online humming courses', 120022),
                ('hummingpro.io', 'Online humming courses', 120023),
                ('hummingpro.io', 'Online humming courses', 120024),
                ('hummingpro.io', 'Online humming courses', 120025),
                ('hummingpro.io', 'Online humming courses', 120026),
                ('hummingpro.io', 'Online humming courses', 120027),
                ('hummingpro.io', 'Online humming courses', 120028),
                ('hummingpro.io', 'Online humming courses', 120029)
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
        # connection pool ?
        self.connect_db()
        # self.table_model.setTable("uniquep_table")
        # self.table_model.select()
        self.table_model.setQuery("select * from uniquep_table")
        self.total_count = self.table_model.rowCount()
        # print(f"self.total_count {self.total_count}")
        if self.total_count % self.count_per_page == 0:
            self.total_page = self.total_count / self.count_per_page
        else:
            self.total_page = int(self.total_count / self.count_per_page) + 1
        # print(f"self.total_page {self.total_page}")
        self.query_page()
        # self.table_view_setup()
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
        # begin transaction
        # insert into db
        # commit transaction
        
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
