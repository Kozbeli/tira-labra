from userinterface import UserInterface
from kivy.app import App
from kivy.config import Config
import kivy
kivy.require('2.1.0')

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')


class RsaEncryptionApp(App):
    pass


RsaEncryptionApp().run()
