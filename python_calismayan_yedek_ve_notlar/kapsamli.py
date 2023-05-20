from kivy.lang import Builder
from kivymd.app import MDApp

kv = '''
Screen:
    <MyWidget>:
        canvas:
            Color:
                rgba: 0.2, 0.2, 0.2, 1
            Ellipse:
                pos: self.center_x - dp(50), self.center_y - dp(50)
                size: dp(100), dp(100)
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint: 1, 0.1

            MDLabel:
                text: 'Alt kutu 1:'
                size_hint_x: 0.3

            MDTextField:
                id: lower_box1_label
                hint_text: 'Alt kutu 1 değerini girin'
                input_filter: 'int'
                helper_text_mode: 'on_error'
                helper_text: 'Lütfen bir sayı girin'
                size_hint_x: 0.7

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint: 1, 0.1

            MDLabel:
                text: 'Alt kutu 2:'
                size_hint_x: 0.3

            MDTextField:
                id: lower_box2_label
                hint_text: 'Alt kutu 2 değerini girin'
                input_filter: 'int'
                helper_text_mode: 'on_error'
                helper_text: 'Lütfen bir sayı girin'
                size_hint_x: 0.7

        MDLabel:
            text: 'Üst kutu:'
            halign: 'center'
            font_style: 'H5'
            size_hint: 1, 0.1

        MDTextField:
            id: upper_box_label
            hint_text: 'Üst kutunun numarasını girin'
            input_filter: 'int'
            helper_text_mode: 'on_error'
            helper_text: 'Lütfen bir sayı girin'
            size_hint: 1, 0.1

        MDLabel:
            text: 'Sonuç:'
            halign: 'center'
            font_style: 'H5'
            size_hint: 1, 0.1

        MDTextField:
            id: result_field
            hint_text: 'Sonuç burada görünecek'
            readonly: True
            size_hint: 1, 0.2

        MDRectangleFlatButton:
            text: 'Hesapla'
            on_press: app.calculate_box_number()
            size_hint: 1, 0.1
'''

class TinCanTowerApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "900"
        screen = Builder.load_string(kv)
        return screen

    def calculate_box_number(self):
        lower_box1_text = self.root.ids.lower_box1_label.text
        lower_box2_text = self.root.ids.lower_box2_label.text
        upper_box_text = self.root.ids.upper_box_label.text

        if lower_box1_text and lower_box2_text and upper_box_text:
            lower_box1_value = int(lower_box1_text)
            lower_box2_value = int(lower_box2_text)
            result = lower_box1_value+lower_box2_value

            if lower_box1_value + lower_box2_value == result:
                box_number = int(upper_box_text.split()[-1])
                result_text = f"Üstteki kutunun numarası: {box_number}"
            else:
                result_text = "Hatalı giriş yaptınız. Lütfen tekrar deneyin."
        else:
            result_text = "Lütfen tüm girdileri doldurun."

        self.root.ids.result_field.text = result_text



if __name__ == '__main__':
    TinCanTowerApp().run()
