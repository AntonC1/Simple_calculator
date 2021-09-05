from kivy.app import App
from kivy.uix.button import Button;
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Kalkulator(App):
    def build(self):
        panel_kalkulatora = BoxLayout(orientation='vertical')
        panel = Label(size_hint_y = 0.5, font_size=50)
        Przyciski =('1', '2', '3', '+',
                    '4', '5', '6', '-',
                    '7', '8', '9', '.',
                    '0', '*', '/', '=')
        plansza = GridLayout(cols=4, size_hint_y=2)
        for symbole in Przyciski:
            plansza.add_widget(Button(text=symbole))

        przyciski_czyszczenia = Button(text = 'Wyczysc', size_hint_y=None, height=150)
        def przyciskanie(instancja):
            panel.text += instancja.text
        for button in plansza.children[1:]:
            button.bind(on_press=przyciskanie)
        def resize_label_text(label, new_height):
            label.fontsize = 0.5*label.height
        panel.bind(height=resize_label_text)

        def evaluate_result(instancja):
            try:
                panel.text = str(eval(panel.text))
            except SyntaxError:
                panel.text = 'Python Syntax error!'
        plansza.children[0].bind(on_press=evaluate_result)

        def clear_label(instancja):
            panel.text = " "
        przyciski_czyszczenia.bind(on_press=clear_label)

        panel_kalkulatora.add_widget(panel)
        panel_kalkulatora.add_widget(plansza)
        panel_kalkulatora.add_widget(przyciski_czyszczenia)
        return panel_kalkulatora
Kalkulator().run()
