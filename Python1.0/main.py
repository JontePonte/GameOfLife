import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.rows = 30
        self.columns = 30
        self.color_foreground = "white"
        self.color_background = "black"
        self.delay = 10
        self.start_white_share = 0.02

        self.cellwidth = 15
        self.cellheight = 15
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

                color_state = 0
                if random.random() < self.start_white_share:
                    color_state = 1
                row_of_cells.append(self.Cell(row,column,color_state))

                cell_color = self.color_background
                if row_of_cells[column].state_current:
                    cell_color = self.color_foreground

                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill=cell_color, tags="rect")
            self.cells.append(row_of_cells)


    def calculate_next_states(self):
        for row in range(self.rows):
            for column in range(self.columns):
                r = self.rows
                c = self.columns                
                neighbors = 0
                neighbors += self.cells[(row-1+r)%r][(column-1+c)%c].state_current
                neighbors += self.cells[(row-1+r)%r][(column+c)%c].state_current
                neighbors += self.cells[(row-1+r)%r][(column+1+c)%c].state_current
                neighbors += self.cells[row][(column-1+c)%c].state_current
                neighbors += self.cells[row][(column+1+c)%c].state_current
                neighbors += self.cells[(row+1+r)%r][(column-1+c)%c].state_current
                neighbors += self.cells[(row+1+r)%r][(column+c)%c].state_current
                neighbors += self.cells[(row+1+r)%r][(column+1+c)%c].state_current

                if self.cells[row][column].state_current == 1 and neighbors < 2:
                    self.cells[row][column].state_next = 0
                if self.cells[row][column].state_current == 1 and neighbors > 3:
                    self.cells[row][column].state_next = 0
                if self.cells[row][column].state_current == 0 and neighbors == 2:
                    self.cells[row][column].state_next = 1
                if self.cells[row][column].state_current == 0 and neighbors == 3:
                    self.cells[row][column].state_next = 1


    def run_game_of_life(self):
        self.canvas.itemconfig("rect", fill=self.color_background)
        
        for row in range(self.rows):
            for column in range(self.columns):
                item_id = self.rect[row,column]

                self.calculate_next_states()

                cell_color = self.color_background
                if self.cells[row][column].state_next:
                    cell_color = self.color_foreground

                self.canvas.itemconfig(item_id, fill=cell_color)
        
        # The current state of the next round is the next state of the current
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column].state_current = self.cells[row][column].state_next

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