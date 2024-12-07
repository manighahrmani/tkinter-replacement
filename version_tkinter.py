from tkinter import *


class PosApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("POS System")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

        self.total = DoubleVar()
        self.total.set(0.00)

        self.newItemPrice = DoubleVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        totalLabel = Label(
            self.mainFrame,
            text=f"Total Bill: £{self.total.get():.2f}"
        )
        totalLabel.pack(padx=5, pady=5)

        addItemButton = Button(
            self.mainFrame,
            text="Add Item",
            command=lambda: self.createNewWin(totalLabel)
        )
        addItemButton.pack(padx=5, pady=5)

    def createNewWin(self, totalLabel):
        newWin = Toplevel(self.win)
        newWin.title("Add Item to Bill")

        newWinFrame = Frame(newWin)
        newWinFrame.pack(padx=10, pady=10)

        itemPriceLabel = Label(newWinFrame, text="Item Price (£):")
        itemPriceLabel.pack(padx=5, pady=5)

        itemPriceEntry = Entry(
            newWinFrame,
            textvariable=self.newItemPrice
        )
        itemPriceEntry.pack(padx=5, pady=5)

        addButton = Button(
            newWinFrame,
            text="Add to Bill",
            command=lambda: self.updateBill(
                totalLabel, newWin)
        )
        addButton.pack(padx=5, pady=5)

    def updateBill(self, totalLabel, newWin):
        newTotal = self.total.get() + self.newItemPrice.get()
        # Update the total (this does not update the label)
        self.total.set(newTotal)
        self.newItemPrice.set(0.00)  # Reset the entry box for the new item
        totalLabel.config(
            text=f"Total Bill: £{self.total.get():.2f}")
        # Without the config line, the totalLabel will not update

        newWin.destroy()


def main():
    app = PosApp()
    app.run()


main()
