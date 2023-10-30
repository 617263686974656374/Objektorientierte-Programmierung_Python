
from MainWindow_c import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mietwagen_verwaltung = Car_rental_management()
    sys.exit(app.exec())

