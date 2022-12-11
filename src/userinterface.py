from kivy.graphics import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from cypher import Cypher
from newkeygenerator import NewKeyGenerator
import time


class UserInterface(BoxLayout):
    """ Käyttöliittymä.

    Attributes:
        key_generator (NewKeyGenerator): avainparin generoija
        slider_key_size (int): sliderin arvo
        slider_key_size_text (str): sliderin arvo tekstimuodossa
        encrypted_message (int): salattu viesti
        encrypted_message_text (str): salattu viesti tekstimuodossa
        decrypted_message_text (str): purettu viesti tekstimuodossa
        generation_time (str): avaimenparin generoinnin kesto
        encryption_time (str): salauksen kesto
        decryption_time (str): purun kesto
    """

    key_generator = NewKeyGenerator()

    slider_key_size = 512
    slider_key_size_text = StringProperty("key size")

    encrypted_message = 0
    encrypted_message_text = StringProperty("...")
    decrypted_message_text = StringProperty("...")

    generation_time = StringProperty("0")
    encryption_time = StringProperty("0")
    decryption_time = StringProperty("0")

    def handle_generate_key_pair(self):
        """ Generoi uuden avaimenparin ja laskee sen keston."""

        start = time.time()
        self.key_generator.generate_key_pair(self.slider_key_size)
        end = time.time()
        self.generation_time = str(end - start)

    def handle_slider_change(self, widget):
        """ Käsittelee sliderin muutoksen ja päivittää näytön.

        Args:
            widget (Slider): slider
        """

        self.slider_key_size = pow(2, int(widget.value))
        self.slider_key_size_text = str(pow(2, int(widget.value)))

    def handle_encryption(self, widget):
        """ Käsittelee viestin salauksen ja laskee sen keston.

        Args:
            widget (TextInput): tekstikenttä
        """

        start = time.time()
        self.encrypted_message = Cypher.encrypt(
            self, str(widget.text), self.key_generator.get_public_key())
        end = time.time()
        self.encrypted_message_text = str(self.encrypted_message)
        self.encryption_time = str(end - start)

    def handle_decryption(self):
        """ Käsittelee salauksen purun ja laskee sen keston.

        Args:
            widget (TextInput): tekstikenttä
        """

        start = time.time()
        self.decrypted_message_text = Cypher.decrypt(
            self, self.encrypted_message, self.key_generator.get_private_key())
        end = time.time()
        self.decryption_time = str(end - start)
