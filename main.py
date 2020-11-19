tempF=60
while True: 
    if input.temperature(TemperatureUnit.FAHRENHEIT) > tempF:
        light.set_pixel_color(5, light.rgb(255, 0, 0))
    else : 
        light.clear()