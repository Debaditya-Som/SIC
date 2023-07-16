import tkinter as tk
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import datetime
import requests
import json
import wikipedia
import math

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
r = sr.Recognizer()

# Define functions for text-to-speech and speech-to-text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if 'weather' in command:
        city = command.split(' ')[-1]
        return get_weather(city)
    elif 'news' in command:
        return get_news()
    elif 'wikipedia' in command:
        query = command.replace('wikipedia', '')
        return get_wiki(query)
    elif 'time' in command:
        now = datetime.datetime.now()
        return f"The time is {now.strftime('%I:%M %p')}"
    else:
        return "I'm sorry, I didn't understand that command."

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=<API_KEY>'
    response = requests.get(url)
    data = json.loads(response.text)
    temp = data['main']['temp']
    return f"The temperature in {city} is {temp} Kelvin."

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=<API_KEY>"
    response = requests.get(url)
    data = json.loads(response.text)
    articles = data['articles']
    titles = [article['title'] for article in articles]
    return 'The top news headlines are: ' + ', '.join(titles)

def get_wiki(query):
    return wikipedia.summary(query, sentences=2)

# Define function to handle button click
def button_clicked():
    # Use speech recognition to get user's command
    with sr.Microphone() as source:
        label.config(text="Listening...")
        audio = r.listen(source)
    label.config(text="Processing...")

    # Process user's command
    try:
        command = r.recognize_google(audio)
        response = process_command(command)
        label.config(text=response)
        speak(response)
    except:
        label.config(text="Sorry, I couldn't understand that command.")

window = tk.Tk()
window.title("Jarvis")
window.config(bg="black") # set background color to black

# Create a label widget


progress = ttk.Progressbar(window, orient='horizontal', mode='indeterminate', length=300)
style = ttk.Style()


canvas = tk.Canvas(window, width=500, height=100, bg='black')

# create the wave
def wave():
    amplitude = 10
    frequency = 0.05
    phase = 0
    x_increment = 0.1
    points = []
    for x in range(0, 500):
        y = amplitude * math.sin(frequency * x + phase)
        points.append((x, y + 50))
    return points

# create the wavy line
wave_points = wave()
line_id = canvas.create_line(wave_points, fill='olive drab', width=3)

# add the canvas to the window
canvas.pack()




# test the speak function
speak("Hello, my name is Jarvis.")

btn = tk.Button(window, text="Speak", font=("Helvetica", 16), bg="black", fg="olive drab", bd=2, relief="solid")

btn.pack(pady=0)




image = tk.PhotoImage(file="E:\Codes\Jarvis_Updated\Jarvis_Logo.png")
logo = tk.Label(window, image=image)
logo.pack(pady=10)
# Start the event loop
window.mainloop()
    
