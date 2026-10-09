# Contact Form GUI: Name, Mobile Number, Email
# Submit -> saves the entry into contacts.txt as a table
# Read   -> reads contacts.txt and shows it in the window
# Uses tkinter (comes with Python, no install needed)

import os
import re
import tkinter as tk
from tkinter import messagebox

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.txt")
HEADER = f"{'Sr':<5}| {'Name':<25}| {'Mobile':<15}| {'Email':<35}\n"
LINE = "-" * 85 + "\n"


def save_contact(name, mobile, email):
    """Append one row to the table in contacts.txt (creates header if new)."""
    new_file = not os.path.exists(FILE) or os.path.getsize(FILE) == 0
    count = 0
    if not new_file:
        with open(FILE) as f:
            count = len(f.readlines()) - 3  # header + 2 separator lines
    with open(FILE, "a") as f:
        if new_file:
            f.write(LINE + HEADER + LINE)
        f.write(f"{count + 1:<5}| {name:<25}| {mobile:<15}| {email:<35}\n")


def read_contacts():
    if not os.path.exists(FILE):
        return "No contacts saved yet."
    with open(FILE) as f:
        return f.read()


def validate(name, mobile, email):
    if not name:
        return "Name is required"
    if not re.fullmatch(r"\d{10}", mobile):
        return "Mobile number must be 10 digits"
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}", email):
        return "Enter a valid email"
    return None


def on_submit():
    name = name_entry.get().strip()
    mobile = mobile_entry.get().strip()
    email = email_entry.get().strip()
    error = validate(name, mobile, email)
    if error:
        messagebox.showerror("Invalid input", error)
        return
    save_contact(name, mobile, email)
    messagebox.showinfo("Saved", "Contact saved to contacts.txt")
    for e in (name_entry, mobile_entry, email_entry):
        e.delete(0, tk.END)


def on_read():
    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, read_contacts())
    output.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Form")
    root.geometry("720x450")

    form = tk.Frame(root, padx=15, pady=15)
    form.pack(fill="x")

    tk.Label(form, text="Name").grid(row=0, column=0, sticky="w", pady=4)
    name_entry = tk.Entry(form, width=40)
    name_entry.grid(row=0, column=1, pady=4)

    tk.Label(form, text="Mobile Number").grid(row=1, column=0, sticky="w", pady=4)
    mobile_entry = tk.Entry(form, width=40)
    mobile_entry.grid(row=1, column=1, pady=4)

    tk.Label(form, text="Email").grid(row=2, column=0, sticky="w", pady=4)
    email_entry = tk.Entry(form, width=40)
    email_entry.grid(row=2, column=1, pady=4)

    buttons = tk.Frame(form)
    buttons.grid(row=3, column=1, sticky="w", pady=8)
    tk.Button(buttons, text="Submit", width=12, command=on_submit).pack(side="left", padx=(0, 8))
    tk.Button(buttons, text="Read", width=12, command=on_read).pack(side="left")

    output = tk.Text(root, font=("Courier New", 10), state="disabled")
    output.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    root.mainloop()
