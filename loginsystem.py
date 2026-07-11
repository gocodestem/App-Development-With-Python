import customtkinter as ctk
from PIL import Image
#creating the window
app = ctk.CTk()
app.title("Carlos's System. ")
app.geometry("300x250")
storedUser = "testUser"
storedPass = "testPass"



def validate():
    username = username_entry.get()
    password = password_entry.get()

    if username == storedUser and password == storedPass:
        result.configure(text="Access Granted")
    else:
        result.configure(text="Access Denied")

def showPass():
    password_entry.configure(
        show=""
        )
    print("Show pass is working")
title= ctk.CTkLabel(
    app,
    text = "Login",
    font=("Arial",20)
)
username_entry = ctk.CTkEntry(
    app,
    placeholder_text="username"
)

password_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter password",
    show = "*"
)
showpass = ctk.CTkButton(
    app,
    text = "show password",
    command = showPass
)
submit_btn = ctk.CTkButton(
    app,
    text = "submit",
    command = validate
)
result = ctk.CTkLabel(
    app,
    text = ""
)

title.pack()
username_entry.pack()
password_entry.pack()
showpass.pack()
submit_btn.pack()
result.pack()
app.mainloop()