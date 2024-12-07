# type: ignore
# pylint: disable=no-name-in-module, import-error
import gi
from gi.repository import Gtk, GObject
gi.require_version("Gtk", "3.0")


class PosApp:

    def __init__(self):
        self.win = Gtk.Window(title="POS System")
        self.win.connect("destroy", Gtk.main_quit)

        self.mainFrame = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.win.add(self.mainFrame)

        self.total = GObject.Double(0.00)
        self.newItemPrice = GObject.Double(0.00)

    def run(self):
        self.createWidgets()
        self.win.show_all()
        Gtk.main()

    def createWidgets(self):
        self.totalLabel = Gtk.Label(label=f"Total Bill: £{self.total:.2f}")
        self.mainFrame.pack_start(self.totalLabel, True, True, 5)

        addItemButton = Gtk.Button(label="Add Item")
        addItemButton.connect("clicked", self.createNewWin)
        self.mainFrame.pack_start(addItemButton, True, True, 5)

    def createNewWin(self, button):
        newWin = Gtk.Window(title="Add Item to Bill")
        newWin.set_transient_for(self.win)
        newWin.set_modal(True)

        newWinFrame = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        newWin.add(newWinFrame)

        itemPriceLabel = Gtk.Label(label="Item Price (£):")
        newWinFrame.pack_start(itemPriceLabel, True, True, 5)

        self.itemPriceEntry = Gtk.Entry()
        newWinFrame.pack_start(self.itemPriceEntry, True, True, 5)

        addButton = Gtk.Button(label="Add to Bill")
        addButton.connect("clicked", lambda w: self.updateBill(newWin))
        newWinFrame.pack_start(addButton, True, True, 5)

        newWin.show_all()

    def updateBill(self, newWin):
        try:
            new_item_price = float(self.itemPriceEntry.get_text())
        except ValueError:
            new_item_price = 0.00

        self.total += new_item_price
        self.totalLabel.set_text(f"Total Bill: £{self.total:.2f}")
        self.itemPriceEntry.set_text("")
        newWin.destroy()


def main():
    app = PosApp()
    app.run()


if __name__ == "__main__":
    main()
