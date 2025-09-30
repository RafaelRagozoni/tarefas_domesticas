import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class HBoxLayoutExample(App):
    def build(self):
        layout_all = BoxLayout(padding=10)
        layout_left = BoxLayout(orientation="vertical")
        layout_right = BoxLayout()
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(
                text="Button #%s" % (i + 1), background_color=random.choice(colors)
            )
            btn.bind(on_press=lambda instance: self.on_press_button(instance, i))

            layout_left.add_widget(btn)
        img = Image(
            source="milena.png",
        )
        layout_right.add_widget(img)
        layout_all.add_widget(layout_left)
        layout_all.add_widget(layout_right)
        return layout_all

    def on_press_button(self, instance, button_number):
        print(f"You pressed the button {button_number}!")


class TestekvApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print("You pressed the button!")


if __name__ == "__main__":
    app = HBoxLayoutExample()
    # app = TestekvApp()
    app.run()
