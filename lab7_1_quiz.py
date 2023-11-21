# Quiz: System Inteligentnego Domu

# Inteligentne Oświetlenie (SmartLight)
# Klasa SmartLight reprezentuje inteligentne żarówki, których jasność można regulować. Jasność jest ograniczona zakresem od 0 do 100. Użyj dekoratorów @property i @setter do kontroli poziomu jasności.

# System Audio (AudioSystem i SmartSpeaker)
# AudioSystem: Klasa bazowa z atrybutami brand i max_volume.
# SmartSpeaker: Klasa pochodna od AudioSystem (ma dziedziczyć z AudioSystem) , dodająca atrybut voice_command_enabled. Zdefiniuj metody get_details w obu klasach, aby zwracały informacje o systemie audio i inteligentnym głośniku (w formie słownika)(tak jak w testach).

# Robot Sprzątający (CleaningRobot)
# Klasa CleaningRobot z atrybutami model i battery_life. Zaimplementuj metodę magiczną setattr, aby zarządzać atrybutami klasy, upewniając się, że battery_life jest liczbą całkowitą. Dodatkowo, zaimplementuj metodę magiczną str, aby zwracała czytelną reprezentację robota sprzątającego.

# Twoje rozwiązanie:
# Tutaj tworzone są klasy SmartLight, AudioSystem, SmartSpeaker i CleaningRobot.
# Wszystkie te klasy powinny być zaimplementowane zgodnie z opisem w zadaniu.

class SmartLight:
    def __init__(self):
        self._brightness = 0

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self._brightness = value
        else:
            raise ValueError("Brightness must be between 0 and 100")

class AudioSystem:
    def __init__(self, brand, max_volume):
        self.brand = brand
        self.max_volume = max_volume

    def get_details(self):
        return {"brand": self.brand, "max_volume": self.max_volume}

class SmartSpeaker(AudioSystem):
    def __init__(self, brand, max_volume, voice_command_enabled):
        super().__init__(brand, max_volume)
        self.voice_command_enabled = voice_command_enabled

    def get_details(self):
        details = super().get_details()
        details["voice_command_enabled"] = self.voice_command_enabled
        return details

class CleaningRobot:
    def __init__(self, model, battery_life):
        self.model = model
        self.battery_life = battery_life

    def __setattr__(self, key, value):
        if key == "battery_life" and not isinstance(value, int):
            raise ValueError("battery_life must be an integer")
        self.__dict__[key] = value

    def __str__(self):
        return f"CleaningRobot(model={self.model}, battery_life={self.battery_life})"
