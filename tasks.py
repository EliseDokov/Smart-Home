import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt

def create_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_db()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Raspored aktivnosti stanara")
        self.setGeometry(100, 100, 600, 400)

        self.tasks = {}

        # Glavni widget i layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Lista zadataka
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Gumb za dodaj zadatak
        self.add_task_button = QPushButton("Dodaj zadatak", self)
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        # Gumb za izbrisi zadatak
        self.delete_task_button = QPushButton("Izbriši zadatak", self)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_task_button)

        # Učitaj zadatke iz baze podataka
        self.load_tasks()

    def add_task(self):
        person_name, ok = QInputDialog.getText(self, "Dodaj zadatak", "Unesite ime osobe:")
        if ok:
            task_description, ok = QInputDialog.getText(self, "Dodaj zadatak", "Unesite zadatak:")
            if ok:
                # Spremanje informacija o zadatku u bazu podataka
                conn = sqlite3.connect('tasks.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO tasks (name, task) VALUES (?, ?)
                ''', (person_name, task_description))
                conn.commit()
                conn.close()

                # Dodavanje zadatka na widget listu
                item = QListWidgetItem(f"{person_name}: {task_description}")
                self.task_list.addItem(item)
                # Uloga zadatka
                self.tasks[person_name] = {"name": person_name, "task": task_description}
                item.setData(Qt.UserRole, self.tasks[person_name])

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            person_name = selected_item.data(Qt.UserRole)["name"]
            # Uklanjanje iz dict-a
            if person_name in self.tasks:
                del self.tasks[person_name]

            # Uklanjanje iz baze podataka
            conn = sqlite3.connect('tasks.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE name = ? AND task = ?', (person_name, selected_item.data(Qt.UserRole)["task"]))
            conn.commit()
            conn.close()

            # Uklanjanje iz widget liste
            self.task_list.takeItem(self.task_list.row(selected_item))

    def load_tasks(self):
        # Učitavanje zadataka iz baze podataka
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, task FROM tasks')
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            person_name, task_description = row
            item = QListWidgetItem(f"{person_name}: {task_description}")
            self.task_list.addItem(item)
            self.tasks[person_name] = {"name": person_name, "task": task_description}
            item.setData(Qt.UserRole, self.tasks[person_name])

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
