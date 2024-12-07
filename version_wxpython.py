# type: ignore
# pylint: disable=no-name-in-module, import-error
import wx


class PosApp(wx.Frame):
    def __init__(self, parent=None, title="POS System"):
        super().__init__(parent, title=title, size=(300, 200))
        self.total = 0.00
        self.newItemPrice = 0.00

        # Main panel and sizer
        panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(self.main_sizer)

        # Create Widgets
        self.create_widgets(panel)

        self.Centre()
        self.Show()

    def create_widgets(self, panel):
        # Display the total bill label
        self.total_label = wx.StaticText(
            panel, label=f"Total Bill: £{self.total:.2f}")
        self.main_sizer.Add(self.total_label, 0, wx.ALL | wx.CENTER, 10)

        # Add Item button
        add_item_button = wx.Button(panel, label="Add Item")
        add_item_button.Bind(wx.EVT_BUTTON, self.create_new_win)
        self.main_sizer.Add(add_item_button, 0, wx.ALL | wx.CENTER, 10)

    def create_new_win(self, event):
        # Create a new window for adding an item
        new_win = wx.Dialog(self, title="Add Item to Bill", size=(250, 150))

        # Dialog panel and sizer
        panel = wx.Panel(new_win)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Item price label and text control
        item_price_label = wx.StaticText(panel, label="Item Price (£):")
        sizer.Add(item_price_label, 0, wx.ALL | wx.CENTER, 5)

        self.item_price_ctrl = wx.TextCtrl(panel)
        sizer.Add(self.item_price_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # Add button
        add_button = wx.Button(panel, label="Add to Bill")
        add_button.Bind(wx.EVT_BUTTON, lambda event: self.update_bill(new_win))
        sizer.Add(add_button, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)
        new_win.Centre()
        new_win.ShowModal()

    def update_bill(self, dialog):
        try:
            # Get the item price from the text control
            item_price = float(self.item_price_ctrl.GetValue())
            self.total += item_price

            # Update the total bill label
            self.total_label.SetLabel(f"Total Bill: £{self.total:.2f}")

            # Close the dialog
            dialog.Destroy()
        except ValueError:
            wx.MessageBox("Please enter a valid number.",
                          "Error", wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = wx.App(False)
    PosApp()
    app.MainLoop()
