from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class PosApp(App):
    def __init__(self):
        super().__init__()
        self.total = 0.00  # Total bill amount
        self.new_item_price = 0.00  # New item price

    def build(self):
        # Main layout
        self.main_layout = BoxLayout(
            orientation="vertical", padding=10, spacing=10)

        # Total bill label
        self.total_label = Label(
            text=f"Total Bill: £{self.total:.2f}", font_size=20)
        self.main_layout.add_widget(self.total_label)

        # Add item button
        add_item_button = Button(text="Add Item", size_hint=(1, 0.3))
        add_item_button.bind(on_press=self.open_add_item_popup)
        self.main_layout.add_widget(add_item_button)

        return self.main_layout

    def open_add_item_popup(self, instance):
        # Popup layout
        popup_layout = BoxLayout(
            orientation="vertical", padding=10, spacing=10)

        # Item price input
        item_price_label = Label(text="Item Price (£):", font_size=18)
        self.item_price_input = TextInput(
            hint_text="Enter price", multiline=False, input_filter="float")
        popup_layout.add_widget(item_price_label)
        popup_layout.add_widget(self.item_price_input)

        # Add to bill button
        add_button = Button(text="Add to Bill", size_hint=(1, 0.3))
        add_button.bind(on_press=self.add_to_bill)
        popup_layout.add_widget(add_button)

        # Create and display popup
        self.popup = Popup(title="Add Item to Bill",
                           content=popup_layout, size_hint=(0.8, 0.5))
        self.popup.open()

    def add_to_bill(self, instance):
        try:
            # Get item price and update total
            self.new_item_price = float(self.item_price_input.text)
            self.total += self.new_item_price
            self.total_label.text = f"Total Bill: £{self.total:.2f}"
            self.popup.dismiss()  # Close popup
        except ValueError:
            # Handle invalid input
            invalid_popup = Popup(
                title="Invalid Input",
                content=Label(text="Please enter a valid number."),
                size_hint=(0.6, 0.4),
            )
            invalid_popup.open()


if __name__ == "__main__":
    PosApp().run()
