from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import requests

# الرابط العالمي الخاص بك
URL = "https://puzzles-origins-joshua-letting.trycloudflare.com"

class GlobalChat(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # عرض الرسائل
        self.scroll = ScrollView()
        self.chat_logs = Label(text="Welcome to the Global Chat!", size_hint_y=None, halign='left')
        self.chat_logs.bind(texture_size=self.chat_logs.setter('size'))
        self.scroll.add_widget(self.chat_logs)
        self.layout.add_widget(self.scroll)
        
        # خانات الاسم والرسالة
        self.name_in = TextInput(hint_text="Your Name", size_hint_y=None, height=100, multiline=False)
        self.msg_in = TextInput(hint_text="Type Message...", size_hint_y=None, height=100, multiline=False)
        self.layout.add_widget(self.name_in)
        self.layout.add_widget(self.msg_in)
        
        # زر الإرسال
        self.btn = Button(text="Send Message", size_hint_y=None, height=100, background_color=(0, 0.7, 1, 1))
        self.btn.bind(on_press=self.send_message)
        self.layout.add_widget(self.btn)
        
        # تحديث الدردشة كل ثانية
        Clock.schedule_interval(self.refresh_chat, 1)
        return self.layout

    def send_message(self, instance):
        if self.msg_in.text:
            try:
                requests.post(f"{URL}/send", data={'name': self.name_in.text, 'msg': self.msg_in.text})
                self.msg_in.text = ""
            except: pass

    def refresh_chat(self, dt):
        try:
            r = requests.get(f"{URL}/sync", timeout=1)
            msgs = r.json()
            display_text = ""
            for m in msgs:
                display_text += f"[{m['time']}] {m['name']}: {m['msg']}\n"
            self.chat_logs.text = display_text
        except: pass

if __name__ == "__main__":
    GlobalChat().run()

