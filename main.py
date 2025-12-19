from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ScannerUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(
            text="[b][color=00ff00]SECURITY SCANNER[/color][/b]",
            markup=True,
            font_size=24
        ))

        self.result = Label(
            text="Ready to scan.\nNo admin required.",
            size_hint_y=None,
            height=300
        )

        scroll = ScrollView()
        scroll.add_widget(self.result)
        self.add_widget(scroll)

        btn = Button(text="START SCAN", size_hint_y=None, height=60)
        btn.bind(on_press=self.fake_scan)
        self.add_widget(btn)

    def fake_scan(self, instance):
        self.result.text = (
            "Scanning downloads...\n"
            "Checking links...\n"
            "No threats found.\n\n"
            "[color=00ff00]System Safe[/color]"
        )

class ScannerApp(App):
    def build(self):
        return ScannerUI()

ScannerApp().run()
