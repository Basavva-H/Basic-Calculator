import tkinter as tk
from tkinter import messagebox
import math

# ==================== CORE FUNCTIONS ====================

def click(event):
    text = event.widget.cget("text")
    current = screen.get()

    if text == "=":
        try:
            expression = current.replace("√", "math.sqrt").replace("%", "/100")
            result = eval(expression)
            screen.set(round(result, 6))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression!")
            screen.set("")
    elif text == "C":
        screen.set("")
    elif text == "⌫":
        screen.set(current[:-1])
    elif text == "x²":
        try:
            result = eval(current) ** 2
            screen.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression!")
    elif text == "√":
        try:
            result = math.sqrt(eval(current))
            screen.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression!")
    else:
        screen.set(current + text)


# ==================== MAIN WINDOW ====================

root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("360x520")
root.configure(bg="#121212")
root.resizable(True, True)

# ==================== ENTRY SCREEN ====================

screen = tk.StringVar()
entry = tk.Entry(
    root,
    textvar=screen,
    font=("Consolas", 22),
    justify="right",
    bg="#1e1e1e",
    fg="#00ffc3",
    bd=0,
    insertbackground="#00ffc3",
)
entry.pack(fill=tk.BOTH, ipadx=8, padx=12, pady=20, ipady=10)

# ==================== BUTTON LAYOUT ====================

buttons = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['√', '0', 'x²', '=']
]

button_style = {
    "font": ("Consolas", 18),
    "relief": "flat",
    "bd": 0,
    "width": 4,
    "height": 2,
    "fg": "#ffffff",
    "activebackground": "#2e2e2e",
    "activeforeground": "#00ffc3",
}

# ==================== BUTTON CREATION ====================

def create_button(frame, text, color="#2e2e2e", hover="#3a3a3a"):
    btn = tk.Button(frame, text=text, bg=color, **button_style)
    btn.pack(side="left", expand=True, fill="both", padx=4, pady=4)

    # Hover effects
    def on_enter(e): btn.config(bg=hover)
    def on_leave(e): btn.config(bg=color)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    btn.bind("<Button-1>", click)

# Create all button rows
for row in buttons:
    frame = tk.Frame(root, bg="#121212")
    frame.pack(expand=True, fill="both")
    for text in row:
        if text in ('/', '*', '-', '+'):
            create_button(frame, text, color="#ff9500", hover="#ffb347")
        elif text in ('C', '⌫'):
            create_button(frame, text, color="#ff3b30", hover="#ff6659")
        elif text == '=':
            create_button(frame, text, color="#34c759", hover="#4cd964")
        elif text in ('√', 'x²', '%'):
            create_button(frame, text, color="#0a84ff", hover="#409cff")
        else:
            create_button(frame, text)

# ==================== KEYBOARD BINDINGS ====================

def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.%":
        screen.set(screen.get() + key)
    elif key == "\r":  # Enter
        click(type("event", (object,), {"widget": type("obj", (object,), {"cget": lambda s, x: "="})()})())
    elif key == "\x08":  # Backspace
        screen.set(screen.get()[:-1])

root.bind("<Key>", key_press)

# ==================== RUN ====================
root.mainloop()
