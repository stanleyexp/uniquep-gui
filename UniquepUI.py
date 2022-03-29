# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uniquep.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 458)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.insert_all_btn = QtWidgets.QPushButton(self.tab)
        self.insert_all_btn.setObjectName("insert_all_btn")
        self.gridLayout_3.addWidget(self.insert_all_btn, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_btn = QtWidgets.QPushButton(self.tab)
        self.prev_btn.setObjectName("prev_btn")
        self.horizontalLayout.addWidget(self.prev_btn)
        self.next_btn = QtWidgets.QPushButton(self.tab)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.jump_btn = QtWidgets.QPushButton(self.tab)
        self.jump_btn.setObjectName("jump_btn")
        self.horizontalLayout.addWidget(self.jump_btn)
        self.pagenum_spinbox = QtWidgets.QSpinBox(self.tab)
        self.pagenum_spinbox.setObjectName("pagenum_spinbox")
        self.horizontalLayout.addWidget(self.pagenum_spinbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.page_label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.page_label.setFont(font)
        self.page_label.setText("")
        self.page_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.page_label.setObjectName("page_label")
        self.verticalLayout_2.addWidget(self.page_label)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 4, 0, 1, 1)
        self.table_view = QtWidgets.QTableView(self.tab)
        self.table_view.setObjectName("table_view")
        self.gridLayout_3.addWidget(self.table_view, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search_input = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search_input.setFont(font)
        self.search_input.setText("")
        self.search_input.setObjectName("search_input")
        self.gridLayout_2.addWidget(self.search_input, 0, 0, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.tab)
        self.search_btn.setStyleSheet("")
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_2.addWidget(self.search_btn, 0, 1, 1, 1)
        self.download_btn = QtWidgets.QPushButton(self.tab)
        self.download_btn.setObjectName("download_btn")
        self.gridLayout_2.addWidget(self.download_btn, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.delete_all_btn = QtWidgets.QPushButton(self.tab)
        self.delete_all_btn.setObjectName("delete_all_btn")
        self.gridLayout_3.addWidget(self.delete_all_btn, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 441, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.upload_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.upload_btn.setObjectName("upload_btn")
        self.gridLayout.addWidget(self.upload_btn, 2, 1, 1, 1)
        self.upload_input = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.upload_input.setPlainText("")
        self.upload_input.setObjectName("upload_input")
        self.gridLayout.addWidget(self.upload_input, 0, 0, 1, 2)
        self.select_file_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.select_file_btn.setObjectName("select_file_btn")
        self.gridLayout.addWidget(self.select_file_btn, 2, 0, 1, 1)
        self.upload_file_label = QtWidgets.QLabel(self.layoutWidget)
        self.upload_file_label.setObjectName("upload_file_label")
        self.gridLayout.addWidget(self.upload_file_label, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "uniquep"))
        self.insert_all_btn.setText(_translate("Form", "insert all"))
        self.prev_btn.setText(_translate("Form", "prev page"))
        self.next_btn.setText(_translate("Form", "next page"))
        self.jump_btn.setText(_translate("Form", "jump to"))
        self.search_input.setPlaceholderText(_translate("Form", "input your word"))
        self.search_btn.setText(_translate("Form", "search"))
        self.download_btn.setText(_translate("Form", "download"))
        self.delete_all_btn.setText(_translate("Form", "delete all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "up search"))
        self.upload_btn.setText(_translate("Form", "upload"))
        self.upload_input.setPlaceholderText(_translate("Form", "input csv format"))
        self.select_file_btn.setText(_translate("Form", "select file"))
        self.upload_file_label.setText(_translate("Form", "xxx.file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "up upload"))
