import os
import pandas as pd
from random import choice, shuffle
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

default_mail = "xyz@mail.com"
default_number = 1234567890

# ------------------------- Password Generator ------------------------- #
def generate_password():
    try:
        symbols = ['@', '#', '&', '%', '*']
        numbers = [str(n) for n in range(10)]
        lowercase = [chr(c) for c in range(97, 123)]
        uppercase = [chr(c) for c in range(65, 91)]

        password = []
        password += [choice(uppercase) for _ in range(int(upper_input.get()))]
        password += [choice(lowercase) for _ in range(int(lower_input.get()))]
        password += [choice(numbers) for _ in range(int(num_input.get()))]
        password += [choice(symbols) for _ in range(int(sym_input.get()))]

        shuffle(password)
        final_pass = ''.join(password)
        pass_entry.delete(0, 'end')
        pass_entry.insert(0, final_pass)
        copy_to_clipboard(final_pass)
        update_strength_indicator(final_pass)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields.")

# ------------------------- Clipboard Copy ------------------------- #
def copy_to_clipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()

# ------------------------- Save to CSV ------------------------- #
def save_password():
    if not platform_entry.get() or not user_entry.get() or not pass_entry.get():
        messagebox.showwarning("Missing Info", "Please fill all fields.")
        return
    new_data = {
        "Platform": platform_entry.get(),
        "UserId": user_entry.get(),
        "Password": pass_entry.get()
    }

    if os.path.exists("Passwords.csv"):
        df = pd.read_csv("Passwords.csv")
    else:
        df = pd.DataFrame(columns=["Platform", "UserId", "Password"])

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("Passwords.csv", index=False)

    platform_entry.delete(0, 'end')
    user_entry.delete(0, 'end')
    pass_entry.delete(0, 'end')
    messagebox.showinfo("Saved", "Password saved successfully!")

# ------------------------- Search Platform ------------------------- #
def search_password():
    try:
        df = pd.read_csv("Passwords.csv")
        query = platform_entry.get()
        result = df[df.Platform.str.lower() == query.lower()]
        if not result.empty:
            user = result.iloc[0]['UserId']
            pw = result.iloc[0]['Password']
            messagebox.showinfo("Result", f"User ID: {user}\nPassword: {pw}")
        else:
            messagebox.showwarning("Not Found", "No entry for this platform.")
    except FileNotFoundError:
        messagebox.showwarning("File Missing", "Passwords.csv not found.")

# ------------------------- Helpers ------------------------- #
def fill_default_mail():
    user_entry.delete(0, 'end')
    user_entry.insert(0, default_mail)

def fill_default_phone():
    user_entry.delete(0, 'end')
    user_entry.insert(0, default_number)

def toggle_password():
    if pass_entry.cget('show') == '*':
        pass_entry.config(show='')
        show_btn.config(text='Hide')
    else:
        pass_entry.config(show='*')
        show_btn.config(text='Show')

def update_strength_indicator(pw):
    length = len(pw)
    strength_bar.configure(value=length * 10)
    if length >= 12:
        strength_bar.configure(bootstyle="success-striped")
    elif length >= 8:
        strength_bar.configure(bootstyle="warning-striped")
    else:
        strength_bar.configure(bootstyle="danger-striped")

# ------------------------- UI Setup ------------------------- #
window = ttk.Window(themename="flatly")
window.title("Secure Password Manager")
window.geometry("600x550")
window.resizable(False, False)

# Title
ttk.Label(window, text="🔐 Password Manager", font=("Helvetica", 20, "bold")).pack(pady=10)

form_frame = ttk.Frame(window, padding=10)
form_frame.pack(pady=5)

# Platform
ttk.Label(form_frame, text="Platform:").grid(row=0, column=0, sticky='e', pady=8)
platform_entry = ttk.Entry(form_frame, width=30)
platform_entry.grid(row=0, column=1, padx=5, pady=8)
ttk.Button(form_frame, text="Search", command=search_password, bootstyle=SUCCESS).grid(row=0, column=2, padx=5, pady=8)

# User ID
ttk.Label(form_frame, text="User ID:").grid(row=1, column=0, sticky='e', pady=8)
user_entry = ttk.Entry(form_frame, width=30)
user_entry.grid(row=1, column=1, padx=5, pady=8)
ttk.Button(form_frame, text="Mail", command=fill_default_mail).grid(row=1, column=2, padx=2, pady=8)
ttk.Button(form_frame, text="Phone", command=fill_default_phone).grid(row=1, column=3, padx=2, pady=8)

# Password
ttk.Label(form_frame, text="Password:").grid(row=2, column=0, sticky='e', pady=8)
pass_entry = ttk.Entry(form_frame, width=30, show='*')
pass_entry.grid(row=2, column=1, padx=5, pady=8)
show_btn = ttk.Button(form_frame, text="Show", command=toggle_password)
show_btn.grid(row=2, column=2, padx=5, pady=8)

# Strength bar
ttk.Label(form_frame, text="Strength:").grid(row=3, column=0, sticky='e', pady=8)
strength_bar = ttk.Progressbar(form_frame, length=200, maximum=100)
strength_bar.grid(row=3, column=1, columnspan=2, pady=8)


# Password settings
settings_frame = ttk.Frame(window, padding=10)
settings_frame.pack()

ttk.Label(settings_frame, text="Uppercase:").grid(row=0, column=0)
upper_input = ttk.Entry(settings_frame, width=5)
upper_input.insert(0, '2')
upper_input.grid(row=0, column=1)

ttk.Label(settings_frame, text="Lowercase:").grid(row=0, column=2)
lower_input = ttk.Entry(settings_frame, width=5)
lower_input.insert(0, '2')
lower_input.grid(row=0, column=3)

ttk.Label(settings_frame, text="Numbers:").grid(row=1, column=0)
num_input = ttk.Entry(settings_frame, width=5)
num_input.insert(0, '4')
num_input.grid(row=1, column=1)

ttk.Label(settings_frame, text="Symbols:").grid(row=1, column=2)
sym_input = ttk.Entry(settings_frame, width=5)
sym_input.insert(0, '2')
sym_input.grid(row=1, column=3)

# Buttons
btn_frame = ttk.Frame(window, padding=10)
btn_frame.pack()

ttk.Button(btn_frame, text="Generate Password", command=generate_password, bootstyle=PRIMARY).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(btn_frame, text="Save Password", command=save_password, bootstyle=SUCCESS).grid(row=0, column=1, padx=10, pady=10)

window.mainloop()
