"""This app shows the implementation of using dynamic widgets"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicWidgets(App):
    """Main program for dynamic widgets"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names
        self.names = ["Lucas", "Maya", "Ethan"]

    def build(self):
        """Build main app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.status_text = "Creating names..."
        name_box = self.root.ids.name_box

        for name in self.names:
            label = Label(text=name)
            name_box.add_widget(label)








DynamicWidgets().run()
