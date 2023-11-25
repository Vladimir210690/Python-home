from tkinter import*

root = Tk()
root.title("window")
canvas = Canvas(root, width = 600, height = 600, bg = "brown", cursor ="pencil")

canvas.create_rectangle(5,5,100,100,fill="white",outline ="blue")

canvas.pack()
root.mainloop()
