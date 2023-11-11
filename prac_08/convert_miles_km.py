from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KILOMETRE_CONVERSION_RATE = 1.60934


class MilesToKilometresConverterApp(App):
    """MilesToKilometresConverterApp is a Kivy App for converting miles to kilometres."""
    output_kilometres = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation"""
        miles = self.convert_text_to_float(text)
        self.display_kilometres(miles)

    def handle_increment(self, text, change):
        """Handle up/down button presses, update text input with new value and run calculation function."""
        miles = self.convert_text_to_float(text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod
    def convert_text_to_float(text):
        """Convert text to float or 0.0 if text invalid (method can be static)"""
        try:
            return float(text)
        except ValueError:
            return 0.0

    def display_kilometres(self, miles):
        self.output_kilometres = str(miles * MILE_TO_KILOMETRE_CONVERSION_RATE)


MilesToKilometresConverterApp().run()
