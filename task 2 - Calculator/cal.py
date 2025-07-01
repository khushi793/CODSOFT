import tkinter as tk
from tkinter import messagebox

# ------------------ FUNCTIONS ------------------

def button_click(value):
    current = display_var.get()
    if current == "0" or current == "Error":
        display_var.set(str(value))
    else:
        display_var.set(current + str(value))

def clear_display():
    display_var.set("0")

def delete_last():
    current = display_var.get()
    if current not in ["0", "Error"]:
        display_var.set(current[:-1] if len(current) > 1 else "0")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(round(result, 4)))
    except:
        display_var.set("Error")

# ------------------ UI SETUP ------------------

# Main window
app = tk.Tk()
app.title("🎨 Creative Calculator")
app.geometry("330x470")
app.configure(bg="#f0f4f8")
app.resizable(False, False)

# Display
display_var = tk.StringVar(value="0")
display_label = tk.Label(
    app, textvariable=display_var, font=("Consolas", 24), bg="#e0f7fa",
    fg="#222", anchor="e", relief="sunken", bd=5, padx=10, pady=15
)
display_label.pack(fill="x", padx=15, pady=(20, 10))

# ------------------ BUTTONS ------------------

button_style = {
    "font": ("Helvetica", 14),
    "width": 5,
    "height": 2,
    "bd": 0,
    "relief": "raised"
}

# Button layout
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Button colors
color_map = {
    "C": "#f44336",
    "⌫": "#ff9800",
    "=": "#4caf50",
    "/": "#03a9f4", "*": "#03a9f4", "-": "#03a9f4", "+": "#03a9f4",
    "%": "#9c27b0"
}

# Button action mapping
def get_command(label):
    if label == "=":
        return calculate
    elif label == "C":
        return clear_display
    elif label == "⌫":
        return delete_last
    else:
        return lambda: button_click(label)

# Frame for buttons
btn_frame = tk.Frame(app, bg="#f0f4f8")
btn_frame.pack(pady=5)

# Generate buttons
for r, row in enumerate(buttons):
    for c, btn_text in enumerate(row):
        if btn_text == "":
            continue
        bg_color = color_map.get(btn_text, "#ffffff")
        fg_color = "white" if btn_text in color_map else "#333"

        btn = tk.Button(
            btn_frame, text=btn_text, command=get_command(btn_text),
            bg=bg_color, fg=fg_color, **button_style
        )
        btn.grid(row=r, column=c, padx=7, pady=7)

# Footer
footer = tk.Label(app, text="Made with ❤️ by You", bg="#f0f4f8", fg="#555", font=("Arial", 10))
footer.pack(pady=10)

# Run the app
app.mainloop()
