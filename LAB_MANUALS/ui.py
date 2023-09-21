import tkinter as tk

from physical import *

def update_temperature_humidity():
    temp = readTemperature()
    humi = readMoisture()
    temperature_label.config(text=f"Temperature: {temp} °C")
    humidity_label.config(text=f"Humidity: {humi}%")
    
    window.after(2000, update_temperature_humidity)

window = tk.Tk()
window.title("Temperature and Humidity Monitor")
window.attributes('-fullscreen', True)

temperature_label = tk.Label(window, text="Temperature: -- °C", font=("Helvetica", 24))
temperature_label.pack(pady=20)

humidity_label = tk.Label(window, text="Humidity: --%", font=("Helvetica", 24))
humidity_label.pack(pady=20)

update_temperature_humidity()