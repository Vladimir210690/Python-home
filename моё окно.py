from tkinter import*

# создание простейшего окна
window = Tk()
window.title("Окно")
window.mainloop()

lbl = Label(window, text="Привет")  
lbl.grid(column=0, row=0)  
