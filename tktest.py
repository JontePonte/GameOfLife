import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.rows = 40
        self.columns = 60
        self.cellwidth = 15
        self.cellheight = 15

        self.color_foreground = "white"
        self.color_background = "black"
        self.delay = 1000
    
        self.width = self.columns*self.cellwidth
        self.height = self.rows*self.cellheight

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        self.rect = {}
        self.cells = []

        self.create_rows_cells()
        self.run_game_of_life()


    def create_rows_cells(self):
        for row in range(self.rows):
            row_of_cells = []
            for column in range(self.columns):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                row_of_cells.append(self.Cell(row,column,random.randint(0,1)))

                cell_color = self.color_background
                if row_of_cells[column].state_current:
                    cell_color = self.color_foreground

                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill=cell_color, tags="rect")
            self.cells.append(row_of_cells)


    def run_game_of_life(self):
        self.canvas.itemconfig("rect", fill=self.color_background)
        
        for row in range(self.rows):
            for column in range(self.columns):
                item_id = self.rect[row,column]

                cell_color = self.color_background
                if self.cells[row][column].state_next:
                    cell_color = self.color_foreground
                if random.randint(0,1) == 1:
                    cell_color = self.color_foreground

                self.canvas.itemconfig(item_id, fill=cell_color)
        
        self.after(self.delay, lambda: self.run_game_of_life())


    class Cell:
        """ Class for cells """
        def __init__(self,row_id,col_id,state_current):
            self.row_id = row_id
            self.col_id = col_id
            self.state_current = state_current
            self.state_next = 0


if __name__ == "__main__":
    app = App()
    app.mainloop()