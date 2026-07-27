import threading
from server import app
from kivy.app import App
from kivy.uix.label import Label

def run_flask():
    app.run(host='127.0.0.1', port=8080)

class CardApp(App):
    def build(self):
        # تشغيل سيرفر الفلاسك في الخلفية
        threading.Thread(target=run_flask, daemon=True).start()
        return Label(text="شبكة عيسى تعمل بنجاح!")

if __name__ == '__main__':
    CardApp().run()
