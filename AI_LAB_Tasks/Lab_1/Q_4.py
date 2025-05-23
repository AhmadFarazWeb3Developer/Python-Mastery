

def converToFahrenheit(degreesCelsius):
    return degreesCelsius * 9/5 + 32


def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * 5/9


temperature = float(input("Enter temperature in Celsius: "))


fahrenhiteTemp = converToFahrenheit(temperature)
celsiusTemp = convertToCelsius(fahrenhiteTemp)

print('Temperature in Fahrenheit : ', fahrenhiteTemp, 'F')
print('Temperature in celsius :', celsiusTemp, 'C')
