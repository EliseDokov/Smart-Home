import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, 
                             QFrame, QInputDialog, QListWidget, QListWidgetItem, 
                             QDialog, QGridLayout)
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
        self.setGeometry(100, 100, 800, 600)  # Increased the size

        # Main widget and layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Apply main window style
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

        # Separator line
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # Title label
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

        # Upper part with buttons
        self.button_frame = QFrame()
        self.button_layout = QHBoxLayout()
        self.button_frame.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_frame)

        # Button 1 - Kišni mod
        self.button1 = QPushButton("Kišni mod", self)
        self.button1.clicked.connect(self.show_window1)
        self.button_layout.addWidget(self.button1)

        # Button 2 - Pametni uređaji
        self.button2 = QPushButton("Pametni uređaji", self)
        self.button2.clicked.connect(self.show_window2)
        self.button_layout.addWidget(self.button2)

        # Button 3 - Rasvjeta
        self.button3 = QPushButton("Rasvjeta", self)
        self.button3.clicked.connect(self.show_window3)
        self.button_layout.addWidget(self.button3)

        # Separator line
        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.separator)

        # Stacked widget to manage multiple screens
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Home screen
        self.home_screen = QWidget()
        self.home_layout = QVBoxLayout()
        self.home_screen.setLayout(self.home_layout)

        # Indoor temperature label
        self.indoor_label = QLabel("Unutrašnja temperatura: -- °C", self)
        self.indoor_label.setAlignment(Qt.AlignCenter)
        self.home_layout.addWidget(self.indoor_label)

        # Outdoor temperature label
        self.outdoor_label = QLabel("Vanjska temperatura: -- °C", self)
        self.outdoor_label.setAlignment(Qt.AlignCenter)
        self.home_layout.addWidget(self.outdoor_label)

        # Update button
        self.update_button = QPushButton("Ažuriraj temperaturu", self)
        self.update_button.clicked.connect(self.update_temperatures)
        self.home_layout.addWidget(self.update_button)

        # Add home screen to stacked widget
        self.stacked_widget.addWidget(self.home_screen)

        # Window 1 - Kišni mod
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

        # Window 2 - Pametni uređaji
        self.window2 = QWidget()
        self.window2_layout = QVBoxLayout()
        self.window2.setLayout(self.window2_layout)

        # Device list widget
        self.device_list = QListWidget()
        self.device_list.itemClicked.connect(self.show_device_info)
        self.window2_layout.addWidget(self.device_list)

        # Add device button
        self.add_device_button = QPushButton("Dodaj uređaj", self)
        self.add_device_button.clicked.connect(self.add_device)
        self.window2_layout.addWidget(self.add_device_button)

        self.back_button2 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button2.clicked.connect(self.show_home)
        self.window2_layout.addWidget(self.back_button2)

        # Add window 2 to stacked widget
        self.stacked_widget.addWidget(self.window2)

        # Window 3 - Rasvjeta
        self.window3 = QWidget()
        self.window3_layout = QVBoxLayout()
        self.window3.setLayout(self.window3_layout)

        # Lighting control buttons
        self.lighting_layout = QGridLayout()
        self.window3.setLayout(self.window3_layout)
        
        # Add grid layout to the main layout of window3
        self.window3_layout.addLayout(self.lighting_layout)
        
        # Add the buttons in a 3x2 grid format
        for i in range(3):
            on_button = QPushButton("Uključi", self)
            self.lighting_layout.addWidget(on_button, i, 0)
            
            off_button = QPushButton("Isključi", self)
            self.lighting_layout.addWidget(off_button, i, 1)

        self.back_button3 = QPushButton("Povratak na glavni izbornik", self)
        self.back_button3.clicked.connect(self.show_home)
        self.window3_layout.addWidget(self.back_button3)

        # Add window 3 to stacked widget
        self.stacked_widget.addWidget(self.window3)

        # Dictionary to store device information
        self.devices = {}

    def update_temperatures(self):
        # Generate a random indoor temperature between 10 and 30
        indoor_temp = random.uniform(10.0, 30.0)

        # Generate a corresponding outdoor temperature such that the difference is at most 10 degrees
        min_outdoor_temp = max(-10.0, indoor_temp - 10)
        max_outdoor_temp = min(40.0, indoor_temp + 10)
        outdoor_temp = random.uniform(min_outdoor_temp, max_outdoor_temp)

        # Update labels
        self.indoor_label.setText(f"Unutrašnja temperatura: {indoor_temp:.2f} °C")
        self.outdoor_label.setText(f"Vanjska temperatura: {outdoor_temp:.2f} °C")

    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)

    def show_window1(self):
        self.stacked_widget.setCurrentWidget(self.window1)

    def show_window2(self):
        self.stacked_widget.setCurrentWidget(self.window2)

    def show_window3(self):
        self.stacked_widget.setCurrentWidget(self.window3)

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
                    # Store device information
                    self.devices[device_name] = {"name": device_name, "type": device_type, "room": room}
                    # Add device to list widget
                    item = QListWidgetItem(device_name)
                    self.device_list.addItem(item)
                    # Set data role to store device information
                    item.setData(Qt.UserRole, self.devices[device_name])

    def show_device_info(self, item):
        device_info = item.data(Qt.UserRole)
        if device_info:
            info_window = DeviceInfoWindow(device_info)
            info_window.exec_()

# Create the application object
app = QApplication(sys.argv)

# Create an instance of our main window
window = SmartHomeApp()
window.show()

# Run the application event loop
sys.exit(app.exec_())
