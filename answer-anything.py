import tkinter as tk
from tkinter import simpledialog, messagebox
import pyautogui
import openai
import base64
from io import BytesIO
from dotenv import load_dotenv
import os
import threading
import keyboard

# Load OpenAI key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in your .env file.")

client = openai.OpenAI(api_key=api_key)

# Global to hold coordinates
selection = {}

class RegionSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.attributes('-alpha', 0.3)
        self.configure(bg='gray')
        self.canvas = tk.Canvas(self, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.start_x = self.start_y = 0
        self.rect = None
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        selection['x'] = min(self.start_x, event.x)
        selection['y'] = min(self.start_y, event.y)
        selection['w'] = abs(event.x - self.start_x)
        selection['h'] = abs(event.y - self.start_y)
        self.destroy()

def screenshot_to_base64(region):
    screenshot = pyautogui.screenshot(region=region)
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def ask_gpt(image_b64, prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}
                    ]
                }
            ],
            temperature=0.2,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def run_glider():
    RegionSelector().mainloop()
    if not selection:
        messagebox.showinfo("AI Glider", "No region selected.")
        return

    region = (selection['x'], selection['y'], selection['w'], selection['h'])
    prompt = simpledialog.askstring("Ask AI", "What do you want to know about this region?")
    if not prompt:
        return

    def worker():
        image_b64 = screenshot_to_base64(region)
        result = ask_gpt(image_b64, prompt)
        messagebox.showinfo("AI Response", result)

    threading.Thread(target=worker).start()

def listen_hotkey():
    print("Press Ctrl+Shift+E to activate. Press Esc to quit.")
    while True:
        if keyboard.is_pressed('ctrl+shift+e'):
            run_glider()
            while keyboard.is_pressed('ctrl+shift+e'):
                pass
        elif keyboard.is_pressed('esc'):
            print("Exiting...")
            break

if __name__ == '__main__':
    listen_hotkey()
