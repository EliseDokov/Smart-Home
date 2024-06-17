import random
import sqlite3

class TemperatureMonitor:
    def __init__(self, db_path):
        self.db_path = db_path

    def update_temperatures(self):
        # Generate random temperatures
        indoor_temp = random.uniform(10.0, 30.0)
        min_outdoor_temp = max(-10.0, indoor_temp - 10)
        max_outdoor_temp = min(50.0, indoor_temp + 20)
        humidity = random.uniform(min_outdoor_temp, max_outdoor_temp)

        # **For GUI Applications:** If you're using a GUI framework, replace the following with logic to update your visual labels:
        # self.indoor_label.setText(f"Unutrašnja temperatura: {indoor_temp:.2f} °C")
        # self.outdoor_label.setText(f"Vanjska temperatura: {outdoor_temp:.2f} °C")

        # Simulate label updates (optional):
        print(f"Unutrašnja temperatura: {indoor_temp:.2f} °C")
        print(f"Vlaznost zraka: {humidity:.2f} %")

        # Record temperatures to database
        self._record_temperatures(indoor_temp, humidity)
        return indoor_temp, humidity

    def _record_temperatures(self, indoor_temp, humidity):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Create table if it doesn't exist (replace with your desired column names)
            cursor.execute("""CREATE TABLE IF NOT EXISTS temperature_data (
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                indoor_temp REAL,
                humidity REAL
            )""")

            # Insert temperatures
            sql = "INSERT INTO temperature_data (indoor_temp, humidity) VALUES (?, ?)"
            cursor.execute(sql, (indoor_temp, humidity))

            connection.commit()
            print("Temperature and humidity recorded successfully")
        except sqlite3.Error as err:
            print(f"Error recording temperatures: {err}")
        finally:
            if connection:
                connection.close()


# Example usage (replace with your desired database filename)
db_path = "temperatures.db"


if __name__ == '__main__':
    temperature_monitor = TemperatureMonitor(db_path)
    # temperature_monitor.update_temperatures()
    temperature = temperature_monitor.update_temperatures()
    print(f"{temperature[0]:.1f}")
    print(f"{temperature[1]:.1f}")
