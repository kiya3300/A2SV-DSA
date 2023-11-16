class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kalvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kalvin, fahrenheit]

        celsius = 36.50
        ans = convertTemperature(celsius)
        print(ans)