## Smart Home Database Interface

Ovaj projekt omogućava upravljanje uređajima i senzorima u pametnom domu koristeći SQLite bazu podataka. Pruža dvije glavne klase: `Device` i `Sensor`.

### Klasa `Device`

Klasa `Device` omogućava upravljanje stanjem uređaja u bazi podataka.

```python
from device import Device

# Kreirajte instancu klase Device
vacuum_cleaner = Device("smart_home.db", "vacuum_cleaner")

# Pohranite stanje uređaja (0 ili 1)
vacuum_cleaner.store_state(1)
vacuum_cleaner.store_state(0)

# Dohvatite sva stanja uređaja
states = vacuum_cleaner.get_states()
print(states)

```

### Klasa `Sensor`

Klasa `Sensor` omogućava pohranu senzorskih mjerenja u bazi podataka.

```python
from sensor import Sensor

# Kreirajte instancu klase Sensor
temperature_sensor = Sensor("smart_home.db", "temperature_sensor")

# Pohranite temperature (vanjska, unutarnja)
temperature_sensor.store_measurements((22.5, 23.1))
temperature_sensor.store_measurements((24.0, 25.2))

# Dohvatite sva mjerenja temperature
measurements = temperature_sensor.get_measurements()
print(measurements)

```
