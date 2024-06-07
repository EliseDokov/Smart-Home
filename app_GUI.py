import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QFrame, QInputDialog, QListWidget, QListWidgetItem, QMessageBox, QDialog
from PyQt5.QtCore import Qt

class DeviceInfoWindow(QDialog):
    def __init__(self, device_info):
        super().__init__()
        self.setWindowTitle(device_info["name"])
        self.setGeometry(100, 100, 300, 200)  # x, y, width, height

        layout = QVBoxLayout()

        name_label = QLabel(f"Name: {device_info['name']}", self)
        layout.addWidget(name_label)

        type_label = QLabel(f"Type: {device_info['type']}", self)
        layout.addWidget(type_label)

        room_label = QLabel(f"Room: {device_info['room']}", self)
        layout.addWidget(room_label)

        self.setLayout(layout)

class SmartHomeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart App")
        self.setGeometry(100, 100, 600, 400)  # x, y, širina, visina

        # Glavni widget i izgled
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Izgled glavnog prozora
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f8ff;
            }
            QLabel {
                font-size: 16px;
                color: #333333;
            }
            QPushButton {
                font-size: 14px;
                padding: 10px;
                background-color: #4682b4;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5a9bd4;
            }
            QFrame#separator {
                background-color: #f0f8ff;
                height: 2px;
            }
        """)

        # Separator crta
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # Label za naslov
        self.title_label = QLabel("Smart App", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(self.title_label)

        # Separator line
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # Gornji dio s gumbovima
        self.button_frame = QFrame()
        self.button_layout = QHBoxLayout()
        self.button_frame.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_frame)

        # Dugme 1 - Kišni mod
        self.button1 = QPushButton("Kišni mod", self)
        self.button1.clicked.connect(self.show_window1)
        self.button_layout.addWidget(self.button1)

        # Dugme 2 - Pametni uređaji
        self.button2 = QPushButton("Pametni uređaji", self)
        self.button2.clicked.connect(self.show_window2)
        self.button_layout.addWidget(self.button2)

        # Separator crta
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # Widget za više screenova
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Naslovnica
        self.home_screen = QWidget()
        self.home_layout = QVBoxLayout()
        self.home_screen.setLayout(self.home_layout)

        # Unutrašnja temperatura label
        self.indoor_label = QLabel("Unutrašnja temperatura: -- °C", self)
        self.indoor_label.setAlignment(Qt.AlignCenter)
        self.home_layout.addWidget(self.indoor_label)

        # Vanjska temperatura label
        self.outdoor_label = QLabel("Vanjska temperatura: -- °C", self)
        self.outdoor_label.setAlignment(Qt.AlignCenter)
        self.home_layout.addWidget(self.outdoor_label)

        # Dugme za ažuriranje
        self.update_button = QPushButton("Ažuriraj temperaturu", self)
        self.update_button.clicked.connect(self.update_temperatures)
        self.home_layout.addWidget(self.update_button)

        # Dodavanje naslovnice na widget
        self.stacked_widget.addWidget(self.home_screen)

        # Prozor 1 - Kišni mod
        self.window1 = QWidget()
        self.window1_layout = QVBoxLayout()
        self.window1.setLayout(self.window1_layout)
        self.shutter_button = QPushButton("Otvori rolete", self)
        self.shutter_button.clicked.connect(self.toggle_shutters)
        self.window1_layout.addWidget(self.shutter_button)
        self.weather_label = QLabel("Izvještaj vremena: --", self)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.window1_layout.addWidget(self.weather_label)
        self.back_button1 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button1.clicked.connect(self.show_home)
        self.window1_layout.addWidget(self.back_button1)
        self.stacked_widget.addWidget(self.window1)

        # Prozor 2 - Pametni uređaji
        self.window2 = QWidget()
        self.window2_layout = QVBoxLayout()
        self.window2.setLayout(self.window2_layout)

        # Lista uređaja preko widgeta
        self.device_list = QListWidget()
        self.device_list.itemClicked.connect(self.show_device_info)
        self.window2_layout.addWidget(self.device_list)

        # Dugme za dodati uređaj
        self.add_device_button = QPushButton("Dodaj uređaj", self)
        self.add_device_button.clicked.connect(self.add_device)
        self.window2_layout.addWidget(self.add_device_button)

        self.back_button2 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button2.clicked.connect(self.show_home)
        self.window2_layout.addWidget(self.back_button2)

        # Dodavanje drugog prozora na stack widget
        self.stacked_widget.addWidget(self.window2)

        # Dictionary za spremanje informacija
        self.devices = {}

    def update_temperatures(self):
        # Generiranje unutarnje temperature između 10 i 30 stupnjeva
        indoor_temp = random.uniform(10.0, 30.0)

        # Generiranje odgovarajuće vanjske temperature
        min_outdoor_temp = max(-10.0, indoor_temp - 10)
        max_outdoor_temp = min(40.0, indoor_temp + 10)
        outdoor_temp = random.uniform(min_outdoor_temp, max_outdoor_temp)

        # Ažuriranje labela
        self.indoor_label.setText(f"Unutrašnja temperatura: {indoor_temp:.2f} °C")
        self.outdoor_label.setText(f"Vanjska temperatura: {outdoor_temp:.2f} °C")

    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)

    def show_window1(self):
        self.stacked_widget.setCurrentWidget(self.window1)

    def show_window2(self):
        self.stacked_widget.setCurrentWidget(self.window2)

    def toggle_shutters(self):
        if self.shutter_button.text() == "Otvori rolete":
            self.shutter_button.setText("Zatvori rolete")
        else:
            self.shutter_button.setText("Otvori rolete")

    def add_device(self):
        device_name, ok = QInputDialog.getText(self, "Dodaj uređaj", "Unesite ime uređaja:")
        if ok:
            device_type, ok = QInputDialog.getText(self, "Dodaj uređaj", "Unesite vrstu uređaja:")
            if ok:
                room, ok = QInputDialog.getText(self, "Dodaj uređaj", "Unesite prostoriju za korištenje:")
                if ok:
                # Spremanje informacija od uređaja
                    self.devices[device_name] = {"name": device_name, "type": device_type, "room": room}
                # Dodavanje uređaja na widget listu
                    item = QListWidgetItem(device_name)
                    self.device_list.addItem(item)
                # spremanje informacija o uređajima
                    item.setData(Qt.UserRole, self.devices[device_name])

    def show_device_info(self, item):
        device_info = item.data(Qt.UserRole)
        if device_info:
            info_window = DeviceInfoWindow(device_info)
            info_window.exec_()
        
        
# stvaranje objekta
app = QApplication(sys.argv)

# glavni prozor
window = SmartHomeApp()
window.show()


sys.exit(app.exec_())