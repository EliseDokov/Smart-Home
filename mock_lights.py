import sqlite3
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class LightController:
    def __init__(self, db_file="light_state.db"):
        self.db_file = db_file
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            # Create the table with timestamp column
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS light_state (
                    timestamp TEXT NOT NULL,
                    state TEXT NOT NULL
                )
            """)  # End of CREATE TABLE statement

            cursor.execute('''
                INSERT OR IGNORE INTO light_state (timestamp, state)
                VALUES (?, ?)
            ''', (now, 'off'))

            conn.commit()

    def write_light_state(self, state):
        """
        Records the light state with a timestamp in the SQLite database.

        """

        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            # Insert the state and timestamp into the database
            cursor.execute('INSERT INTO light_state (timestamp, state) VALUES (?, ?)', (now, state))

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



    def read_light_state(self):
        state
        

def main():
    controller = LightController()
    controller.turn_off_light()

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
