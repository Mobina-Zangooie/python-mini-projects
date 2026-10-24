
import os
import tkinter as tk
from tkinter import ttk
import calculator_functions as cf

# Create the main window of the application
window = tk.Tk()

# Set the title shown at the top of the window
window.title("ماشین حساب")

# Load the icon image from a file (must be PNG or GIF)
# The icon is looked up next to this file, so the app works from any folder
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_icon.png")
icon = tk.PhotoImage(file=icon_path)

# Set it as the window icon (True = also use it for any new windows)
window.iconphoto(True, icon)

# Set the window size (width x height, in pixels)
window.geometry("400x600")

# Create a label inside "window" (no fixed width, so it can stretch)
label = tk.Label(window,
                 text='به برنامه ماشین حساب خوش آمدید',
                 fg='white',
                 font=('vazir', 14),  # (font name, size)
                 bg='#0077B6',
                 height=3)

# Place the label in the window and stretch it horizontally to fill the full width
label.pack(fill='x', pady=10, padx=5)

# Create a frame (an invisible box) that will hold both entries on one line
entries_frame = tk.Frame(window)

# Place the frame in the window with some vertical space around it
entries_frame.pack(pady=10)

# Create the first entry inside the frame
entry1 = tk.Entry(entries_frame,
                  width=15,                  # width in characters
                  fg='white',
                  font=('vazir', 14),  # (font name, size)
                  bg='#0096c7',
                  insertbackground="#CAF0F8",  # color of the blinking text cursor
                  )

# Place entry1 on the left side of the frame
entry1.pack(side='left', padx=5)

# Create the second entry with the same settings
entry2 = tk.Entry(entries_frame,
                  width=15,
                  fg='white',
                  font=('vazir', 14),  # (font name, size)
                  bg='#0096c7',
                  insertbackground="#CAF0F8")

# Place entry2 next to entry1
entry2.pack(side='left', padx=5)

# Create an empty label that will show the result
result_label = tk.Label(window, 
                        text='',
                        fg='white',
                        font=('vazir', 12),  # (font name, size)
                        bg='#00B4D8',
                        )

# Place the label in the window
result_label.pack(pady=10, padx=27, fill='x')

# Format a result and show it in the result label
def show_result(result):
    # Round to 2 decimal places to hide tiny floating-point errors
    result = round(result, 2)

    # If the result is a whole number (like 5.0), convert it to int so it is shown as 5
    if result.is_integer():
        result = int(result)

    # Display the final value in the result label
    result_label.config(text=result)

# Read both entries, run the given operation on them, and show the result
def calculate(operation):
    # First try: convert the entries' text into numbers
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        # The user left an entry empty or typed something that is not a number
        result_label.config(text="لطفاً دو عدد معتبر وارد کنید")
        return  # stop the function here

    # Second try: run the operation that was passed in
    try:
        result = operation(num1, num2)
    except ValueError as e:
        # e holds the message we wrote in functions (e.g. division by zero)
        result_label.config(text=str(e))
        return  # stop the function here
    except OverflowError:
        # The result is too big for a float to hold
        result_label.config(text="نتیجه خیلی بزرگ است")
        return

    # Everything worked, so show the result
    show_result(result)
    
# Map each (from unit, to unit) pair to the function that does the conversion
# Note: the functions are written WITHOUT parentheses, we only store them here
conversions = {
    ("سلسیوس", "کلوین"): cf.C_to_K,
    ("کلوین", "سلسیوس"): cf.K_to_C,
    ("سلسیوس", "فارنهایت"): cf.C_to_F,
    ("فارنهایت", "سلسیوس"): cf.F_to_C,
    ("کلوین", "فارنهایت"): cf.K_to_F,
    ("فارنهایت", "کلوین"): cf.F_to_K,
}

# Read the dropdowns and the entry, convert the temperature, and show the result
def temperature_transition():
    # Read both combo boxes
    base, dest = combo1.get(), combo2.get()

    # Convert the first entry's text into a number
    try:
        value = float(entry1.get())
    except ValueError:
        # The user left the entry empty or typed something that is not a number
        result_label.config(text="لطفاً عدد معتبر وارد کنید")
        return  # stop the function here

    # Same unit on both sides: nothing to convert
    if base == dest:
        result = value
    else:
        # Find the right function for this pair, then call it with the value
        result = conversions[(base, dest)](value)

    # Round, format and display the result
    show_result(result)
    
    
# Create and place a frame
operation1_frame = tk.Frame(window)
operation1_frame.pack(pady=10)   

# Create the add button and place it; command gets the function name WITHOUT parentheses
add_but = tk.Button(operation1_frame, width=10, text='+', command=lambda: calculate(cf.add), bg='#48CAE4', fg='white', font=('vazir',14))
add_but.pack(side='left', padx=8)

# Create the subtract button and place it; command gets the function name WITHOUT parentheses
sub_but = tk.Button(operation1_frame, width=10, text='-', command=lambda: calculate(cf.subtract), bg='#48CAE4', fg='white', font=('vazir',14))
sub_but.pack(side='left', padx=8)

# Create and place a frame
operation2_frame = tk.Frame(window)
operation2_frame.pack(pady=10)

# Create the multiply button and place it; command gets the function name WITHOUT parentheses
mul_but = tk.Button(operation2_frame, width=10, text='x', command=lambda: calculate(cf.multiply), bg='#48CAE4', fg='white', font=('vazir',14))
mul_but.pack(side='left', padx=8)   

# Create the divide button and place it; command gets the function name WITHOUT parentheses
dvd_but = tk.Button(operation2_frame, width=10, text='÷', command=lambda: calculate(cf.divide), bg='#48CAE4', fg='white', font=('vazir',14))
dvd_but.pack(side='left', padx=8)

# Create the power button and place it; command gets the function name WITHOUT parentheses
pow_but = tk.Button(window, width=10, text='**', command=lambda: calculate(cf.power), bg='#48CAE4', fg='white', font=('vazir',14))
pow_but.pack(pady=10)

# Create and place a frame
combobox_frame = tk.Frame(window)
combobox_frame.pack(pady=10)

# Create a dropdown whose options are the three units
combo1 = ttk.Combobox(
    combobox_frame,
    font= ('vazir', 14),
    width=10,
    values=["سلسیوس", "کلوین", "فارنهایت"],
    state="readonly",
)

# Select the first option by default (index 0)
combo1.current(0)

# Place the first dropdown
combo1.pack(side='left', padx=10)

# Create a dropdown whose options are the three units
combo2 = ttk.Combobox(
    combobox_frame,
    font= ('vazir', 14),
    width=10,
    values=["سلسیوس", "کلوین", "فارنهایت"],
    state="readonly",
)

# Select the second option by default (index 1)
combo2.current(1)
# Place the first dropdown
combo2.pack(side='left', padx=10)

# Create the temperature transition button and place it; command gets the function name WITHOUT parentheses
temp_but = tk.Button(window, width=10, text='تبدیل دما', command= temperature_transition, bg='#48CAE4', fg='white', font=('vazir',14))
temp_but.pack(pady=10)

# Keep the window open until the user closes it
window.mainloop()
