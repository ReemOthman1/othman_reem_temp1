let tempF = 70
while (true) {
    console.log("tempature" + input.temperature(TemperatureUnit.Fahrenheit))
}
if (input.temperature(TemperatureUnit.Fahrenheit) > tempF) {
    light.setPixelColor(0, light.rgb(255, 0, 0))
    light.setPixelColor(1, light.rgb(255, 0, 0))
    light.setPixelColor(2, light.rgb(255, 0, 0))
    light.setPixelColor(3, light.rgb(255, 0, 0))
    light.setPixelColor(4, light.rgb(255, 0, 0))
    light.setPixelColor(5, light.rgb(255, 0, 0))
    light.setPixelColor(6, light.rgb(255, 0, 0))
    light.setPixelColor(7, light.rgb(255, 0, 0))
    light.setPixelColor(8, light.rgb(255, 0, 0))
    light.setPixelColor(9, light.rgb(255, 0, 0))
} else if (input.temperature(TemperatureUnit.Fahrenheit) < tempF + input.temperature(TemperatureUnit.Fahrenheit) && tempF + input.temperature(TemperatureUnit.Fahrenheit) < 40) {
    light.setPixelColor(0, light.rgb(0, 255, 0))
    light.setPixelColor(1, light.rgb(0, 255, 0))
    light.setPixelColor(2, light.rgb(0, 255, 0))
    light.setPixelColor(3, light.rgb(0, 255, 0))
    light.setPixelColor(4, light.rgb(0, 255, 0))
    light.setPixelColor(5, light.rgb(0, 255, 0))
    light.setPixelColor(6, light.rgb(0, 255, 0))
    light.setPixelColor(7, light.rgb(0, 255, 0))
    light.setPixelColor(8, light.rgb(0, 255, 0))
    light.setPixelColor(9, light.rgb(0, 255, 0))
} else {
    light.setPixelColor(0, light.rgb(0, 0, 255))
    light.setPixelColor(1, light.rgb(0, 0, 255))
    light.setPixelColor(2, light.rgb(0, 0, 255))
    light.setPixelColor(3, light.rgb(0, 0, 255))
    light.setPixelColor(4, light.rgb(0, 0, 255))
    light.setPixelColor(5, light.rgb(0, 0, 255))
    light.setPixelColor(6, light.rgb(0, 0, 255))
    light.setPixelColor(7, light.rgb(0, 0, 255))
    light.setPixelColor(8, light.rgb(0, 0, 255))
    light.setPixelColor(9, light.rgb(0, 0, 255))
}

