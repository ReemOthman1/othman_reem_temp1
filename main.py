tempF=70
while True:
    print ("tempature"+ input.temperature(TemperatureUnit.FAHRENHEIT))  
if input.temperature(TemperatureUnit.FAHRENHEIT) > tempF:
    light.set_pixel_color(0, light.rgb(255, 0, 0))
    light.set_pixel_color(1, light.rgb(255, 0, 0))
    light.set_pixel_color(2, light.rgb(255, 0, 0))
    light.set_pixel_color(3, light.rgb(255, 0, 0))
    light.set_pixel_color(4, light.rgb(255, 0, 0))
    light.set_pixel_color(5, light.rgb(255, 0, 0))    
    light.set_pixel_color(6, light.rgb(255, 0, 0)) 
    light.set_pixel_color(7, light.rgb(255, 0, 0)) 
    light.set_pixel_color(8, light.rgb(255, 0, 0)) 
    light.set_pixel_color(9, light.rgb(255, 0, 0)) 

elif input.temperature(TemperatureUnit.FAHRENHEIT) < tempF + input.temperature(TemperatureUnit.FAHRENHEIT)<40:
    light.set_pixel_color(0, light.rgb(0, 255, 0))
    light.set_pixel_color(1, light.rgb(0, 255, 0))
    light.set_pixel_color(2, light.rgb(0, 255, 0))
    light.set_pixel_color(3, light.rgb(0, 255, 0))
    light.set_pixel_color(4, light.rgb(0, 255, 0))
    light.set_pixel_color(5, light.rgb(0, 255, 0))
    light.set_pixel_color(6, light.rgb(0, 255, 0))
    light.set_pixel_color(7, light.rgb(0, 255, 0))
    light.set_pixel_color(8, light.rgb(0, 255, 0))
    light.set_pixel_color(9, light.rgb(0, 255, 0))

else:  
   light.set_pixel_color(0, light.rgb(0, 0, 255))
   light.set_pixel_color(1, light.rgb(0, 0, 255))
   light.set_pixel_color(2, light.rgb(0, 0, 255))
   light.set_pixel_color(3, light.rgb(0, 0, 255))
   light.set_pixel_color(4, light.rgb(0, 0, 255))
   light.set_pixel_color(5, light.rgb(0, 0, 255))
   light.set_pixel_color(6, light.rgb(0, 0, 255))
   light.set_pixel_color(7, light.rgb(0, 0, 255))
   light.set_pixel_color(8, light.rgb(0, 0, 255))
   light.set_pixel_color(9, light.rgb(0, 0, 255))