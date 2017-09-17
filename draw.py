#! env bin/python
# codding = utf-8
import turtle


def circle(data):
    lst_data = data.split(' ')
    print(lst_data)
    color = lst_data[-1]
    lst_data = [int(elem) for elem in lst_data[:-1]]
    turtle.pu()
    turtle.setpos(lst_data[0], lst_data[1])
    turtle.pd()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(lst_data[2])
    turtle.end_fill()

    print('in function circle' + str(data))


def rectangle(data):
    lst_data = data.split(' ')
    color = lst_data[-1]
    lst_data = [int(elem) for elem in lst_data[:-1]]
    turtle.pu()
    turtle.setpos(lst_data[0], lst_data[1])
    turtle.pd()

    turtle.color(color)
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(lst_data[0], lst_data[1])
    turtle.pd()
    for i in range(2):
        turtle.forward(lst_data[2]-lst_data[0])
        turtle.right(90)
        turtle.forward(lst_data[3]-lst_data[1])
        turtle.right(90)
    turtle.end_fill()
    print('in function rectangle'+ (data))

