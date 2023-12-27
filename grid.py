import pygame

CELLSIZE = 50

class Cell():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.CELLSIZE = CELLSIZE

        self.pos = (self.column * self.CELLSIZE, self.row * self.CELLSIZE)

        self.state = 'D' 

    def draw(self, surface):
        if self.state == "D":
            pygame.draw.rect(surface, 'black', pygame.Rect(self.pos[0], self.pos[1], CELLSIZE-5, CELLSIZE-5))
        if self.state == "A":
            pygame.draw.rect(surface, 'white', pygame.Rect(self.pos[0], self.pos[1], CELLSIZE -5 , CELLSIZE-5))

    def matchCell(self, row, column):
        if row == self.row and column == self.column:
            return True
        else:
            return False

grid =[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]

WIDTH = len(grid[1]) * CELLSIZE
HEIGHT = len(grid) * CELLSIZE

class Grid():
    def __init__(self):
        self.grid = grid
        self.cellgrid = []

        self.initializeGrid()

    def initializeGrid(self):

        row_num = 0
        for row in self.grid:
            col_num = 0
            for col in row:
                if col == 0:
                    cell = Cell(row_num, col_num)
                    cell.state = 'D'
                    self.cellgrid.append(cell)
                if col == 1:
                    cell = Cell(row_num, col_num)
                    cell.state = 'A'
                    self.cellgrid.append(cell)
                col_num += 1
            row_num += 1
    def drawGrid(self, surface):
        for cell in self.cellgrid:
            cell.draw(surface)

    def yeildNeighbors(self, cell):
        alive_count = 0
        for i in range(len(self.cellgrid)):
            neighCell = self.cellgrid[i]
            if neighCell.matchCell(cell.row-1, cell.column-1):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row-1, cell.column):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row-1, cell.column+1):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row, cell.column-1):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row, cell.column+1):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row+1, cell.column-1):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row+1, cell.column):
                if neighCell.state == 'A':
                    alive_count += 1
            elif neighCell.matchCell(cell.row+1, cell.column+1):
                if neighCell.state == 'A':
                    alive_count += 1

        if cell.state == 'A':
            if alive_count <= 1:
                cell.state = 'D' 
            elif alive_count == 2 or alive_count ==3:
                cell.state = 'A'
            elif alive_count >= 3:
                cell.state = 'D'
        elif cell.state == 'D':
            if alive_count == 3:
                cell.state = 'A'

        print(alive_count)
        return cell.state
    
    def generation(self):
        for cell in self.cellgrid:
            self.yeildNeighbors(cell)
