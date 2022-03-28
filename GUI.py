import tkinter as tk



    
    
root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
def hello():
    T.insert(tk.END,"hello world")
str2=T.insert(tk.END,"hello")
print(str2)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="submit", 
                   fg="red",
                   command=hello)
button.pack()
tk.mainloop()
