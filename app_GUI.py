import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, 
                             QFrame, QInputDialog, QListWidget, QListWidgetItem, 
                             QDialog, QGridLayout)
from PyQt5.QtCore import Qt
from mock_lights import LightController
from live_clock import LiveClock
from vrijeme import Vrijeme
<<<<<<< HEAD
from temperature_recorder import TemperatureMonitor

=======
import emoji_clothes
>>>>>>> b4fe822bec99a737caee5d2750480a176134fdd7

LightController = LightController()
url = "https://vrijeme.hr/hrvatska_n.xml"
vrijeme = Vrijeme(url)
vrijeme.fetch_weather_data()


<<<<<<< HEAD
db_path = "temperatures.db"
temperature_monitor = TemperatureMonitor(db_path)
temperature = temperature_monitor.update_temperatures()


=======
>>>>>>> b4fe822bec99a737caee5d2750480a176134fdd7
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
        self.setGeometry(100, 100, 800, 600)  # Increased the size

        # glavni widget i raspored
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Create a horizontal layout for the clock
        clock_layout = QHBoxLayout()
        # Add stretch to push the clock to the right
        clock_layout.addStretch()
        # Create an instance of LiveClock and add it to the clock layout
        clock = LiveClock()
        clock_layout.addWidget(clock)
        # Add the clock layout to the main layout
        self.main_layout.addLayout(clock_layout)

        self.setCentralWidget(self.main_widget)

        self.emoji = emoji_clothes.get_emoji(float(vrijeme.get_temperature()))

        # izgled glavnog prozora
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

        # linija za razdvajanje
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # naslov
        self.title_label = QLabel("Smart App", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(self.title_label)

        # linija razdvajanja
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # gornji dio sa gumbovima
        self.button_frame = QFrame()
        self.button_layout = QHBoxLayout()
        self.button_frame.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_frame)

        # Gumb 1 - Kišni mod
        self.button1 = QPushButton("Meteo", self)
        self.button1.clicked.connect(self.show_window1)
        self.button_layout.addWidget(self.button1)

        # Gumb 2 - Pametni uređaji
        self.button2 = QPushButton("Pametni uređaji", self)
        self.button2.clicked.connect(self.show_window2)
        self.button_layout.addWidget(self.button2)

        # Gumnb 3 - Rasvjeta
        self.button3 = QPushButton("Rasvjeta", self)
        self.button3.clicked.connect(self.show_window3)
        self.button_layout.addWidget(self.button3)

        # Gumb 4 - Raspored zadataka
        self.button4 = QPushButton("Raspored zadataka", self)
        self.button4.clicked.connect(self.show_window4)
        self.button_layout.addWidget(self.button4)

        # linija za razdvajanje
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # wisget za upravljanje višestrukih zaslona
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Naslovnica
        self.home_screen = QWidget()
        self.home_layout = QVBoxLayout()
        self.home_screen.setLayout(self.home_layout)

        # Unutrašnja temperatura
        self.indoor_label = QLabel(f"Temperatura u kući: {temperature[0]:.1f} °C", self)
        self.indoor_label.setAlignment(Qt.AlignCenter)
        self.home_layout.addWidget(self.indoor_label)

        # Vanjska temperatura
        self.outdoor_label = QLabel(f"Vlažnost zraka u kući: {temperature[1]:.0f} %", self)
        self.outdoor_label.setAlignment(Qt.AlignCenter)
        self.home_layout.addWidget(self.outdoor_label)

        # Gumb za Ažuriranje
        self.update_button = QPushButton("Ažuriraj temperaturu", self)
        self.update_button.clicked.connect(self.update_temperatures)
        self.home_layout.addWidget(self.update_button)

        # Dodavanje naslovnice na widget
        self.stacked_widget.addWidget(self.home_screen)

        # Prozor 1 - Kišni mod (Meteo)
        self.window1 = QWidget()
        self.window1_layout = QVBoxLayout()
        self.window1.setLayout(self.window1_layout)

        # Dodavanje meteo informacija
        self.city_label = QLabel(f"Grad: {vrijeme.get_location()}", self)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.window1_layout.addWidget(self.city_label)

        self.current_temp_label = QLabel(f"Trenutna temperatura: {vrijeme.get_temperature()}°C {self.emoji}", self)
        self.current_temp_label.setAlignment(Qt.AlignCenter)
        self.window1_layout.addWidget(self.current_temp_label)

        self.pressure_label = QLabel(f"Tlak zraka: {vrijeme.get_pressure()} hPa", self)
        self.pressure_label.setAlignment(Qt.AlignCenter)
        self.window1_layout.addWidget(self.pressure_label)

        self.humidity_label = QLabel(f"Vlažnost zraka: {vrijeme.get_humidity()} %", self)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.window1_layout.addWidget(self.humidity_label)

        self.back_button1 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button1.clicked.connect(self.show_home)
        self.window1_layout.addWidget(self.back_button1)
        self.stacked_widget.addWidget(self.window1)

        # Prozor 2 - Pametni uređaji
        self.window2 = QWidget()
        self.window2_layout = QVBoxLayout()
        self.window2.setLayout(self.window2_layout)

        # Lista uređaja
        self.device_list = QListWidget()
        self.device_list.itemClicked.connect(self.show_device_info)
        self.window2_layout.addWidget(self.device_list)

        # Gumb za dodaj uređaj
        self.add_device_button = QPushButton("Dodaj uređaj", self)
        self.add_device_button.clicked.connect(self.add_device)
        self.window2_layout.addWidget(self.add_device_button)

        # Gumb za izbrisi uređaj
        self.delete_device_button = QPushButton("Izbriši uređaj", self)
        self.delete_device_button.clicked.connect(self.delete_device)
        self.window2_layout.addWidget(self.delete_device_button)

        self.back_button2 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button2.clicked.connect(self.show_home)
        self.window2_layout.addWidget(self.back_button2)

        # Dodavanje prozora 2 na widget
        self.stacked_widget.addWidget(self.window2)

        # Prozor 3 - Rasvjeta
        self.window3 = QWidget()
        self.window3_layout = QVBoxLayout()
        self.window3.setLayout(self.window3_layout)

        # Gumbi za rasvjetu
        self.lighting_layout = QGridLayout()
        self.window3.setLayout(self.window3_layout)

        # dodavanje grida na glavni zaslon
        self.window3_layout.addLayout(self.lighting_layout)

        # Naslov i gumbi u 3x2 formatu
        sections = ["Vanjska rasvjeta", "Dnevni boravak", "Balkonska svijetla"]

        for i, section in enumerate(sections):
            title_label = QLabel(section)
            title_label.setContentsMargins(0, 7, 0, 7)  # Reduce the margins by 30%
            self.lighting_layout.addWidget(title_label, i * 2, 0, 1, 2, alignment=Qt.AlignCenter)

            on_button = QPushButton("Uključi", self)
            on_button.setStyleSheet("color: black;")  # Set text color to black
            on_button.clicked.connect(lambda _, row=i: self.on_button_clicked(row))
            self.lighting_layout.addWidget(on_button, i * 2 + 1, 0)

            off_button = QPushButton("Isključi", self)
            off_button.setStyleSheet("color: black;")  # Set text color to black
            off_button.clicked.connect(lambda _, row=i: self.off_button_clicked(row))
            self.lighting_layout.addWidget(off_button, i * 2 + 1, 1)

        self.back_button3 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button3.clicked.connect(self.show_home)
        self.window3_layout.addWidget(self.back_button3)

        # Dodavanje prozora 3 na widget
        self.stacked_widget.addWidget(self.window3)

        # Prozor 4 - Raspored zadataka
        self.window4 = QWidget()
        self.window4_layout = QVBoxLayout()
        self.window4.setLayout(self.window4_layout)

        # Lista zadataka
        self.task_list = QListWidget()
        self.window4_layout.addWidget(self.task_list)

        # Gumb za dodaj zadatak
        self.add_task_button = QPushButton("Dodaj zadatak", self)
        self.add_task_button.clicked.connect(self.add_task)
        self.window4_layout.addWidget(self.add_task_button)

        # Gumb za izbrisi zadatak
        self.delete_task_button = QPushButton("Izbriši zadatak", self)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.window4_layout.addWidget(self.delete_task_button)

        self.back_button4 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button4.clicked.connect(self.show_home)
        self.window4_layout.addWidget(self.back_button4)

        # Dodavanje prozora 4 na widget
        self.stacked_widget.addWidget(self.window4)

        # Dictionary za spremanje informacija
        self.devices = {}
        self.tasks = {}

    def on_button_clicked(self, row):
        for col in range(self.lighting_layout.columnCount()):
            button = self.lighting_layout.itemAtPosition(row * 2 + 1, col).widget()
            if isinstance(button, QPushButton) and button.text() == "Uključi":
                button.setStyleSheet("background-color: yellow; color: black;")  # Set background color to yellow and text color to black
            else:
                button.setStyleSheet("background-color: #4682b4; color: black;")  # Reset background color and text color

    def off_button_clicked(self, row):
        for col in range(self.lighting_layout.columnCount()):
            button = self.lighting_layout.itemAtPosition(row * 2 + 1, col).widget()
            if isinstance(button, QPushButton) and button.text() == "Isključi":
                button.setStyleSheet("background-color: #851c1c; color: black;")  # Set background color to dark red and text color to black
            else:
                button.setStyleSheet("background-color: #4682b4; color: black;")  # Reset background color and text color

    def update_temperatures(self):
        # Generiranje nasumične temperature između 10 i 30 stupnjeva C
        temperature = temperature_monitor.update_temperatures()

        self.indoor_label.setText(f"Unutrašnja temperatura: {temperature[0]:.1f} °C")
        self.outdoor_label.setText(f"Vlažnost u kući: {temperature[1]:.0f} %")


    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)

    def show_window1(self):
        self.stacked_widget.setCurrentWidget(self.window1)

    def show_window2(self):
        self.stacked_widget.setCurrentWidget(self.window2)

    def show_window3(self):
        self.stacked_widget.setCurrentWidget(self.window3)

    def show_window4(self):
        self.stacked_widget.setCurrentWidget(self.window4)

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
                    # Spremanje informacija o uređajima
                    self.devices[device_name] = {"name": device_name, "type": device_type, "room": room}
                    # Dodavanje uređaja na widget listu
                    item = QListWidgetItem(device_name)
                    self.device_list.addItem(item)
                    # Uloga uređaja
                    item.setData(Qt.UserRole, self.devices[device_name])

    def delete_device(self):
        selected_item = self.device_list.currentItem()
        if selected_item:
            device_name = selected_item.data(Qt.UserRole)["name"]
            # Uklanjanje iz dict-a
            if device_name in self.devices:
                del self.devices[device_name]
            # Uklanjanje iz widget liste
            self.device_list.takeItem(self.device_list.row(selected_item))

    def show_device_info(self, item):
        device_info = item.data(Qt.UserRole)
        if device_info:
            info_window = DeviceInfoWindow(device_info)
            info_window.exec_()

    def add_task(self):
        person_name, ok = QInputDialog.getText(self, "Dodaj zadatak", "Unesite ime osobe:")
        if ok:
            task_description, ok = QInputDialog.getText(self, "Dodaj zadatak", "Unesite zadatak:")
            if ok:
                # Spremanje informacija o zadatku
                self.tasks[person_name] = {"name": person_name, "task": task_description}
                # Dodavanje zadatka na widget listu
                item = QListWidgetItem(f"{person_name}: {task_description}")
                self.task_list.addItem(item)
                # Uloga zadatka
                item.setData(Qt.UserRole, self.tasks[person_name])

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            person_name = selected_item.data(Qt.UserRole)["name"]
            # Uklanjanje iz dict-a
            if person_name in self.tasks:
                del self.tasks[person_name]
            # Uklanjanje iz widget liste
            self.task_list.takeItem(self.task_list.row(selected_item))


app = QApplication(sys.argv)

window = SmartHomeApp()
window.show()

# Run the application event loop
sys.exit(app.exec_())
