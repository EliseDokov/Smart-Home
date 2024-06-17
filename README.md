## Funkcije za Vrijeme i Emoji odjeće

Ovaj Python modul pruža funkcije za dohvaćanje trenutne temperature za određeni grad putem hrvatskog vremenskog API-ja te za određivanje odgovarajućeg emoji-ja odjeće na temelju temperature.

### TL;DR

Kombiniraj dvije funkcije kako bi se dobila preporuka za odjeću na temelju trenutne temperature u "Zagreb-Maksimiru" izražene emoji-jima.

```python
print(get_emoji(get_temp()))
```

### Funkcija `get_temp`

Dohvaća temperaturu za određeni grad putem hrvatskog vremenskog API-ja.

```python
temperatura = get_temp("Zagreb-Maksimir")

print(f"Temperatura u Zagrebu-Maksimiru je {temperatura}°C")
```

- **Argumenti**

  - Naziv grada za koji želite dohvatiti temperaturu. `(str)`
  - Zadano je `"Zagreb-Maksimir"`

- **Povratna vrijednost**:

  - Temperatura odabranog grada. `(float)`

### Funkcija `get_emoji`

Vraća niz emoji-ja koji predstavlja odgovarajuću odjeću za zadatu temperaturu.

```python
emoji_odjeće = get_emoji(25.0)

print(f"Preporučena odjeća za 25°C: {emoji_odjeće}")
```

- **Argumenti**

  - Temperatura u Celzijusima. `(float)`

- **Povratna vrijednost**:

  - Niz emoji-ja koji predstavlja preporučenu odjeću na temelju temperature. `(str)`

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
