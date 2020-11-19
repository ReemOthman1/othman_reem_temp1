let tempF = 60
while (true) {
    if (input.temperature(TemperatureUnit.Fahrenheit) > tempF) {
        light.setPixelColor(5, light.rgb(255, 0, 0))
    } else {
        light.clear()
    }
    
}
