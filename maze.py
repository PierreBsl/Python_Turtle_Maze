from file import File

class Maze:
    def __init__(self, file_path):
        data = File.getFile(file_path)
        self.__maze_grid = list()

        for line in data:
            self.__maze_grid.append(list(line))
        print(self.__maze_grid)

    def setCell(self, line, column, value):
        self.__maze_grid[line][column] = value

    def getCell(self, line, column):
        if line < 0 or line >= self.getHeight() or column < 0 or column >= self.getWidth():
            return 0

        return int(self.__maze_grid[line][column])

    def getHeight(self):
        return len(self.__maze_grid)

    def getWidth(self):
        return len(self.__maze_grid[0])

    def getGrid(self):
        return self.__maze_grid
