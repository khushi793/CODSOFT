import tkinter as tk
from tkinter import messagebox

# Create main window
app = tk.Tk()
app.title("✨ Creative To-Do App")
app.geometry("400x550")
app.configure(bg="#f9f7f7")

# ------------------- Styling -------------------

PRIMARY_COLOR = "#3a86ff"
SECONDARY_COLOR = "#ff006e"
ACCENT_COLOR = "#8338ec"
LIGHT_BG = "#edf2fb"
BTN_FONT = ("Helvetica", 11, "bold")
ENTRY_FONT = ("Helvetica", 12)

# ------------------- Hover Effect -------------------
def on_enter(e):
    e.widget['background'] = "#4cc9f0"

def on_leave(e):
    e.widget['background'] = PRIMARY_COLOR

# ------------------- Header -------------------
header_frame = tk.Frame(app, bg=ACCENT_COLOR, height=70)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="🌟 My Creative Tasks", font=("Comic Sans MS", 18, "bold"), fg="white", bg=ACCENT_COLOR)
header_label.pack(pady=15)

# ------------------- Entry Section -------------------
entry_frame = tk.Frame(app, bg=LIGHT_BG, pady=15)
entry_frame.pack(fill="x", padx=20)

task_input = tk.Entry(entry_frame, width=28, font=ENTRY_FONT, bd=3, relief="flat")
task_input.pack(side="left", padx=5)

def add_task():
    task = task_input.get()
    if task.strip():
        task_list.insert(tk.END, "🔹 " + task)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Type something to add!")

# Add Button
add_btn = tk.Button(entry_frame, text="➕", font=("Arial", 14), fg="white", bg=PRIMARY_COLOR,
                    relief="flat", padx=10, command=add_task)
add_btn.pack(side="left")
add_btn.bind("<Enter>", on_enter)
add_btn.bind("<Leave>", on_leave)

# ------------------- Task List -------------------
list_frame = tk.Frame(app, bg=LIGHT_BG)
list_frame.pack(pady=10, padx=20, fill="both", expand=True)

task_list = tk.Listbox(list_frame, font=("Arial", 12), width=30, height=12, bg="#fefae0",
                       fg="#333", selectbackground="#cdb4db", relief="flat", bd=2)
task_list.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# ------------------- Buttons -------------------
def edit_task():
    try:
        index = task_list.curselection()[0]  
        new_text = task_input.get()
        if new_text.strip():
            task_list.delete(index)
            task_list.insert(index, "🔹 " + new_text)
            task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Nothing to update.")
    except IndexError:
        messagebox.showwarning("No Selection", "Select a task to edit.")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("No Selection", "Pick a task to delete.")

btn_frame = tk.Frame(app, bg="#f9f7f7")
btn_frame.pack(pady=15)

style_btn = lambda text, color, cmd: tk.Button(
    btn_frame, text=text, font=BTN_FONT, bg=color, fg="white", relief="flat",
    width=12, height=2, command=cmd)

edit_btn = style_btn("✏️ Edit Task", "#ff6d00", edit_task)
edit_btn.grid(row=0, column=0, padx=10)
edit_btn.bind("<Enter>", on_enter)
edit_btn.bind("<Leave>", lambda e: edit_btn.config(bg="#ff6d00"))

delete_btn = style_btn("🗑️ Delete", "#ef233c", delete_task)
delete_btn.grid(row=0, column=1, padx=10)
delete_btn.bind("<Enter>", on_enter)
delete_btn.bind("<Leave>", lambda e: delete_btn.config(bg="#ef233c"))

# ------------------- Footer -------------------
footer_label = tk.Label(app, text="Designed by You 💖", bg="#f9f7f7", fg="#666", font=("Arial", 9))
footer_label.pack(side="bottom", pady=5)

# ------------------- Run Application -------------------
app.mainloop()
