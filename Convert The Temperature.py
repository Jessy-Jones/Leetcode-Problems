def convertTemperature(Celcius: float) -> [int]:
    return[Celcius + 273.15, Celcius * 1.80 + 32.00]

print(convertTemperature(37.00))