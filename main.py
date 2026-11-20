from pyscript import document
# Dictionary of weather instruments and their corresponding information
weather_instruments = {
    "Thermometer": ("Air Temperature", "Degrees Celsius (°C)", "Measures how hot or cold the air is."),
    "Barometer": ("Atmospheric Pressure", "Hectopascals (hPa)", "Measures air pressure to help monitor weather changes."),
    "Anemometer": ("Wind Speed", "Kilometers per hour (km/h)", "Measures how fast the wind is blowing."),
    "Hygrometer": ("Relative Humidity", "Percent (%)", "Measures the amount of moisture in the air."),
    "Rain Gauge": ("Rainfall", "Millimeters (mm)", "Measures the amount of rainfall in an area."),
    "Wind Vane": ("Wind Direction", "Cardinal Directions", "Identifies the direction from which the wind is blowing."),
    "Weather Balloon": ("Atmospheric Conditions", "Varies", "Collects atmospheric data at different altitudes."),
    "Pyranometer": ("Solar Radiation", "Watts per square meter (W/m²)", "Measures incoming solar radiation.")
}
# Get the Input from HTML
def Search_Element(e):
    raw_input = document.getElementById("weather_instruments").value
    instrument_name = raw_input.strip().title()

    if not instrument_name:
        document.getElementById("instruments").innerText = "-"
        document.getElementById("measures").innerText = "Please enter an instrument name"
        document.getElementById("unit-of-measurement").innerText = "-"
        document.getElementById("purpose").innerText = "-"
        return
# Retrieve info from the dictionary
    result = weather_instruments.get(instrument_name, ("Weather Instrument not found", "-", "-"))
# Display the result in HTML
    document.getElementById("instruments").innerText = instrument_name
    document.getElementById("measures").innerText = result[0]
    document.getElementById("unit-of-measurement").innerText = result[1]
    document.getElementById("purpose").innerText = result[2]