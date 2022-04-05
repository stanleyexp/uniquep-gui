from ast import keyword
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
from contextlib import closing

class MainWindow(QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.conn_name = "uniquep.db"
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
        self.count_sql = """
            SELECT COUNT(*) FROM uniquep_table
        """
        self.page_sql = """
            SELECT * FROM uniquep_table
            WHERE rowid > ? LIMIT ?
        """
        self.keyword = ''
        self.load_data()
        
        
        # temp test
        self.delete_all_btn.clicked.connect(self.delete_all)
        self.insert_all_btn.clicked.connect(self.insert_all)
    def closeEvent(self, event): # close window
        self.disconnect_db()
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
        query = QSqlQuery(self.conn_name)
        offset = (page - 1) * self.count_per_page
        query.prepare(self.page_sql)
        if self.keyword:
            query.addBindValue(self.keyword)
        query.addBindValue(offset)
        query.addBindValue(self.count_per_page)
        query.exec()
        self.table_model.setQuery(query)
        self.table_view_setup()
        self.uppate_page_status()

    def uppate_page_status(self):
        self.page_label.setText(f'curr: {str(self.curr_page)} total: {str(self.total_page)}')
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
        self.table_view.verticalHeader().setVisible(False)
    def search(self):
        input = self.search_input.text().strip()
        # from https://github.com/simonw/datasette/issues/651#issuecomment-579675357
        bits = input.split()
        input = ' '.join('"{}"'.format(bit.replace('"', '')) for bit in bits)
        query = QSqlQuery(self.conn_name)
        self.keyword = input
        if self.keyword:
            self.keyword = self.keyword + ' *'  # prefix search (sqlite fts5)
            self.count_sql = """
                SELECT COUNT(*) FROM uniquep_vtable WHERE uniquep_vtable MATCH ?
            """
            query.prepare(self.count_sql)
            query.addBindValue(self.keyword)
            self.page_sql="""
                SELECT url, descr, income FROM
                    (SELECT  ROW_NUMBER() OVER(ORDER BY rowid) rownum, * FROM uniquep_vtable WHERE uniquep_vtable MATCH ?)
                WHERE rownum > ? LIMIT ?
            """
        else:
            self.count_sql = """
                SELECT COUNT(*) FROM uniquep_table
            """
            query.prepare(self.count_sql)
            self.page_sql="""
                SELECT * FROM uniquep_table
                WHERE rowid > ? LIMIT ?
            """
        
        
        query.exec()
        self.total_count = query.value(0) if query.next() else 0
        # print(f"search self.total_count {self.total_count}")
        # self.table_model.setQuery(query)
        # self.total_count = self.table_model.rowCount()
        if self.total_count % self.count_per_page == 0:
            self.total_page = int(self.total_count / self.count_per_page)
        else:
            self.total_page = int(self.total_count / self.count_per_page) + 1

        self.query_page()

    
    def download(self):
        print("download search result")
    def connect_db(self):
        if not exists(self.conn_name):
            # init db
            
            with sqlite3.connect(self.conn_name) as connection:
                with closing(connection.cursor()) as cursor:
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
                    cursor.execute("""
                        CREATE VIRTUAL TABLE uniquep_vtable USING FTS5(url, descr, income);
                    """)
                    cursor.execute("""
                        INSERT INTO uniquep_vtable SELECT url, descr, income from uniquep_table;
                    """)
                    connection.commit()
           
        self.conn = QSqlDatabase.addDatabase("QSQLITE")
        self.conn.setDatabaseName(self.conn_name)
        if not self.conn.open():
            sys.exit(1)
        
    def disconnect_db(self):
        if not self.conn.isOpen():
            sys.exit(1)
        self.conn.close()
        QSqlDatabase.removeDatabase(self.conn_name)

    def load_data(self):
        # connection pool ?
        self.connect_db()
        # self.table_model.setTable("uniquep_table")
        # self.table_model.select()
        # self.table_model.setQuery("select * from uniquep_table")
        # self.total_count = self.table_model.rowCount()
        query = QSqlQuery(self.conn_name)
        query.prepare(self.count_sql)
        # print(f"self.count_sql {self.count_sql}")
        query.exec()
        self.total_count = query.value(0) if query.next() else 0
        # print(f"self.total_count {self.total_count}")
        if self.total_count % self.count_per_page == 0:
            self.total_page = int(self.total_count / self.count_per_page)
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
