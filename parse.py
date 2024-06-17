from bs4 import BeautifulSoup

# Sample XML data as a string
xml_data = """
<Hrvatska>
<DatumTermin>
<Datum>17.06.2024</Datum>
<Termin>17</Termin>
</DatumTermin>
<Grad autom="0">
<GradIme>RC Bilogora</GradIme>
<Lat>45.884</Lat>
<Lon>17.200 </Lon>
<Podatci>
<Temp> 28.0</Temp>
<Vlaga>47</Vlaga>
<Tlak>1014.8</Tlak>
<TlakTend>-0.2</TlakTend>
<VjetarSmjer>SW</VjetarSmjer>
<VjetarBrzina> 1.5</VjetarBrzina>
<Vrijeme>pretežno vedro</Vrijeme>
<VrijemeZnak>2</VrijemeZnak>
</Podatci>
</Grad>
<!-- More <Grad> entries -->
</Hrvatska>
"""

# Parse the XML data
soup = BeautifulSoup(xml_data, 'xml')

# Extract date and time
datum = soup.find('Datum').text
termin = soup.find('Termin').text

print(f"Date: {datum}, Time: {termin}")

# Extract city data
cities = soup.find_all('Grad')
for city in cities:
    grad_ime = city.find('GradIme').text
    lat = city.find('Lat').text.strip()
    lon = city.find('Lon').text.strip()
    temp = city.find('Temp').text.strip()
    vlaga = city.find('Vlaga').text.strip()
    tlak = city.find('Tlak').text.strip()
    tlak_tend = city.find('TlakTend').text.strip()
    vjetar_smjer = city.find('VjetarSmjer').text.strip()
    vjetar_brzina = city.find('VjetarBrzina').text.strip()
    vrijeme = city.find('Vrijeme').text.strip()
    vrijeme_znak = city.find('VrijemeZnak').text.strip()

    print(f"\nCity: {grad_ime}")
    print(f"Latitude: {lat}, Longitude: {lon}")
    print(f"Temperature: {temp}°C, Humidity: {vlaga}%")
    print(f"Pressure: {tlak} hPa, Pressure Trend: {tlak_tend} hPa")
    print(f"Wind Direction: {vjetar_smjer}, Wind Speed: {vjetar_brzina} m/s")
    print(f"Weather: {vrijeme}, Weather Sign: {vrijeme_znak}")
