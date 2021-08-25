import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

# check if the save file exists
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#  function to add the app to the list
def addApp():
    # clean the text box
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="C:\Program Files", title="Select File",
                                            filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# funtion to run the app
def runApps():
    for app in apps:
        os.startfile(app)


# set the window size and color
convas = tk.Canvas(root, height=700, width=700, bg="#263D42")
convas.pack()

# set the frame inside the window

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# set the open file button

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42" ,command=addApp)
openFile.pack()

# set run app button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# read from the save.txt file
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# intialize the window
root.mainloop()

# write to the save.txt file
with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")