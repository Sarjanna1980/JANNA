from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class MyRoot(BoxLayout):

    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

        # Create references to the TextInput widgets
        self.input1 = self.ids['input1']
        self.input2 = self.ids['input2']
        self.input3 = self.ids['input3']
        self.input4 = self.ids['input4']

    def calc_symbol(self, symbol):
        if symbol == "Submit":
            try:
                wanted_concentration = float(self.input1.text)
                current_concentration = float(self.input2.text)
                current_volume = float(self.input3.text)

                if current_concentration != 0:
                    volume_to_add = (current_concentration * current_volume) / wanted_concentration
                    self.input4.text = str(volume_to_add)
                else:
                    self.input4.text = "Error: Division by zero"
            except ValueError:
                self.input4.text = "Error: Invalid input"
        elif symbol == "Reset":
            # Reset the text in all input fields
            self.input1.text = ""
            self.input2.text = ""
            self.input3.text = ""
            self.input4.text = ""
        elif symbol == "Close":
            # Close the Kivy application
            App.get_running_app().stop()

class NeuralCalc(App):

    def build(self):
        return MyRoot()

if __name__ == '__main__':
    neuralcalc = NeuralCalc()
    neuralcalc.run()
