
# Imports
from tkinter import *
from tkinter import ttk

# Define calculate function
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

# Create root window
root = Tk()
root.title("Feet to Meters")

# Create mainframe to hold widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create feet entry box
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Create meters label
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Create calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W
)

# Configure padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Set focus on feet entry box
feet_entry.focus()

# Bind return key to calculate function
root.bind("<Return>", calculate)

# Start mainloop
root.mainloop()
