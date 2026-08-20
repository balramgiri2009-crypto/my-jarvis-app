# ====================================================================
# PROJECT JARVIS: COMPLETE END-TO-END MOBILE CODE
# Save this entire file as 'jarvis_core.py' in your system.
# ====================================================================

import os
import sys
import time
import struct
import threading
from openai import OpenAI
import speech_recognition as sr
import pvporcupine
from pyaudio import PyAudio, paInt16

# Kivy Framework Imports for Futuristic Holographic UI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock

# ====================================================================
# 1. AUTHENTICATION & CORE CREDENTIALS
# ====================================================================
# Substitute your personal API tokens below
PICOVOICE_API_KEY = "YOUR_PICOVOICE_API_KEY_HERE"
KEYWORD_PATH = "jarvis_wakeword.ppn" 
OPENAI_CLIENT = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

# ====================================================================
# 2. FUTURISTIC HUD/UI DESIGN (GRAPHICS)
# ====================================================================
class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        
        # Holographic Cyan Status Bar
        self.status_label = Label(
            text="SYSTEM STANDBY - AWAITING WAKE WORD", 
            font_size='16sp', 
            color=(0.0, 0.75, 1.0, 1.0),
            size_hint_y=0.15
        )
        self.add_widget(self.status_label)
        
        # Reactive Core Graphic Visualizer
        self.jarvis_core = Image(
            source='jarvis_blue_core.png', 
            size_hint=(None, None), 
            size=(220, 220),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.jarvis_core)
        
        # Idle Animation Engine (Breathing Pulsation)
        self.pulse = Animation(size=(240, 240), duration=1.2) + Animation(size=(220, 220), duration=1.2)
        self.pulse.repeat = True
        self.pulse.start(self.jarvis_core)

    def update_status(self, text, state="idle"):
        self.status_label.text = text
        if state == "listening":
            self.status_label.color = (1.0, 0.2, 0.2, 1.0) # Warning Red when processing human speech
        elif state == "processing":
            self.status_label.color = (0.8, 0.0, 1.0, 1.0) # Arc Purple when executing AI thinking
        else:
            self.status_label.color = (0.0, 0.75, 1.0, 1.0) # Standard Stark Cyan

ui_instance = None

# ====================================================================
# 3. CONVERSATIONAL LOGIC & SPEECH SYNTHESIS
# ====================================================================
def process_with_ai(user_command):
    try:
        response = OPENAI_CLIENT.chat.completions.create(
            model="gpt-4o", 
            messages=[
                {"role": "system", "content": "You are JARVIS, an advanced, highly loyal, and slightly witty AI assistant. Speak in sharp Hinglish (Hindi + English blend), use respectful terms like Sir, and give direct responses."},
                {"role": "user", "content": user_command}
            ]
        )
        ai_reply = response.choices.message.content
        print(f"[JARVIS]: {ai_reply}")
        
        # Audio execution block
        if sys.platform == "darwin":
            os.system(f"say '{ai_reply}'")
        elif sys.platform.startswith("win"):
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(ai_reply)
        else:
            os.system(f"espeak '{ai_reply}'")
            
    except Exception as e:
        print("[CRITICAL] AI Matrix Synapse Failure:", e)

def listen_command():
    global ui_instance
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ui_instance:
            Clock.schedule_once(lambda dt: ui_instance.update_status("LISTENING COMMAND...", state="listening"))
        
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=7)
            if ui_instance:
                Clock.schedule_once(lambda dt: ui_instance.update_status("DECRYPTING SPEECH...", state="processing"))
            
            command = r.recognize_google(audio, language="en-IN")
            print(f"[USER]: {command}")
            process_with_ai(command)
        except sr.WaitTimeoutError:
            print("[INFO] No acoustic inputs detected.")
        except Exception as e:
            print("[ERROR] Signal corrupted or unintelligible.")
    
    if ui_instance:
        Clock.schedule_once(lambda dt: ui_instance.update_status("SYSTEM STANDBY - AWAITING WAKE WORD", state="idle"))

# ====================================================================
# 4. ACOUSTIC WAKE-WORD MONITOR (BACKGROUND SPECTRUM)
# ====================================================================
def background_ears():
    porcupine = pvporcupine.create(access_key=PICOVOICE_API_KEY, keyword_paths=[KEYWORD_PATH])
    pa = PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate, channels=1, format=paInt16, input=True, frames_per_buffer=porcupine.frame_length
    )
    
    while True:
        try:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            
            if keyword_index >= 0:
                listen_command()
        except Exception:
            break

# ====================================================================
# 5. INITIALIZATION ENGINE
# ====================================================================
class MainJarvisApp(App):
    def build(self):
        global ui_instance
        Window.clearcolor = (0, 0, 0, 0.4) # Sets transparent overlay window mode
        ui_instance = JarvisUI()
        
        # Spawns asynchronous thread keeping the system background-ready
        threading.Thread(target=background_ears, daemon=True).start()
        return ui_instance

if __name__ == '__main__':
    MainJarvisApp().run()
