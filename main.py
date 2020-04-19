from turtle import *
import time
import random
import threading
import sys

sys.setrecursionlimit(999999)  # set the maximum depth as 1500

# Initialize
snake_dir = 'u'
snake_list = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3)]
# Create turtle object
snake = Turtle()
food = Turtle()
mons = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
mons_pos = [-5, -5]
dir_mons = 'u'
mons_stamp = 0
over_control = False
n = 0


def startUI():
    global n
    hideturtle()
    penup()
    goto(-200, 100)
    write("Welcome to Boke's version of Snake\n\n"
          "You are going to use the 4 arrow keys to move the snake\n"
          "around the screen, trying to consume all the food items\n"
          "before the monster catches you...\n\n"
          "press 'Space' to start the game, have fun!!", font=["Arial Bold", 15])
    screen.onkey(main, "space")
    screen.listen()
    screen.mainloop()


def snakeDir():
    return snake_dir


# Verified
def convertCod(snake_list):
    cod_list = []
    for cod in snake_list:
        x = cod[0]
        y = cod[1]
        x_cod = x * 20
        y_cod = y * 20
        new_cod = (x_cod, y_cod)
        cod_list.append(new_cod)

    return cod_list


def createFood():
    global food_list
    food_list = {}
    tracer(False)
    for i in list(range(1, 10)):
        cod_list = list(range(-10, 11))
        x_fd = random.choice(cod_list) * 20
        y_fd = random.choice(cod_list) * 20
        cod_pair = (x_fd, y_fd)
        food_list[i] = cod_pair
        food.penup()
        food.goto(x_fd - 3, y_fd - 12)
        food.pendown()
        opt = str(i)
        # opt=str(i)+' '+str(x_fd)+' '+str(y_fd)
        food.write(opt, font=["Arial Bold", 20])
    update()


# turn right
def right():
    global snake_dir
    if snake_dir == 'u':
        snake_dir = 'r'
        # print('right')
        # print(snake_dir)
    elif snake_dir == 'd':
        snake_dir = 'r'
        # print('right')
        # print(snake_dir)


# turn left
def left():
    global snake_dir
    if snake_dir == 'u':
        snake_dir = 'l'
        # print('left')
        # print(snake_dir)
    elif snake_dir == 'd':
        snake_dir = 'l'
        # print('left')
        # print(snake_dir)


# turn left
def up():
    global snake_dir
    if snake_dir == 'l':
        snake_dir = 'u'
        # print('up')
        # print(snake_dir)
    elif snake_dir == 'r':
        snake_dir = 'u'
        # print('up')
        # print(snake_dir)


# turn left
def down():
    global snake_dir
    if snake_dir == 'l':
        snake_dir = 'd'
        # print('down')
        # print(snake_dir)
    elif snake_dir == 'r':
        snake_dir = 'd'
        # print('down')
        # print(snake_dir)


def drawWhiteSquare():
    global food
    hideturtle()
    food.pencolor('white')
    food.begin_fill()
    food.fillcolor('white')
    for x in range(4):
        food.forward(30)
        food.right(90)
    food.end_fill()


def drawRedSquare():
    global stamp_list
    screen.tracer(False)
    snake.pencolor("blue")
    snake.fillcolor("red")
    snake.shape("square")
    snake.shapesize(1, 1, 0)
    back = snake.stamp()
    stamp_list.append(back)

    # print('Position of turtle '+str(snake.pos()))

    a = snake.pos()

    if (a[0] <= -240) and (a[1] >= 240) and (snake_dir == 'u'):
        # print('nw Vertex')
        right()
    elif (a[0] <= -240) and (a[1] >= 240) and (snake_dir == 'l'):
        # print('nw Vertex')
        down()
    elif (a[0] <= -240) and (a[1] <= -240) and (snake_dir == 'd'):
        # print('sw Vertex')
        right()
    elif (a[0] <= -240) and (a[1] >= 240) and (snake_dir == 'l'):
        # print('sw Vertex')
        up()
    elif (a[0] >= 240) and (a[1] <= -240) and (snake_dir == 'r'):
        # print('se Vertex')
        up()
    elif (a[0] >= 240) and (a[1] <= -240) and (snake_dir == 'l'):
        # print('se Vertex')
        left()
    elif (a[1] >= 240) and (snake_dir == 'u'):
        # print('Top')
        left()
    elif (a[0] <= -240) and (snake_dir == 'l'):
        # print('Left')
        down()
    elif (a[0] >= 240) and (snake_dir == 'r'):
        # print('Right')
        up()
    elif (a[1] <= -240) and (snake_dir == 'd'):
        # print('Bottom')
        right()


