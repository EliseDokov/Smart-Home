from random import uniform
from sqlite3 import connect
from time import sleep


def main():

    # mock data generator

    create_database("smart_home.db")

    for _ in range(20):
        temperatures = generate_temperatures()
        store_temperature("smart_home.db", temperatures)
        sleep(5)


def generate_temperatures() -> tuple[float, float]:

    return (round(uniform(20.0, 20.5), 1), round(uniform(25.0, 25.5), 1))


def create_database(database_path: str) -> None:

    statement = """
        CREATE TABLE IF NOT EXISTS temperatures (
            measured_at     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
            out_temp        FLOAT        NOT NULL,
            in_temp         FLOAT        NOT NULL
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


def store_temperature(database_path: str, values: tuple[float, float]) -> None:

    statement = "INSERT INTO temperatures (out_temp, in_temp) VALUES (?, ?);"

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
