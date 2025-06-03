class TemperatureConverter:

    def __init__(self, temp, unit):
        self.temperature = temp
        self.unit = unit.upper()

    # ✅ Class Method to take input from user
    @classmethod
    def input_value(cls):
        try:
            temp = float(input("Enter temperature: "))
            unit = input("Enter unit (C, F, K): ").upper()
            return cls(temp, unit)
        except ValueError:
            print("Invalid input")
            return None

    # ✅ Instance Method to convert
    def convertunit(self):
        if self.unit == 'C':
            self.from_celsius()
        elif self.unit == 'F':
            self.from_fahrenheit()
        elif self.unit == 'K':
            self.from_kelvin()
        else:
            print("Invalid unit. Use C, F, or K.")

    # ✅ Static Methods
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    # ✅ Instance helper methods
    def from_celsius(self):
        f = self.celsius_to_fahrenheit(self.temperature)
        k = self.celsius_to_kelvin(self.temperature)
        print(f"{self.temperature} °C = {f:.2f} °F = {k:.2f} K")

    def from_fahrenheit(self):
        c = self.fahrenheit_to_celsius(self.temperature)
        k = self.celsius_to_kelvin(c)
        print(f"{self.temperature} °F = {c:.2f} °C = {k:.2f} K")

    def from_kelvin(self):
        c = self.kelvin_to_celsius(self.temperature)
        f = self.celsius_to_fahrenheit(c)
        print(f"{self.temperature} K = {c:.2f} °C = {f:.2f} °F")


# ---------- MAIN PROGRAM ----------
converter = TemperatureConverter.input_value()
if converter:
    converter.convertunit()
