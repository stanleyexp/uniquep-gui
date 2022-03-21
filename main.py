from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QMainWindow,
    QLabel,
    QLineEdit,
    QMenu,
    QAction,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QProgressBar,
    QRadioButton,
    QSpinBox,
    QGridLayout,
    QStackedLayout,
    QTabWidget
)
"""
1.search/download/upload -> async?
2. two pages => search page and upload page
3. can handle search and upaload at the same time

"""
import sys
class Search(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.btn = QPushButton("Press me")
        layout.addWidget(self.btn)
        # self.setStyleSheet("background-color:green;")
        
    
class Upload(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.btn = QPushButton("Presss me 2")
        layout.addWidget(self.btn)
        # self.setStyleSheet("background-color:red;")
        
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("uniquep")
        self.main_layout = QStackedLayout()
        


        self.label = QLabel("OK I am Label")
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        # Qt.AlignHCenter
        # Qt.AlignJustify
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.input = QLineEdit()
        # self.input.setMaxLength(10)
        self.input.setPlaceholderText("Enter your text")
        self.input.returnPressed.connect(self.return_pressed)
        # self.input.textChanged.connect(self.label.setText)
        # self.input.textChanged.connect(self.text_changed)
        self.input.textEdited.connect(self.text_edited)


        # QGridLayout
        # QGridLayout.addWidget(QWidget)
        # QGridLayout.addWidget(QWidget, int row, int column, Qt.Alignment alignment=0)
        # QGridLayout.addWidget(QWidget, int row, int column, int rowSpan, int columnSpan, Qt.Alignment alignment=0)
        self.button_is_checked = True
        self.button = QPushButton("press me")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)
        inside_layout1 = QHBoxLayout()
        # inside_layout1.setContentsMargins(0, 0, 0, 0)
        # inside_layout1.setSpacing(20)
        inside_layout2 = QHBoxLayout()
        layout = QVBoxLayout()
        inside_layout1.addWidget(self.input)
        inside_layout2.addWidget(self.label)
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        checkBox = QCheckBox()
        layout.addWidget(checkBox)
        checkBox.setCheckState(Qt.Checked) # Qt.Unchecked
        checkBox.stateChanged.connect(self.checkbox_state)
        self.combox = QComboBox()
        layout.addWidget(self.combox)
        self.combox.addItems(["Option1", "Option2", "Option3"])
        # Sends the current index (position) of the selected item.
        self.combox.currentIndexChanged.connect(self.combox_index_state)
        # There is an alternate signal to send the text.
        self.combox.currentTextChanged.connect(self.combox_text_state)
        widgets = [
            # QCheckBox,
            # QComboBox,
            # QDateEdit,
            # QDateTimeEdit,
            # QDial,
            # QDoubleSpinBox,
            # QFontComboBox,
            # QLCDNumber,
            # QLabel,
            # QLineEdit,
            QProgressBar,
            # QPushButton,
            # QRadioButton,
            # QSlider,
            # QSpinBox,
            # QTimeEdit,
        ]
        for w in widgets:
            layout.addWidget(w())

        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        layout.addLayout(inside_layout1)
        layout.addLayout(inside_layout2)
        container1 = QWidget()
        container1.setLayout(layout)
        self.main_layout.addWidget(container1)
        # Set the central widget of the Window.
        self.setCentralWidget(container1)
        # self.setCentralWidget(self.main_layout)

        # self.setFixedSize(QSize(400, 300))
        # self.setMaximumSize(QSize(400, 300))
        # self.setCentralWidget(self.button)
    
    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEvent")

    # mouse right click to call the menu (contextMenuEvent, original event handler)
    # def contextMenuEvent(self, e):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(e.globalPos())
    def return_pressed(self):
        print("Return pressed!")
        self.input.setText("BOOM!")

    # def text_changed(self, s):
    #     print("Text changed...")
    #     print(s)
    def text_edited(self, s):
        print("Text edited...")
        print(s)
    def combox_index_state(self, s):
        print(s)
        # print(str(self.combox.currentText())) # get option text
    def combox_text_state(self, s):
        print("current option text", s)
    def checkbox_state(self, s):
        pass
        # print(s == Qt.Checked)
        # print(s)
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        # disabled
        self.button.setEnabled(False)
        print("Clicked!")
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        # print("Checked?", checked)
        print(self.button_is_checked)

class MainWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(400, 500)
        self.btn1 = QPushButton("Search")
        self.btn2 = QPushButton("Upload")
        wid1 = Search()
        wid2 = Upload()
        container = QWidget()
        self.main_layout = QStackedLayout()
        container.setLayout(self.main_layout)
        self.main_layout.addWidget(wid1)
        self.main_layout.addWidget(wid2)

        layout = QVBoxLayout()
        layout.addWidget(container)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)

        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)
        
    def btn1_clicked(self):
        self.main_layout.setCurrentIndex(0)
    def btn2_clicked(self):
        self.main_layout.setCurrentIndex(1)

class MainWindow3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test2")
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        wid1 = Search()
        wid2 = Upload()
        tabs.addTab(wid1, "search")
        tabs.addTab(wid2, "upload")
        layout.addWidget(tabs)


        

# only one QApplication instance per application
# app = QApplication([])
app = QApplication(sys.argv)
# window = MainWindow()
# window = MainWindow2()
window = MainWindow3()


# Windows are hidden by default
window.show()

# start event loop
app.exec()
