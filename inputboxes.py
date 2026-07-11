import customtkinter as ctk
#creating window
app = ctk.CTk() 

def showName():
    n = name.get()
    #print("Helloooo ", n)
    outputLabel.configure(text=n)
    submitButton.configure(width=250)
name = ctk.CTkEntry(
    app,
    placeholder_text="name",
    width = 250
)


submitButton = ctk.CTkButton(
    app,
    text="Submit",
    command = showName,
    width= 100
)

outputLabel = ctk.CTkLabel(
    app,
    text = "Your name will appear here"
)


name.pack()
submitButton.pack()
outputLabel.pack()
app.geometry("400x400")
app.mainloop()