from maze import Maze
import turtle

class TurtleMaze(Maze):
    def __init__(self, file_path, square_size):
        Maze.__init__(self, file_path)

        self.__square_size = square_size

        self.__game_line = 0
        self.__game_column = 0
        self.__game_x = 0
        self.__game_y = 0
        self.__visited_cases = list()

        self.__width = self.__square_size * Maze.getWidth(self)
        self.__height = self.__square_size * Maze.getHeight(self)

        turtle.title('Maze')
        turtle.speed('normal')
        turtle.shape('turtle')
        turtle.setup(self.__width + 50, self.__height + 50)

        self.drawMaze()

    def drawSquare(self, draw_color, fill=0, fill_color='black'):
        turtle.pencolor(draw_color)

        if fill == 1:
            turtle.fillcolor(fill_color)
            turtle.begin_fill()

        turtle.down()

        for i in range(4):
            turtle.forward(self.__square_size)
            turtle.right(90)

        turtle.up()

        if fill == 1:
            turtle.end_fill()

    def drawMaze(self):
        turtle.tracer(0, 0)

        start_draw_x = - self.__width / 2
        start_draw_y = self.__height / 2

        turtle.up()

        for line in range(Maze.getWidth(self)):
            turtle.goto(start_draw_x, start_draw_y)

            for column in range(Maze.getHeight(self)):
                value = Maze.getCell(self, line, column)

                if int(value) == 0:
                    self.drawSquare('black', 1, 'black')

                if int(value) == 1:
                    self.drawSquare('red', 1, 'red')
                    self.__game_line = line
                    self.__game_column = column
                    self.__game_x = start_draw_x + column * self.__square_size + self.__square_size / 2
                    self.__game_y = start_draw_y - self.__square_size / 2

                if int(value) == 3:
                    self.drawSquare('green', 1, 'green')

                turtle.forward(self.__square_size)

            start_draw_y -= self.__square_size

        turtle.update()

    def nextCase(self):
        if self.getCell(self.__game_line, self.__game_column + 1) >= 2:
            self.__visited_cases.append(
                {"l": self.__game_line, "c": self.__game_column, "x": self.__game_x, "y": self.__game_y})

            self.__game_column += 1
            self.__game_x += self.__square_size

        elif self.getCell(self.__game_line + 1, self.__game_column) >= 2:
            self.__visited_cases.append(
                {"l": self.__game_line, "c": self.__game_column, "x": self.__game_x, "y": self.__game_y})

            self.__game_line += 1
            self.__game_y -= self.__square_size

        elif self.getCell(self.__game_line, self.__game_column - 1) >= 2:
            self.__visited_cases.append(
                {"l": self.__game_line, "c": self.__game_column, "x": self.__game_x, "y": self.__game_y})

            self.__game_column -= 1
            self.__game_x -= self.__square_size

        elif self.getCell(self.__game_line - 1, self.__game_column) >= 2:
            self.__visited_cases.append(
                {"l": self.__game_line, "c": self.__game_column, "x": self.__game_x, "y": self.__game_y})

            self.__game_line -= 1
            self.__game_y += self.__square_size

        else:
            return False

        turtle.pencolor('green')
        turtle.goto(self.__game_x, self.__game_y)

        return True

    def doMaze(self):
        turtle.tracer(1, 10)
        turtle.speed('slowest')
        turtle.pencolor('green')

        turtle.goto(self.__game_x, self.__game_y)
        turtle.down()

        while not self.getCell(self.__game_line, self.__game_column) == 3:
            self.setCell(self.__game_line, self.__game_column, -1)

            while not self.nextCase():
                previous_case = self.__visited_cases.pop()

                self.__game_line = previous_case["l"]
                self.__game_column = previous_case["c"]
                self.__game_x = previous_case["x"]
                self.__game_y = previous_case["y"]

                turtle.pencolor('red')
                turtle.goto(self.__game_x, self.__game_y)

        print("Completed")

    @staticmethod
    def leaveMaze():
        turtle.exitonclick()
