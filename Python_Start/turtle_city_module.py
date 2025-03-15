def draw_figure(turtle, side_length, color, count):  
    turtle.fillcolor(color)  
    turtle.begin_fill()  
    for _ in range(count):  
        turtle.forward(side_length)  
        turtle.left(360/count)  
    turtle.end_fill()  

def change_position(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_meria(turtle, x, y):
    # Рисуем здание
    change_position(turtle, x, y)

    draw_figure(turtle, 50, "gray", 4)
    change_position(turtle, x, y + 50)
    draw_figure(turtle, 50, "red", 3)



def draw_neboscreb(turtle, x, y, count_floors=4):
    # Рисуем небоскреб
    for _ in range(count_floors):
        change_position(turtle, x, y)
        # Отрисовка этажа
        draw_figure(turtle, 40, 'black', 4)

        # Отрисовка окна
        change_position(turtle, x + 10, y + 10)
        draw_figure(turtle, 20, 'blue', 4)

        # Переход на следующий этаж
        y += 40


def draw_background(turtle):
    # Отрисовка фона

    # Отрисовка неба
    change_position(turtle,-200, 0)
    draw_figure(turtle, 400, 'blue', 4)

    # Отрисовка земли
    change_position(turtle,-200, -400)
    draw_figure(turtle, 400, 'green', 4)




# Импорт черепашки
import turtle
pen = turtle.Turtle()
pen.speed(10)


draw_background(pen)
draw_meria(pen, 20, -10)
draw_neboscreb(pen,100, -10)


