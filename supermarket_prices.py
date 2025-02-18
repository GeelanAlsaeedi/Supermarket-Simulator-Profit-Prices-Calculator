import tkinter as tk
from tkinter import ttk

def profit():
        enter = entry.get()

        if enter.lower() == "x":
            window.destroy()
            return
        try:
            market_price = float(enter)
            percentage = percent.get()
            profit_amount = market_price * (percentage/100)
            new_price = market_price + profit_amount
            result.config(text=f"10% profit price: {new_price:.2f}", fg="green")#dynamically set the configuration for a label already set up below and depending on which result the text will be set. 
        except ValueError:
            result.config(text= "the Value was not a number dummy!", fg="red")


window =tk.Tk() #create the main menu 
window.title("Supermarket Simulator 10% price profit")
window.geometry("400x300") #size
rounded_font = ("Baloo Bhaijaan 2", 14)


enter_label = tk.Label(window, text="Market Price:", font=rounded_font)
enter_label.pack(pady=10)

style = ttk.Style()
style.configure("Padded.TEntry", padding="10 5")
entry = ttk.Entry(window, style="Padded.TEntry", font=rounded_font)
entry.pack(pady=10, padx=10)
entry.bind("<Return>", lambda event:profit())

radio_frame = ttk.Frame(window)
radio_frame.pack(pady=10)
percent = tk.DoubleVar(value=10)#default is 10%
ttk.Radiobutton(radio_frame, text="5% Profit", variable=percent, value=5.0).pack(side="left", padx=10)
ttk.Radiobutton(radio_frame, text="8.5% Profit", variable=percent, value=8.5).pack(side="left", padx=10)
ttk.Radiobutton(radio_frame, text="10% Profit", variable=percent, value=10.0).pack(side="left", padx=10)


button = tk.Button(window, text="Calculate", command=profit, font=rounded_font)
button.pack(pady=10)

result = tk.Label(window, text="", font=rounded_font)
result.pack(pady=10)

window.mainloop()

