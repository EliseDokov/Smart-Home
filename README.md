## Funkcije za Vrijeme i Emoji odjece

Ovaj Python modul pruza funkcije za dohvacanje trenutne temperature za odredeni grad putem hrvatskog vremenskog API-ja te za odredivanje odgovarajuceg emoji-ja odjece na temelju temperature.

### TL;DR

Kombiniraj dvije funkcije kako bi se dobila preporuka za odjecu na temelju trenutne temperature u "Zagreb-Maksimiru" izrazene emoji-jima.

```python
from emoji_clothes import get_emoji, get_temp

print(get_emoji(get_temp()))
```

### Funkcija `get_temp`

Dohvaca temperaturu za odredeni grad putem hrvatskog vremenskog API-ja.

```python
from emoji_clothes import get_temp

temperatura = get_temp("Zagreb-Maksimir")

print(f"Temperatura u Zagrebu-Maksimiru je {temperatura}_C")
```

- **Argumenti**

  - Naziv grada za koji zelite dohvatiti temperaturu. `(str)`
  - Zadano je `"Zagreb-Maksimir"`

- **Povratna vrijednost**:

  - Temperatura odabranog grada. `(float)`

### Funkcija `get_emoji`

Vraca niz emoji-ja koji predstavlja odgovarajucu odjecu za zadatu temperaturu.

```python
from emoji_clothes import get_emoji

emoji_odjece = get_emoji(25.0)

print(f"Preporucena odjeca za 25_C: {emoji_odjece}")
```

- **Argumenti**

  - Temperatura u Celzijusima. `(float)`

- **Povratna vrijednost**:

  - Niz emoji-ja koji predstavlja preporucenu odjecu na temelju temperature. `(str)`

## Smart Home Database Interface

Ovaj projekt omogucava upravljanje uredajima i senzorima u pametnom domu koristeci SQLite bazu podataka. Pruza dvije glavne klase: `Device` i `Sensor`.

### Klasa `Device`

Klasa `Device` omogucava upravljanje stanjem uredaja u bazi podataka.

```python
from device import Device

# Kreirajte instancu klase Device
vacuum_cleaner = Device("smart_home.db", "vacuum_cleaner")

# Pohranite stanje uredaja (0 ili 1)
vacuum_cleaner.store_state(1)
vacuum_cleaner.store_state(0)

# Dohvatite sva stanja uredaja
states = vacuum_cleaner.get_states()
print(states)

```

### Klasa `Sensor`

Klasa `Sensor` omogucava pohranu senzorskih mjerenja u bazi podataka.

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
