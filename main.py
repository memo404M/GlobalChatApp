# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.name_input = TextInput(multiline=False)
        self.layout.add_widget(self.name_input)
        self.button = Button(text='دخول')
        self.button.bind(on_press=self.login)
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)

    def login(self, instance):
        name = self.name_input.text
        if name:
            self.manager.current = 'chat'

class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(multiline=False)
        self.layout.add_widget(self.text_input)
        self.button = Button(text='إرسال')
        self.button.bind(on_press=self.send_message)
        self.layout.add_widget(self.button)
        self.messages = Label(text='')
        self.layout.add_widget(self.messages)
        self.add_widget(self.layout)

    def send_message(self, instance):
        message = self.text_input.text
        self.messages.text += f'{self.manager.current_screen.name}: {message}\n'
        self.text_input.text = ''

class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(ChatScreen(name='chat'))
        return self.sm

if __name__ == '__main__':
    MyApp().run()
