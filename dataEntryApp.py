import customtkinter as c
import csv
app = c.CTk()
app.geometry("400x250")
def appendtoCSV():
    d = data.get()
    with open("text.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow([d])
    result.configure(text="You successfully added inside CSV")
data = c.CTkEntry(
    app,
    placeholder_text="Enter data"
)
submit = c.CTkButton(
    app,
    text="submit",
    command=appendtoCSV
)
result = c.CTkLabel(
    app,
    text=""
)
data.pack()
submit.pack()
result.pack()
app.mainloop()