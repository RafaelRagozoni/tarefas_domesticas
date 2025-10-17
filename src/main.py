import kivy
import random
import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


MEDIA_DIR=os.environ["MEDIA_DIR"]

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
        images_texts = ["Milena", "Mamaco", "Tigrinho","FAZUELI","pescador"]
        btn = []
        for i in range(5):
            btn.append(Button(
                text=images_texts[i], background_color=random.choice(colors)
            ))
            btn[i].bind(on_press=lambda instance, index_fixo=i: self.on_press_button(instance, index_fixo))
            layout_left.add_widget(btn[i])
        self.img = Image()
        layout_right.add_widget(self.img)
        layout_all.add_widget(layout_left)
        layout_all.add_widget(layout_right)
        return layout_all

    def on_press_button(self, instance, idx):
        paths=[
            "milena.png",
            "mamaco.png",
            "tigrinho.png",
            "L.png",
            "pescador.png"
        ]
        nova_imagem_source = f"{MEDIA_DIR}/{paths[idx]}"
        self.img.source = nova_imagem_source        
        self.img.reload() 
        print(f"You pressed the button {idx}, loaded {paths[idx]}!")


class TestekvApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print("You pressed the button!")


if __name__ == "__main__":
    app = HBoxLayoutExample()
    # app = TestekvApp()
    app.run()
