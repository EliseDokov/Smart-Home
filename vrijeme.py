import xml.etree.ElementTree as ET
import requests

class Vrijeme:
    def __init__(self, url):
        self.url = url
        self.weather_data = None

    def fetch_weather_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            xml_data = response.content
            root = ET.fromstring(xml_data)
            for location in root.findall("Grad"):
                name = location.find("GradIme").text if location.find("GradIme") is not None else "N/A"
                if name == "Zagreb-Maksimir":
                    data = location.find("Podatci")
                    temp = data.find("Temp").text if data.find("Temp") is not None else "N/A"
                    humidity = data.find("Vlaga").text if data.find("Vlaga") is not None else "N/A"
                    pressure = data.find("Tlak").text if data.find("Tlak") is not None else "N/A"
                    
                    self.weather_data = {
                        "location": name,
                        "temperature": temp,
                        "humidity": humidity,
                        "pressure": pressure,
                    }
                    break
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    def get_location(self):
        if self.weather_data:
            return self.weather_data.get("location", "N/A")
        return "N/A"

    def get_temperature(self):
        if self.weather_data:
            return self.weather_data.get("temperature", "N/A")
        return "N/A"

    def get_humidity(self):
        if self.weather_data:
            return self.weather_data.get("humidity", "N/A")
        return "N/A"

    def get_pressure(self):
        if self.weather_data:
            return self.weather_data.get("pressure", "N/A")
        return "N/A"

# Example usage
url = "https://vrijeme.hr/hrvatska_n.xml"
vrijeme = Vrijeme(url)
vrijeme.fetch_weather_data()

print("Location:", vrijeme.get_location())
print("Temperature:", vrijeme.get_temperature())
print("Humidity:", vrijeme.get_humidity())
print("Pressure:", vrijeme.get_pressure())