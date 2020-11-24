import tkinter as tk
from random import randint


def create_dice():
    
    dice = list()
    dice.append(draw_dice('dot0')) 
    dice.append(draw_dice('dot4'))  
    dice.append(draw_dice('dot3', 'dot5'))  
    dice.append(draw_dice('dot2', 'dot4', 'dot6')) 
    dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))  
    dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9')) 
    dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9')) 
    return dice


def draw_dice(*args):
    
    w, h = 250, 250 
    x, y, r = 2, 2, 5
    c = tk.Canvas(root, width=w, height=h, bg='white') 

    
    dots = {
        'dot0': lambda x, y, r: c,
        'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
        'dot2': lambda x, y, r: c.create_oval(x + 16, y, (x + 16) + r, y + r, fill='green'),
        'dot3': lambda x, y, r: c.create_oval(x, y + 8, x + r, (y + 8) + r, fill='red'),
        'dot4': lambda x, y, r: c.create_oval(x + 8, (y + 8), (x + 8) + r, (y + 8) + r, fill='purple'),
        'dot5': lambda x, y, r: c.create_oval(x + 16, (y + 8), (x + 16) + r, (y + 8) + r, fill='brown'),
        'dot6': lambda x, y, r: c.create_oval(x, y + 16, x + r, (y + 16) + r, fill='pink'),
        'dot9': lambda x, y, r: c.create_oval(x + 16, y + 16, (x + 16) + r, (y + 16) + r, fill='grey')
    }

    for arg in args:
        dots.get(arg)(x, y, r) 

    return c


def click():
   
    t = 100 
    stop = randint(13, 18) 
    for x in range(stop):
        dice_index = x % 6 + 1 
        dice_list[dice_index].grid(row=1, column=0, columnspan=3)
        root.update()
        if x == stop - 1:
            
            text.set(str(x % 6 + 1))
            break
        root.after(t, dice_list[dice_index].grid_forget()) 
        t += 25



root = tk.Tk()
root.title("Игра Кости ")


text = tk.StringVar()


text.set("")


result = tk.Label(root, textvariable=text, fg='black')
result.grid(row=3, column=0, columnspan=3)
dice_list = create_dice()


dice_list[0].grid(row=1, column=0, columnspan=3)
button1 = tk.Button(root, text="Бросить кости", command=click)
button1.grid(row=2, column=0, padx=3, pady=3)
button2 = tk.Button(root, text="Покинуть игру", command=root.destroy)
button2.grid(row=2, column=1, pady=3)

menu = tk.Menu(root)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label='Доп. информация', command=info)
menu.add_cascade(label='Файл', menu=filemenu)
menu.add_command(label='Справка', command=f1)
root.config(menu=menu) 

root.mainloop()

