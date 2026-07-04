import customtkinter as ctk
ctk.set_appearance_mode("Dark") #changes visual theme of application, can be either, dark, light or system
ctk.set_default_color_theme("blue") #built in themes : "dark blue","blue","green"

#creating window
app = ctk.CTk() 
#title
app.title("My first app")
#window size
app.geometry("800x600") #without this it would be the default size

app.mainloop()