import sys
from PySide6.QtWidgets import QApplication, QWidget

# Base class of Qt (PySide)
# Process loop events
app = QApplication()
# Creating window object
window = QWidget()
# Modifiying window
window.setWindowTitle('Hello World with PySide')
window.resize(600, 400)
# Show window
window.show()
# Execute app
sys.exit(app.exec())
