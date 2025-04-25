import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={API_KEY}&units=metric"
    )
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            return f"🌡 Temp: {temp}°C\n☁️ Condition: {condition}\n💧 Humidity: {humidity}%\n💨 Wind: {wind} m/s"
        else:
            return f"❌ Error: {data.get('message', 'Something went wrong.')}"
    except Exception as e:
        return f"⚠️ Could not fetch weather: {e}"

def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

# GUI setup
window = tk.Tk()
window.title("🌦 Weather App")
window.geometry("300x250")

tk.Label(window, text="Enter City:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(window, width=25)
city_entry.pack()

tk.Button(window, text="Get Weather", command=show_weather).pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

window.mainloop()
