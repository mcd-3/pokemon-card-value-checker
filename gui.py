from tkinter import *
from tkinter import messagebox
import network

# Creates the front-end of this application
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        bg_colour = "#F5F5F5"
        bg_colour_entry = "#FFFFFF"

        self.configure(bg=bg_colour)
        self.pack()
        self.master.title("Pokemon Card Price Checker")
        self.master.minsize(400, 175)
        self.master.configure(bg=bg_colour)

        self.name_label = Label(self, text="Card Name: ", font=("bold"), bg=bg_colour)
        self.name_label.grid(row=0, column=1, sticky=E, pady=(10, 5))
        self.name_entry = Entry(self, bg=bg_colour_entry)
        self.name_entry.grid(row=0, column=2, pady=(14, 5), padx=5)

        self.number_label = Label(self, text="Number: ", font=("bold"), bg=bg_colour)
        self.number_label.grid(row=1, column=1, sticky=E, pady=(8, 10))
        self.number_entry = Entry(self)
        self.number_entry.grid(row=1, column=2, padx=5, pady=(12, 10))

        self.price_label = Label(self, text="Price: ", font=("bold"), bg=bg_colour)
        self.price_label.grid(row=2, column=1, sticky=E, pady=(12, 10))
        self.price_text = Label(self, text="$0.00", font=("bold"), bg=bg_colour)
        self.price_text.grid(row=2, column=2, sticky=W, pady=(12, 10))

        self.submit_button = Button(self, text="Get Price", command=self.get_price)
        self.submit_button.grid(row=3, column=1, columnspan=2, pady=(20, 10), ipadx=35, ipady=5)

    # Grab the price and change the label
    def get_price(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name.strip() != "" and number.strip() != "":
            price = network.grab_price(name, number)
            price_str = ""
            if price == '0':
                price_str = "Not Found"
            else:
                price_str = "$" + price
            self.price_text.config(text=price_str)
        else:
            messagebox.showinfo(title="Invalid Entries", message="Please give a valid name and number")