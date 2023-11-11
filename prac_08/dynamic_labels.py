from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App for dynamically creating a Label for each name in a list."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Dylan", "Riley", "Sarah", "Mitchell", "Harry", "Bob"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.names_box.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
