import xml.etree.ElementTree as ET

import requests


def main():
    print(get_emoji(get_temp()))


def get_temp(city: str = "Zagreb-Maksimir") -> float:
    """
    Fetches the temperature for a given city from the Croatian weather API.

    Args:
        city (str): The name of the city for which to retrieve the temperature.
                    Default is "Zagreb-Maksimir".

    Returns:
        float: The temperature of the specified city. Returns "N/A" if the
               city or temperature data is not found.

    Raises:
        ValueError: If the temperature data cannot be converted to a float.
    """

    url = "https://vrijeme.hr/hrvatska_n.xml"
    response = requests.get(url)
    xml_data = response.content
    root = ET.fromstring(xml_data)

    for location in root.findall("Grad"):
        name = (
            location.find("GradIme").text
            if location.find("GradIme") is not None
            else "N/A"
        )

        if name == city:
            data = location.find("Podatci")
            if data is not None:
                temp = (
                    data.find("Temp").text if data.find("Temp") is not None else "N/A"
                )
                temp = float(temp)
            else:
                temp = "N/A"

            return temp


def get_emoji(temp: float) -> str:
    """
    Returns an emoji string representing the appropriate clothing for a given temperature.

    Args:
        temp (float): The temperature in degrees Celsius.

    Returns:
        str: An emoji string representing the recommended clothing based on the temperature.
             - "🩳👕" for temperatures above 22°C
             - "👖👔" for temperatures above 12°C
             - "👖🧥" for temperatures above 0°C
             - "👖🧥🧣🧤🧢" for temperatures 0°C or below
    """

    if temp > 22:
        return "🩳👕"
    elif temp > 12:
        return "👖👔"
    elif temp > 0:
        return "👖🧥"
    else:
        return "👖🧥🧣🧤🧢"


if __name__ == "__main__":
    main()
