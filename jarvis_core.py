import os
import sys
import threading
from openai import OpenAI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.window import Window

OPENAI_CLIENT = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        
        self.status_label = Label(
            text="JARVIS ONLINE - READY TO RECEIVE SYSTEMS", 
            font_size='16sp', 
            color=(0.0, 0.75, 1.0, 1.0),
            size_hint_y=0.15
        )
        self.add_widget(self.status_label)
        
        self.jarvis_core = Image(
            source='jarvis_blue_core.png', 
            size_hint=(None, None), 
            size=(220, 220),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.jarvis_core)
        
        self.pulse = Animation(size=(240, 240), duration=1.2) + Animation(size=(220, 220), duration=1.2)
        self.pulse.repeat = True
        self.pulse.start(self.jarvis_core)

class MainJarvisApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0.4)
        return JarvisUI()

if __name__ == '__main__':
    MainJarvisApp().run()
