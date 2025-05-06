import tkinter as tk
from tkinter import messagebox

# Menyimpan data register sementara
user_data = {"username": "", "password": ""}

def go_to_login():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        user_data["username"] = username
        user_data["password"] = password
        show_register_success()
    else:
        show_error("Register Gagal! Harap isi semua data.", show_register)

def login_action():
    username = entry_username.get()
    password = entry_password.get()
    if username == user_data["username"] and password == user_data["password"]:
        show_login_success()
    else:
        show_error("Login Gagal! Username atau password salah.", show_login)

def show_register():
    clear_widgets()
    window.configure(bg='#ffc0cb')  # pink
    tk.Label(window, text="Register", bg='#ffc0cb', font=('Times New Roman', 16)).pack(pady=10)

    global entry_username, entry_password
    entry_username = tk.Entry(window, width=30, font=('Times New Roman', 12))
    entry_username.pack(pady=5)
    entry_username.insert(0, "Username")

    entry_password = tk.Entry(window, width=30, show="*", font=('Times New Roman', 12))
    entry_password.pack(pady=5)
    entry_password.insert(0, "Password")

    tk.Button(window, text="Register", command=go_to_login, bg="white", font=('Times New Roman', 12)).pack(pady=10)

def show_register_success():
    clear_widgets()
    window.configure(bg='white')
    tk.Label(window, text="Berhasil Register!", bg='white', fg='green', font=('Times New Roman', 16)).pack(pady=30)
    tk.Button(window, text="Lanjut ke Login", command=show_login, bg='#006400', fg='white', font=('Times New Roman', 12)).pack(pady=10)

def show_login():
    clear_widgets()
    window.configure(bg='#006400')  # dark green
    tk.Label(window, text="Login", bg='#006400', fg='white', font=('Times New Roman', 16, 'italic')).pack(pady=10)

    global entry_username, entry_password
    entry_username = tk.Entry(window, width=30, font=('Times New Roman', 12))
    entry_username.pack(pady=5)
    entry_username.insert(0, "Username")

    entry_password = tk.Entry(window, width=30, show="*", font=('Times New Roman', 12))
    entry_password.pack(pady=5)
    entry_password.insert(0, "Password")

    tk.Button(window, text="Login", command=login_action, bg="white", font=('Times New Roman', 12, 'italic')).pack(pady=10)

def show_login_success():
    clear_widgets()
    window.configure(bg='white')
    tk.Label(window, text="Login Berhasil!", bg='white', fg='green', font=('Times New Roman', 16, 'bold')).pack(pady=40)

def show_error(message, back_action):
    clear_widgets()
    window.configure(bg='red')
    tk.Label(window, text=message, bg='red', fg='white', font=('Times New Roman', 14, 'bold')).pack(pady=30)
    tk.Button(window, text="Kembali", command=back_action, bg='white', font=('Times New Roman', 12)).pack(pady=10)

def clear_widgets():
    for widget in window.winfo_children():
        widget.destroy()

# Main window setup
window = tk.Tk()
window.title("Register/Login UI")
window.geometry("300x250")

show_register()

window.mainloop()
