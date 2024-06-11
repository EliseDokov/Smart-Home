import sqlite3

class LightController:
    def __init__(self, db_file="light_state.db"):
        self.db_file = db_file
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS light_state (
                    id INTEGER PRIMARY KEY,
                    state TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                INSERT OR IGNORE INTO light_state (id, state)
                VALUES (1, 'off')
            ''')
            conn.commit()

    def read_light_state(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT state FROM light_state WHERE id = 1')
            state = cursor.fetchone()[0]
            return state

    def write_light_state(self, state):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE light_state SET state = ? WHERE id = 1', (state,))
            conn.commit()

    def turn_on_light(self):
        self.write_light_state("on")
        print("The light is turned on.")

    def turn_off_light(self):
        self.write_light_state("off")
        print("The light is turned off.")

    def check_light_state(self):
        state = self.read_light_state()
        print(f"The light is currently {state}.")
        return state

def main():
    controller = LightController()

    while True:
        action = input("Enter action (on/off/check/quit): ").strip().lower()

        if action == "on":
            controller.turn_on_light()
        elif action == "off":
            controller.turn_off_light()
        elif action == "check":
            controller.check_light_state()
        elif action == "quit":
            print("Exiting the light controller.")
            break
        else:
            print("Invalid action. Please enter 'on', 'off', 'check', or 'quit'.")

if __name__ == "__main__":
    main()