def drawSquare():
    global stamp_list
    tracer(False)
    snake.pencolor("red")
    snake.fillcolor("blue")
    snake.shape("square")
    snake.shapesize(1, 1, 0)
    back = snake.stamp()
    stamp_list.append(back)


def drawSnake(cod_list):
    cod_h = cod_list[0]
    x = cod_h[0]
    y = cod_h[1]
    snake.penup()
    snake.goto(x, y)
    snake.pendown()
    drawRedSquare()
    # print('OK')
    idcard = 2
    length = len(cod_list)
    while idcard <= length:
        idi = idcard - 1
        cod_xy = cod_list[idi]
        x = cod_xy[0]
        y = cod_xy[1]
        snake.penup()
        snake.goto(x, y)
        snake.pendown()
        drawSquare()
        idcard = idcard + 1
        # print('Ordinary square OK')


# Verified
def newSnakeList(snake_list):
    # Remove the last box
    length = len(snake_list)
    del snake_list[length - 1]
    new_length = length - 1
    new_snake_list = []
    # Add a new box at the head
    if snakeDir() == 'l':
        # print(snakeDir())
        cod = snake_list[0]
        x = cod[0]
        y = cod[1]
        x = x - 1
        new_cod = (x, y)
        new_snake_list.append(new_cod)
    elif snakeDir() == 'r':
        # print(snakeDir())
        cod = snake_list[0]
        x = cod[0]
        y = cod[1]
        x = x + 1
        new_cod = (x, y)
        new_snake_list.append(new_cod)
    elif snakeDir() == 'u':
        # print(snakeDir())
        cod = snake_list[0]
        x = cod[0]
        y = cod[1]
        y = y + 1
        new_cod = (x, y)
        new_snake_list.append(new_cod)
    elif snakeDir() == 'd':
        # print(snakeDir())
        cod = snake_list[0]
        x = cod[0]
        y = cod[1]
        y = y - 1
        new_cod = (x, y)
        new_snake_list.append(new_cod)
    for remainder in snake_list:
        new_snake_list.append(remainder)
    return new_snake_list


def clearstamp_my(pre_length):
    global stamp_list
    global n
    count = 1
    while count <= pre_length:
        count_index = count - 1
        id_stamp = stamp_list[count_index]
        snake.clearstamp(id_stamp)
        del stamp_list[count_index]
        count = count + 1
    n = n + 1


def snakeMove():
    global snake_timer

    global stamp_list
    global n
    global snake_list
    global cod_list
    tracer(False)
    if n == 0:
        clearscreen()
        createFood()
        stamp_list = []
    # pre_length = len(snake_list)
    snake.clearstamps()
    snake.hideturtle()
    snake_list = newSnakeList(snake_list)
    cod_list = convertCod(snake_list)
    drawSnake(cod_list)
    n = n + 1
    update()
    ontimer(mainMove, 500)
    # snake_timer = threading.Timer(0.5, mainMove)
    # snake_timer.start()

    # print('How much time has passed '+str(n))

    screen.onkey(right, "Right")
    screen.onkey(left, "Left")
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    # screen.onkey(pause, "space")
    # ontimer(mainMove, 200)
    # 100ms后继续调用
    screen.listen()


