from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyGridLayout(GridLayout):
    # constructor
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        self.add_widget(Label(text="Favorite programming language: "))
        self.language = TextInput(multiline=False)
        self.add_widget(self.language)

        # Add submit button
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        color = self.color.text
        language = self.language.text
        if (name=="kadir"):
            print("kadi sakadsmöas")

        print(f'Hello {name}, your favorite color is {color}, and your favorite programming language is {language}!')

        # Clear the input boxes
        self.name.text = ""
        self.color.text = ""
        self.language.text = ""

class TestApp(App):
    def build(self):
        return MyGridLayout()

TestApp().run()
