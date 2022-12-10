import kivy
kivy.require('2.1.0')

from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')

from kivy.app import App
from userinterface import UserInterface


class RsaEncryptionApp(App):
    pass


RsaEncryptionApp().run()
