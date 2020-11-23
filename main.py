tempF=70
while True:
    print ("tempature"+ input.temperature(TemperatureUnit.FAHRENHEIT))  
    if input.temperature(TemperatureUnit.FAHRENHEIT) > tempF:
        light.set_pixel_color(5, light.rgb(255, 0, 0))
    else :  
     if input.temperature(TemperatureUnit.FAHRENHEIT) < 70:
        light.set_pixel_color(5, light.rgb(0, 255, 0))