# Verified
def appendSeg(snake_list):
    length_app = len(snake_list)
    index_max = length_app - 1
    last_1 = snake_list[index_max]
    last_2 = snake_list[index_max - 1]
    x_last_1 = last_1[0]
    x_last_2 = last_2[0]
    y_last_1 = last_1[1]
    y_last_2 = last_2[1]
    if (x_last_1 - x_last_2 == 1):  # have to append rightward
        x_new = x_last_1 + 1
        y_new = y_last_1
        pair_new = (x_new, y_new)
        snake_list.append(pair_new)
    elif (x_last_1 - x_last_2 == -1):  # have to append leftward
        x_new = x_last_1 - 1
        y_new = y_last_1
        pair_new = (x_new, y_new)
        snake_list.append(pair_new)
    elif (y_last_1 - y_last_2 == 1):  # have to append upward
        x_new = x_last_1
        y_new = y_last_1 + 1
        pair_new = (x_new, y_new)
        snake_list.append(pair_new)
    elif (y_last_1 - y_last_2 == -1):  # have to append downward
        x_new = x_last_1
        y_new = y_last_1 - 1
        pair_new = (x_new, y_new)
        snake_list.append(pair_new)
    # print('Append successfully!!!!')
    # time.sleep(2)
    return snake_list


def singleMoveTail():
    global stamp_list
    global n
    global snake_list
    global cod_list
    tracer(False)
    snake.clearstamps()
    stamp_list = []
    snake.hideturtle()
    snake_list = newSnakeList(snake_list)  # Has renewed!
    # append a new tail segment
    snake_list = appendSeg(snake_list)
    # end
    cod_list = convertCod(snake_list)
    drawSnake(cod_list)
    update()
    n = n + 1
    # print('How much time has passed '+str(n))
    screen.onkey(right, "Right")
    screen.onkey(left, "Left")
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    # screen.onkey(pause, "space")

    screen.listen()


def tailExt(number):
    global food
    global food_list
    # print('eating food')
    card = 1
    while card <= number:
        singleMoveTail()
        # print('Move is OK')
        time.sleep(0.5)
        # ontimer(singleMoveTail, 500)
        card = card + 1
    # delete food
    cod_food = food_list[number]
    x_food = cod_food[0]
    y_food = cod_food[1]
    del food_list[number]
    # print(x_food)
    # print(y_food)
    food.penup()
    food.goto(x_food - 10, y_food + 10)
    food.pendown()
    drawWhiteSquare()
    mainMove()


def judgeInRange():
    global post_food
    # global snake_list
    # global food_list
    head_cod = snake_list[0]
    # print('Food item '+str(list(food_list.keys())))
    for food_index in list(food_list.keys()):

        food_cod = food_list[food_index]
        # print('Food coordinate '+str(food_cod))

        x_cod_food = food_cod[0]
        y_cod_food = food_cod[1]
        x_cod_head = head_cod[0] * 20
        y_cod_head = head_cod[1] * 20
        delta_x = x_cod_food - int(x_cod_head)
        delta_y = y_cod_food - int(y_cod_head)
        abs_x = abs(delta_x)
        abs_y = abs(delta_y)

        # print('delta x '+str(abs_x))
        # print('delta y '+str(abs_y))
        # time.sleep(2)
        # print('Food list is '+str(food_list))
        # print('Snake head '+str(cod_list[0]))
        # time.sleep(2)
        # time.sleep(1.5)
        if (abs_x <= 10) and (abs_y <= 10):
            # print('the snake should have caught food')
            # time.sleep(2)
            post_food = food_index
            # print('How many units will the snake tail extend by? '+str(post_food))
            # time.sleep(2)
            # del food_list[food_index]
            ##print('Food deleted')
            # print('Food eaten!!!')
            return True
    return False


def drawMons():
    global mons_stamp
    tracer(False)
    mons.clearstamp(mons_stamp)
    # print('Previous monster cleared!')
    mons.pencolor("green")
    mons.fillcolor("green")
    mons.shape("square")
    mons.shapesize(1, 1, 0)
    mons_stamp = mons.stamp()
    # print('Get stamp id of monster')
    update()
    # print('Draw monster successfully!')


