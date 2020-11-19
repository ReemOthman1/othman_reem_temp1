let tempF = 60
while (true) {
    console.log("tempature" + input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) > tempF) {
        light.setPixelColor(5, light.rgb(255, 0, 0))
    } else {
        light.clear()
    }
    
}
