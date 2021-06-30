import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.rows = 40
        self.columns = 60
        self.cellwidth = 15
        self.cellheight = 15

        self.width = self.columns*self.cellwidth
        self.height = self.rows*self.cellheight

        self.color_foreground = "white"
        self.color_background = "blue"

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        self.rect = {}

        for row in range(self.rows):
            for column in range(self.columns):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill=self.color_background, tags="rect")

        self.redraw(1000)

    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill=self.color_background)
        for _ in range(50):
            row = random.randint(0,(self.rows-1))
            col = random.randint(0,(self.columns-1))
            item_id = self.rect[row,col]
            self.canvas.itemconfig(item_id, fill=self.color_foreground)
        self.after(delay, lambda: self.redraw(delay))

if __name__ == "__main__":
    app = App()
    app.mainloop()