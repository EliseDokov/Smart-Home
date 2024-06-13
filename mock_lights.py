import sqlite3
import datetime
from devices import Device

class LightController:
    def __init__(self, device):
        self.device = device

    def turn_on_light(self):
        self.device.store_state(1)
        print("The light is turned on.")

    def turn_off_light(self):
        self.device.store_state(0)
        print("The light is turned off.")

    def check_light_state(self):
        state = self.device.get_states()
        print(f"The light is currently {state}.")
        return state

    def read_light_state(self):
        state


def main():
    controller = LightController(Device)

    while True:
        action = input("Enter action (on/off/check/quit): ").strip().lower()

        if action == "on":
            controller.turn_on_light()
        elif action == "off":
            controller.turn_off_light()
        elif action == "check":
            controller.check_light_state() ##currently not working
        elif action == "quit":
            print("Exiting the light controller.")
            break
        else:
            print("Invalid action. Please enter 'on', 'off', 'check', or 'quit'.")


if __name__ == "__main__":
    main()
