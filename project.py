import requests
from tkinter import *
from tkinter import messagebox

API_KEY = "4dc88a05207039941ba2e1a14cce380d"  # Your actual API key

def get_weather():
    print("Button clicked")
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data.get("message", "Cannot fetch weather"))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        result = f"City: {city.title()}\n"
        result += f"Temperature: {temp} °C\n"
        result += f"Humidity: {humidity}%\n"
        result += f"Condition: {weather}\n"
        result += f"Wind Speed: {wind} m/s"

        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI Setup
root = Tk()
root.title("Weather App")
root.geometry("350x300")
root.config(padx=20, pady=20)

Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=5)
city_entry = Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12), justify=LEFT)
result_label.pack(pady=10)

print("Launching weather app...")
root.mainloop()
