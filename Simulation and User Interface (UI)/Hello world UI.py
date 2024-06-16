## Program 1
import tkinter as tk

window = tk.Tk(className='Program 1 part 1')
window.geometry('400x400')
window.configure(bg='white')
label = tk.Label(window, text='Hello world', bg='white', fg='#000064')
label.place(x=130, y=200)
label.configure(font=('Arial', 24))
window.mainloop()

# Tarea 1 part 2
import tkinter as tk
import time

window = tk.Tk()
window.title('Program 1 part 2')
window.geometry('400x400')
window.configure(bg='white')
label = tk.Label(window, text='Hello world', bg='white', font=('Arial', 24), fg='#000064')
t1 = time.time()
for ix in range(10):
    label.place(x=220 - ((ix + 1) * 20), y=200)
    window.update()
    time.sleep(1)
t2 = time.time()
print(t2 - t1)
window.mainloop()
