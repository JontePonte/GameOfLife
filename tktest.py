import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.rows = 50
        self.columns = 50
        self.cellwidth = 15
        self.cellheight = 15

        self.canvas = tk.Canvas(self, width=800, height=800, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        self.rect = {}
        
        for column in range(self.rows):
            for row in range(self.columns):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="black", tags="rect")

        self.redraw(1000)

    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="black")
        for _ in range(10):
            row = random.randint(0,(self.rows-1))
            col = random.randint(0,(self.columns-1))
            item_id = self.rect[row,col]
            self.canvas.itemconfig(item_id, fill="white")
        self.after(delay, lambda: self.redraw(delay))

if __name__ == "__main__":
    app = App()
    app.mainloop()