def chaseArith():
    global snake_list
    # the head of the snake
    head_pos = snake_list[0]
    x_head = head_pos[0]
    y_head = head_pos[1]

    # the monster
    x_mons = mons_pos[0]
    y_mons = mons_pos[1]

    adelta_x = x_head - x_mons
    adelta_y = y_head - y_mons

    if adelta_x == 0:  # Consider the gradient is inifinity
        if adelta_y > 0:
            dir_mons = 'u'
        elif adelta_y < 0:
            dir_mons = 'd'
    else:
        gradient = adelta_y / adelta_x
        if gradient >= 3:
            if adelta_x > 0:
                dir_mons = 'u'
            elif adelta_x < 0:
                dir_mons = 'd'
        elif (gradient < 3) and (gradient >= 0.2):
            if adelta_x > 0:
                dir_mons = 'ne'
            elif adelta_x < 0:
                dir_mons = 'sw'
        elif (gradient < 0.2) and (gradient > 0):
            if adelta_x < 0:
                dir_mons = 'l'
            elif adelta_x > 0:
                dir_mons = 'r'
        elif gradient == 0:
            if adelta_x > 0:
                dir_mons = 'r'
            elif adelta_x < 0:
                dir_mons = 'l'
        elif (gradient > -0.2) and (gradient < 0):
            if adelta_x < 0:
                dir_mons = 'l'
            elif adelta_x > 0:
                dir_mons = 'r'
        elif (gradient > -3) and (gradient <= -0.2):
            if adelta_x > 0:
                dir_mons = 'se'
            elif adelta_x < 0:
                dir_mons = 'nw'
        elif (gradient <= -3):
            if adelta_x > 0:
                dir_mons = 'd'
            elif adelta_x < 0:
                dir_mons = 'u'
    return dir_mons


def chaseExec():
    operation = chaseArith()
    print('Monster will turn -- ' + operation)
    global mons_pos
    if len(operation) == 1:
        if operation == 'u':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            y_mons = y_mons + 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is '+str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
        elif operation == 'd':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            y_mons = y_mons - 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
        elif operation == 'l':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            x_mons = x_mons - 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
        elif operation == 'r':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            x_mons = x_mons + 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
    elif len(operation) == 2:
        if operation == 'nw':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            y_mons = y_mons + 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
            time.sleep(0.5)
            # Then,
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            x_mons = x_mons - 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
        elif operation == 'se':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            y_mons = y_mons - 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons, y_mons)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
            time.sleep(0.5)
            # Then,
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            x_mons = x_mons + 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
        elif operation == 'sw':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            y_mons = y_mons - 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
            time.sleep(0.5)
            # Then,
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            x_mons = x_mons - 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
        elif operation == 'ne':
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            y_mons = y_mons + 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
            time.sleep(0.5)
            # Then,
            tracer(False)
            x_mons = mons_pos[0]
            y_mons = mons_pos[1]
            x_mons = x_mons + 1
            mons_pos = [x_mons, y_mons]
            # print('Monster renewed')
            # print('Monster coordinate is ' + str(mons_pos))
            mons.penup()
            mons.goto(x_mons * 20, y_mons * 20)
            mons.pendown()
            drawMons()
            # print('Exec is OK')
            update()
    else:
        print(operation)
        print('BUG!!!')
        return
    ontimer(monsMove, 500)


def monsMove():
    global over_control
    if over_control == False:
        chaseExec()
        # print('Game is Over!')


def mainMove():
    global n
    global food_list
    global over_control

    # print('mainMove invoked')
    if n == 0:
        snakeMove()
    else:
        if food_list == {}:
            over_control = True
            snake.penup()
            snake.goto(-150, 0)
            snake.write("CONGRATULATIONS!", font=["Arial Bold", 70])
            snake.pendown()
            ontimer(1000)
        if judgeInRange() == True:
            # print('Judge is True')
            # time.sleep(2)
            tailExt(post_food)
            # print('Main is OK')
            # time.sleep(2)
        else:
            snakeMove()


def main():
    # Create threads
    thread_snake = threading.Thread(target=mainMove)
    thread_monster = threading.Thread(target=monsMove)
    # Start threads
    thread_snake.start()
    thread_monster.start()
    print('Main thread has ended!')


startUI()


