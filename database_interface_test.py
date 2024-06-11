from random import uniform
from time import sleep

from devices import Device
from sensors import Sensor


def main():
    # ----------------------------------------
    # Demo for working with classes/databases
    # ----------------------------------------

    # Instantiate Device and Sensor classes (along with their database/tables)
    vacuum_cleaner = Device("smart_home.db", "vacuum_cleaner")
    temperature_sensor = Sensor("smart_home.db", "temperature")

    # Mock generate some data
    for _ in range(20):
        temperatures = (round(uniform(20.0, 20.5), 1), round(uniform(25.0, 25.5), 1))
        temperature_sensor.store_measurements(temperatures)
        sleep(5)
        vacuum_cleaner.store_state(1)
        sleep(5)
        vacuum_cleaner.store_state(0)
        sleep(5)

    # Fetch rows from tables
    print(vacuum_cleaner.get_states())
    print(temperature_sensor.get_measurements())


if __name__ == "__main__":
    main()
