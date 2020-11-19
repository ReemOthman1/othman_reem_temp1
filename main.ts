while (true) {
    console.log(" Current Room Temperature:" + input.temperature(TemperatureUnit.Fahrenheit) + "°F - " + input.temperature(TemperatureUnit.Celsius) + "°C")
}
let TempF = 60
if (TempF > 60) {
    light.setPixelColor(5, light.rgb(255, 0, 0))
}

