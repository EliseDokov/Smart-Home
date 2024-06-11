from sqlite3 import connect


class Sensor:
    """
    A class to represent a sensor and interact with its database table.

    Attributes:
    ------------
    database_path : str
        Path to the SQLite database file.
    sensor_name : str
        Name of the sensor which is used as the table name.
    """

    def __init__(self, database_path: str, sensor_name: str) -> None:
        """
        Initialize the Sensor class with database path and sensor name.

        Parameters:
        ------------
        database_path : str
            Path to the SQLite database file.
        sensor_name : str
            Name of the sensor which is used as the table name.
        """
        self.database_path = database_path
        self.sensor_name = sensor_name
        self.create_table()  # Create table when instantiating class

    @property
    def database_path(self):
        return self._database_path

    @database_path.setter
    def database_path(self, database_path):
        self._database_path = database_path

    @property
    def sensor_name(self):
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, sensor_name):
        self._sensor_name = sensor_name

    def create_table(self) -> None:
        """
        Create a table for the sensor if it does not already exist.

        The table will have columns:
        - measured_at: DATETIME, records the timestamp of the measurement, defaults to the current timestamp.
        - outside: FLOAT, stores the outside measurement.
        - inside: FLOAT, stores the inside measurement.
        """

        # SQL statement to create table with columns: measured_at (being automatic datetime), outside measurement (float), inside measurement (float)
        statement = f"CREATE TABLE IF NOT EXISTS {self.sensor_name} (measured_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, outside FLOAT NOT NULL, inside FLOAT NOT NULL);"

        # Generic try/except/finally block to execute SQL statement
        try:
            connection = connect(self.database_path)
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
        except Exception as e:
            print("Error creating sensor table:", e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def store_measurements(self, values: tuple[float, float]) -> None:
        """
        Store the outside and inside measurements in the database.

        Parameters:
        ------------
        values : tuple[float, float]
            A tuple containing the outside and inside measurement values.

        Raises:
        ------------
        ValueError
            If any value in the tuple is not of type 'float'.
        """

        # Check each measurement value (must be of type 'float')
        for value in values:
            if type(value) != float:
                raise ValueError("Value must be of type 'float'.")

        # SQL statement to insert outside and inside measurement values (datetime value is inserted automatically)
        statement = f"INSERT INTO {self.sensor_name} (outside, inside) VALUES (?, ?);"

        # Generic try/except/finally block to execute SQL statement
        try:
            connection = connect(self.database_path)
            cursor = connection.cursor()
            cursor.execute(statement, values)
            connection.commit()
        except Exception as e:
            print("Error storing measurements:", e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_measurements(self) -> list[tuple]:
        """
        Fetch all measurements from the sensor table in the database.

        This method retrieves all rows from the sensor table corresponding to
        the sensor name provided during the instantiation of the class.

        Returns:
        ------------
        list[tuple]
            A list of tuples, where each tuple represents a row in the sensor table.
            Each tuple contains:
            - measured_at (datetime): The timestamp when the measurement was taken.
            - outside (float): The outside measurement.
            - inside (float): The inside measurement.

        Raises:
        ------------
        Exception
            If there is an error in fetching measurements from the database, an exception is caught and an error message is printed.
        """

        # SQL statement to fetch all rows from table
        statement = f"SELECT * FROM {self.sensor_name};"

        # Generic try/except/finally block to execute SQL statement
        try:
            connection = connect(self.database_path)
            cursor = connection.cursor()
            cursor.execute(statement)
            selection = cursor.fetchall()
        except Exception as e:
            print("Error fetching measurements:", e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
            return selection
