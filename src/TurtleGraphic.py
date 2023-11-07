import turtle

class TurtleGraph:
    def __init__(self, map_info):
        self.map = map_info
        self.screen = turtle.Screen()
        self.screen.setup(300,300)
        self.t=turtle.Turtle()
        turtle.bgcolor("#E1F1FF")
        self.box_size = 20

        self.draw_map()
        self.draw_turtle()
    
    def draw_map(self):
        self.t.speed(0)

        for y in range(self.map.num_rows):
            for x in range(self.map.num_cols):
                if self.map.map[y][x] == '1':
                    self.draw_shape(x, y, "square", "#654000")
                if self.map.map[y][x] == 'T':
                    self.draw_shape(x, y, "circle", "red")
                if self.map.map[y][x] == 'G':
                    self.draw_shape(x, y, "circle", "green")

        self.t.speed(6)

    def draw_turtle(self):
        self.t.shape("turtle")
        self.t.color("#2A93FA")
        self.t.penup()
        self.t.goto(self.getx(self.map.turtle_pos[1]), self.gety(self.map.turtle_pos[0]))
        self.t.pendown()

    def draw_shape(self, x, y, shape, color):
        # 좌표 재설정
        x = self.getx(x)
        y = self.gety(y)

        # 그리기
        self.t.penup()
        self.t.goto(x, y)
        self.t.shape(shape)
        self.t.color(color)
        self.t.stamp()

    def getx(self, x):
        return (x - self.map.num_cols / 2) * self.box_size
    
    def gety(self, y):
        return -(y - self.map.num_rows / 2) * self.box_size

    def move_turtle(self, x, y, action):
        if action == 0: # UP
            self.t.seth(90)
        if action == 1: # DOWN
            self.t.seth(270)
        if action == 2: # LEFT
            self.t.seth(180)
        if action == 3: # RIGHT
            self.t.seth(0)
        self.t.goto(self.getx(x), self.gety(y))
