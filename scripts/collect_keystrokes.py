import time
import psutil
import pandas as pd
from pynput import keyboard

data = []

def on_press(key):
    try:
        keystroke = key.char
    except AttributeError:
        keystroke = str(key)

    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    data.append([timestamp, keystroke, cpu_usage, memory_usage])
    print(f"[{timestamp}] Key: {keystroke}, CPU: {cpu_usage}%, Memory: {memory_usage}%")

with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass

df = pd.DataFrame(data, columns=["Timestamp", "Keystroke", "CPU Usage (%)", "Memory Usage (%)"])
df.to_csv("data/keystrokes_data.csv", index=False)
print("✅ Keystroke data saved to data/keystrokes_data.csv")