
from PyQt5.QtWidgets import QApplication, QWidget
import sys

# only one QApplication instance per application
# app = QApplication([])
app = QApplication(sys.argv)
window = QWidget()

# Windows are hidden by default
window.show()

# start event loop
app.exec()
# sys.exit(app.exec_())
