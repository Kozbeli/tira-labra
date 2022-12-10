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
    slider_key_size = 0
    slider_key_size_text = StringProperty("key size")

    key_generator = NewKeyGenerator()
    public_key = 0
    private_key = 0
    key_pair = (0, 0)
    key_pair_text = StringProperty("key pair")
    generation_time = StringProperty("0")

    message_input = StringProperty("")
    encrypted_message = 0
    encrypted_message_text = StringProperty("...")
    decrypted_message_text = StringProperty("...")

    def handle_generate_key_pair(self):
        start = time.time()
        self.key_generator.generate_key_pair(self.slider_key_size)
        end = time.time()
        self.generation_time = str(end - start)

    def handle_slider_change(self, widget):
        self.slider_key_size = pow(2, int(widget.value))
        self.slider_key_size_text = str(pow(2, int(widget.value)))

    def handle_encryption(self, widget):
        self.logger("start encryption")
        self.message_input = str(widget.text)
        self.encrypted_message = Cypher.encrypt(
            self, self.message_input, self.key_generator.get_public_key())
        self.encrypted_message_text = str(self.encrypted_message)
        self.logger("end encryption")

    def handle_decryption(self, widget):
        self.logger("start decryption")
        self.decrypted_message_text = Cypher.decrypt(
            self, self.encrypted_message, self.key_generator.get_private_key())
        self.logger("end decryption")

    def logger(self, phase=""):
        print("")
        print(f"phase: {phase}")
        print("")
        print(f"message input: {self.message_input}")
        print(f"encrypted message: {self.encrypted_message}")
        print(f"encrypted message text: {self.encrypted_message_text}")
        print(f"decrypted message text: {self.decrypted_message_text}")
        print("")


# class UserInterface(GridLayout):
#     count = 0
#     count_enabled = BooleanProperty(False)
#     my_text = StringProperty("1")
#     text_input_str = StringProperty("foo")
#     # slider_value_txt = StringProperty("Value")

#     def on_button_click(self):
#         print("Button clicked")
#         if self.count_enabled:
#             self.count += 1
#             self.my_text = str(self.count)

#     def on_toggle_button_state(self, widget):
#         print("toggle state: " + widget.state)
#         if widget.state == "normal":
#             widget.text = "OFF"
#             self.count_enabled = False
#         else:
#             widget.text = "ON"
#             self.count_enabled = True

#     def on_switch_active(self, widget):
#         print("Switch: " + str(widget.active))

#     # def on_slider_value(self, widget):
#         # print("Slider: " + str(int(widget.value)))
#         # self.slider_value_txt = str(int(widget.value))

#     def on_text_validate(self, widget):
#         self.text_input_str = widget.text
