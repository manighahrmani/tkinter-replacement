# type: ignore
# pylint: disable=no-name-in-module, import-error
import flet as ft


class PosApp:
    def __init__(self):
        self.total = 0.00  # Total bill amount
        self.new_item_price = 0.00  # New item price input

    def main(self, page: ft.Page):
        page.title = "POS System"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Label for displaying the total bill
        total_label = ft.Text(f"Total Bill: £{self.total:.2f}", size=20)

        # Function to update total bill
        def update_total_bill():
            item_price = float(item_price_field.value)
            self.total += item_price
            item_price_field.value = ""  # Clear the input field
            total_label.value = f"Total Bill: £{self.total:.2f}"
            add_item_dialog.open = False  # Close the dialog
            page.update()

        # Button to open the "Add Item" dialog
        def open_add_item_dialog(e):
            add_item_dialog.open = True
            page.update()

        add_item_button = ft.ElevatedButton(
            "Add Item", on_click=open_add_item_dialog)

        # Dialog for adding an item
        item_price_field = ft.TextField(
            label="Item Price (£)", keyboard_type=ft.KeyboardType.NUMBER)
        add_item_button_dialog = ft.ElevatedButton(
            "Add to Bill", on_click=lambda e: update_total_bill())

        add_item_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Add Item to Bill"),
            content=ft.Column([item_price_field]),
            actions=[add_item_button_dialog],
        )

        # Add components to the page
        page.add(
            ft.Column(
                [total_label, add_item_button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        page.dialog = add_item_dialog


# Entry point of the program
def main():
    app = PosApp()
    ft.app(target=app.main)


main()
