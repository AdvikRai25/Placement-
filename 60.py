import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_entry.get()

    if not name or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    with open("registrations.txt", "a") as f:
        f.write(f"{name},{email},{password}\n")

    messagebox.showinfo("Success", "Registration Successful!")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")
root.config(bg="#e6f2ff")


tk.Label(root, text="Name", bg="#e6f2ff").place(x=50, y=30)
name_entry = tk.Entry(root, width=30)
name_entry.place(x=150, y=30)

tk.Label(root, text="Email", bg="#e6f2ff").place(x=50, y=70)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=150, y=70)

tk.Label(root, text="Password", bg="#e6f2ff").place(x=50, y=110)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.place(x=150, y=110)

tk.Label(root, text="Confirm Password", bg="#e6f2ff").place(x=50, y=150)
confirm_entry = tk.Entry(root, show="*", width=30)
confirm_entry.place(x=150, y=150)


tk.Button(root, text="Register", command=register, bg="blue", fg="white", width=15).place(x=150, y=200)

root.mainloop()
