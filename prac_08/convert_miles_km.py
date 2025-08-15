from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder

CONVERSION_FACTOR = 1.60934

class Converter(App):
    """The class variable in the app is the 'model'."""
    result = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = "Enter a number in miles to convert"
        return self.root

    def calculation(self):
        """Handles the conversion from miles to kms"""
        try:
            miles = float(self.root.ids.user_input.text)
        except ValueError:
            self.result = f"{0.0:.2f} Kilometers"
            return

        kms = miles * CONVERSION_FACTOR
        self.result = f'{kms:.2f} Kilometers'

    def increment(self,change):
        """This handles the increments"""
        try:
            miles = float(self.root.ids.user_input.text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.user_input.text = str(miles)
        self.calculation()


# create and start the App running
Converter().run()
