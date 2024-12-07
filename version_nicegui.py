from nicegui import ui


class PosApp:
    def __init__(self):
        # Initialize total and UI attributes
        self.total = 0.00
        self.total_label = None  # Placeholder for the total label
        self.item_price_input = None  # Placeholder for the input field

    def render(self):
        # Set the page title
        ui.label("Point of Sale (POS) System").classes(
            "text-2xl font-bold mb-4")

        # Display current total
        self.total_label = ui.label(
            f"Total Bill: £{self.total:.2f}").classes("text-lg mb-4")

        # Item price input
        self.item_price_input = ui.number(
            label="Enter Item Price (£)",
            value=0.00,
            step=0.01,
            min=0.00,
        ).classes("mb-4")

        # Add item button
        ui.button("Add Item", on_click=self.add_item).classes("mr-2")

        # Reset button
        ui.button("Reset Bill", on_click=self.reset_bill).classes(
            "bg-red-500 text-white")

    def add_item(self):
        item_price = self.item_price_input.value
        if item_price > 0:
            # Update total
            self.total += item_price

            # Update the total label
            self.total_label.set_text(f"Total Bill: £{self.total:.2f}")

            # Provide feedback
            ui.notify(f"Added item: £{item_price:.2f}", color="green")

    def reset_bill(self):
        # Reset total
        self.total = 0.00

        # Update the total label
        self.total_label.set_text(f"Total Bill: £{self.total:.2f}")

        # Provide feedback
        ui.notify("Bill reset successfully!", color="red")


def main():
    app = PosApp()
    with ui.row().classes("w-full justify-center"):
        app.render()

    # Start NiceGUI app
    ui.run(title="POS System")


if __name__ in {"__main__", "__mp_main__"}:
    main()
