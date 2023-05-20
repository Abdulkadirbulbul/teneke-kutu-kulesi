from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window


class CalculatorApp(App):
    def build(self):
        self.expression = ""

        # Set the window size
        Window.size = (300, 400)

        # Create the layout
        layout = GridLayout(cols=4, padding=10, spacing=10)

        # Create the buttons
        layout.add_widget(Button(text="7", on_press=self.add_text))
        layout.add_widget(Button(text="8", on_press=self.add_text))
        layout.add_widget(Button(text="9", on_press=self.add_text))
        layout.add_widget(Button(text="/", on_press=self.add_text))

        layout.add_widget(Button(text="4", on_press=self.add_text))
        layout.add_widget(Button(text="5", on_press=self.add_text))
        layout.add_widget(Button(text="6", on_press=self.add_text))
        layout.add_widget(Button(text="*", on_press=self.add_text))

        layout.add_widget(Button(text="1", on_press=self.add_text))
        layout.add_widget(Button(text="2", on_press=self.add_text))
        layout.add_widget(Button(text="3", on_press=self.add_text))
        layout.add_widget(Button(text="-", on_press=self.add_text))

        layout.add_widget(Button(text="C", on_press=self.clear_text))
        layout.add_widget(Button(text="0", on_press=self.add_text))
        layout.add_widget(Button(text=".", on_press=self.add_text))
        layout.add_widget(Button(text="+", on_press=self.add_text))

        layout.add_widget(Button(text="=", on_press=self.calculate, size_hint=(1, .5), font_size=20))

        return layout

    def add_text(self, button):
        self.expression += button.text

    def clear_text(self, button):
        self.expression = ""

    def calculate(self, button):
        try:
            self.expression = str(eval(self.expression))
        except ZeroDivisionError:
            self.expression = "Divide by zero error"
        except:
            self.expression = "Error"

    def on_pause(self):
        return True


if __name__ == "__main__":
    CalculatorApp().run()