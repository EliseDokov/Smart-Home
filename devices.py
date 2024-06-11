from sqlite3 import connect


class Device:
    """
    A class to represent a device and interact with its database table.

    Attributes:
    ------------
    database_path : str
        Path to the SQLite database file.
    device_name : str
        Name of the device which is used as the table name.
    """

    def __init__(self, database_path: str, device_name: str) -> None:
        """
        Initialize the Device class with database path and device name.

        Parameters:
        ------------
        database_path : str
            Path to the SQLite database file.
        device_name : str
            Name of the device which is used as the table name.
        """
        self.database_path = database_path
        self.device_name = device_name
        self.create_table()  # Create table when instantiating class

    @property
    def database_path(self):
        return self._database_path

    @database_path.setter
    def database_path(self, database_path):
        self._database_path = database_path

    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        self._device_name = device_name

    def create_table(self) -> None:
        """
        Create a table for the device if it does not already exist.

        The table will have columns:
        - changed_at: DATETIME, records the timestamp of the change, defaults to the current timestamp.
        - state: TINYINT(1), stores the state of the device (0 or 1).
        """

        # SQL statement to create table with columns: changed_at (being automatic datetime), state (either 0 or 1)
        statement = f"CREATE TABLE IF NOT EXISTS {self.device_name} (changed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, state TINYINT(1) NOT NULL);"

        # Generic try/except/finally block to execute SQL statement
        try:
            connection = connect(self.database_path)
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
        except Exception as e:
            print("Error creating device table:", e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def store_state(self, state: int) -> None:
        """
        Store the state of the device in the database.

        Parameters:
        ------------
        state : int
            The state of the device, should be either 0 or 1.

        Raises:
        ------------
        ValueError
            If the state is not 0 or 1.
        """

        # Check state value (must be either 0 or 1)
        if state not in (0, 1):
            raise ValueError("Device state can be either 0 or 1.")

        # SQL statement to insert device state (datetime value is inserted automatically)
        statement = f"INSERT INTO {self.device_name} (state) VALUES (?);"

        # Generic try/except/finally block to execute SQL statement
        try:
            connection = connect(self.database_path)
            cursor = connection.cursor()
            cursor.execute(statement, (state,))
            connection.commit()
        except Exception as e:
            print("Error storing state:", e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_states(self) -> list[tuple]:
        """
        Fetch all states from the device table in the database.

        This method retrieves all rows from the device table corresponding to
        the device name provided during the instantiation of the class.

        Returns:
        ------------
        list[tuple]
            A list of tuples, where each tuple represents a row in the device table.
            Each tuple contains:
            - changed_at (datetime): The timestamp when the state was changed.
            - state (int): The state of the device (0 or 1).

        Raises:
        ------------
        Exception
            If there is an error in fetching states from the database, an exception is caught and an error message is printed.
        """

        # SQL statement to fetch all rows from table
        statement = f"SELECT * FROM {self.device_name};"

        # Generic try/except/finally block to execute SQL statement
        try:
            connection = connect(self.database_path)
            cursor = connection.cursor()
            cursor.execute(statement)
            selection = cursor.fetchall()
        except Exception as e:
            print("Error fetching states:", e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
            return selection
