from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Window.size = 300, 500
class mostrar_texto(MDApp):
    def build(self):
        self.theme_cls.primary_pallete = 'Dark_Blue'
        self.theme_cls.theme_style = 'Dark'

    def mudar_texto(self):
        field = self.root.ids.field.text
        title = self.root.ids.title

        title.text = field
        print(title.text)



if __name__ == '__main__':
    mostrar_texto().run()
