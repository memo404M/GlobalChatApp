from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# تصميم الواجهة بلغة KV لإضافة ألوان وهوية بصرية
Builder.load_string('''
<LoginScreen>:
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.2, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: "Global Chat"
            font_size: '32sp'
            bold: True
            color: 0, 1, 0.8, 1
        TextInput:
            id: username
            hint_text: "ادخل اسم المستخدم (اليوزر)"
            multiline: False
            size_hint_y: None
            height: '50dp'
        Button:
            text: "دخول للدردشة"
            size_hint_y: None
            height: '50dp'
            background_color: 0, 0.7, 0.9, 1
            on_press: root.login()

<ChatScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "غرفة الدردشة العامة"
            size_hint_y: None
            height: '50dp'
        ScrollView:
            Label:
                id: chat_logs
                text: "مرحباً بك في النسخة التجريبية الأولى..."
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]
''')

class LoginScreen(Screen):
    def login(self):
        # هنا سنربط مستقبلاً بنظام الحسابات
        self.manager.current = 'chat'

class ChatScreen(Screen):
    pass

class GlobalChatApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == '__main__':
    GlobalChatApp().run()
