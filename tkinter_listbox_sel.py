from tkinter import *
from tkinter import ttk

main = Tk()
main.title("Multiple Choice Listbox")
main.geometry("+50+150")
frame = ttk.Frame(main, padding=(3, 3, 12, 12))
frame.grid(column=0, row=0, sticky=(N, S, E, W))
valores = StringVar()
valores.set("C C++ Java Python R ASP.NET")
rl = []
lstbox = Listbox(frame, listvariable=valores, selectmode=SINGLE, width=20, height=10)
lstbox.grid(column=0, row=0, columnspan=2)


def callback(event):
    si = lstbox.curselection()
    for i in si:
        entrada = lstbox.get(i)
        rl.append(entrada)
        lstbox.delete(si[0])


def save():
    print("Selected items: \n")
    for i in rl:
        print(i)


lstbox.bind("<<ListboxSelect>>", callback)

btn = ttk.Button(frame, text="Save", command=save)
btn.grid(column=1, row=1)

main.mainloop()
