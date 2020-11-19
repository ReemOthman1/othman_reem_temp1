while True:
    print(" Current Room Temperature:" + input.temperature(TemperatureUnit.FAHRENHEIT) + "°F - " + input.temperature(TemperatureUnit.CELSIUS) + "°C")
TempF=60 
if TempF>60:
    light.set_pixel_color(5, light.rgb(255, 0, 0))
