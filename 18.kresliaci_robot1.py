import tkinter as tk
import turtle

c = tk.Canvas(width=400, height=400)
c.pack()

ts = turtle.TurtleScreen(c)
ts.tracer(0)
k = turtle.RawTurtle(ts)

k.lt(90)
k.hideturtle()
def submit():
    command = entry.get().strip().lower().split()
    if len(command) == 2 and command[0] == 'ciara':
        k.fd(int(command[1]))
    elif len(command) == 1:
        if command[0] == 'vlavo':
            k.lt(90)
        elif command[0] == 'vpravo':
            k.rt(90)
    ts.update()
entry = tk.Entry()
entry.pack()
button = tk.Button(command=submit, text="Submit")
button.pack()

c.mainloop()