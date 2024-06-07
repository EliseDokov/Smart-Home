from datetime import datetime
from sqlite3 import connect


def main():
    pass


def now_sql() -> str:
    """
    Generates the current date and time in SQL datetime format.

    This function retrieves the current local date and time, formats it according to
    the standard SQL datetime format 'YYYY-MM-DD HH:MM:SS', and returns it as a string.

    Returns:
        str: The current date and time as a string in the format 'YYYY-MM-DD HH:MM:SS'.
    """

    now_datetime = datetime.now()
    now_str = now_datetime.strftime(r"%Y-%m-%d %H:%M:%S")
    return now_str


def create_database(database_path: str) -> None:
    """
    Creates a temperatures table in the specified SQLite database if it does not already exist.

    This function connects to an SQLite database at the given path, creates a cursor, and
    executes a SQL statement to create a table named 'temperatures' with the columns 'datetime',
    'out_temp', and 'in_temp'. The table will be created only if it does not already exist.
    Any errors during the connection, cursor creation, or SQL execution are caught and printed.

    Args:
        database_path (str): The file path to the SQLite database.

    Returns:
        None
    """

    statement = """
        CREATE TABLE IF NOT EXISTS temperatures (
            datetime     DATETIME     NOT NULL,
            out_temp     FLOAT        NOT NULL,
            in_temp      FLOAT        NOT NULL
        );
        """

    try:
        connection = connect(database_path)
        cursor = connection.cursor()
    except Exception as e:
        print("Error establishing connection and cursor:", e)
    else:
        try:
            cursor.execute(statement)
            connection.commit()
        except Exception as e:
            print("Error executing SQL statement:", e)
        else:
            print("SQL statement executed successfully.")
        finally:
            cursor.close()
            connection.close()


def store_temperature(database_path: str, values: tuple[str, float, float]) -> None:
    """
    Inserts a temperature record into the temperatures table of the specified SQLite database.

    This function connects to an SQLite database at the given path, creates a cursor,
    and executes an SQL statement to insert a record into the 'temperatures' table with
    the provided values for datetime, out_temp, and in_temp. Any errors during the
    connection, cursor creation, or SQL execution are caught and printed.

    Args:
        database_path (str): The file path to the SQLite database.
        values (tuple[str, float, float]): A tuple containing the datetime string,
                                           outside temperature (float), and inside
                                           temperature (float) to be inserted.

    Returns:
        None
    """

    statement = """
        INSERT INTO temperatures
            (datetime, out_temp, in_temp)
        VALUES
            (?, ?, ?);
    """

    try:
        connection = connect(database_path)
        cursor = connection.cursor()
    except Exception as e:
        print("Error establishing connection and cursor:", e)
    else:
        try:
            cursor.execute(statement, values)
            connection.commit()
        except Exception as e:
            print("Error executing SQL statement:", e)
        else:
            print("SQL statement executed successfully.")
        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    main()
