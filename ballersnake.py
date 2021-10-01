#!/usr/bin/python
import curses
import time
import random
# This starts the screen and all the colors
screen = curses.initscr()
curses.start_color()
curses.curs_set(False)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)
screen.keypad(1)
dims = screen.getmaxyx()

# fail cheat code atm
# def cheat():
#  time.sleep(.6)


# the main game function
def game():
    screen.nodelay(1)
    head = [1, 1]
    body = [head[:]]*5
    screen.border()
    direction = 0  # 0:right, 1:down, 2:left, 3:up
    foodmade = False
    foodmade1 = False
    bomb = False
    bomb2 = False
    bomb3 = False
    bomb4 = False
    bomb5 = False
    bomb6 = False
    gameover = False
    deadcell = body[-1][:]
    while not gameover:
        curses.noecho()
# place random food on screen
        while not foodmade:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' '):
                foodmade = True
                screen.addch(y, x, ord('$') |
                             curses.color_pair(3) | curses.A_BOLD)
        while not foodmade1 and len(body) > 14 and len(body) < 105:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' '):
                foodmade1 = True
                screen.addch(y, x, ord('$') |
                             curses.color_pair(3) | curses.A_BOLD)
# Place bombs on screen
        while not bomb and len(body) > 25:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' ') or ord('$') and screen.inch(y, x) != ord('#'):
                bomb = True
                screen.addch(y, x, '*', curses.color_pair(2))
        while not bomb2 and len(body) > 40:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' ') or ord('$') and screen.inch(y, x) != ord('#'):
                bomb2 = True
                screen.addch(y, x, '*', curses.color_pair(2))
        while not bomb3 and len(body) > 60:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' ') or ord('$') and screen.inch(y, x) != ord('#'):
                bomb3 = True
                screen.addch(y, x, '*', curses.color_pair(2))
        while not bomb4 and len(body) > 85:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' ') or ord('$') and screen.inch(y, x) != ord('#'):
                bomb4 = True
                screen.addch(y, x, '*', curses.color_pair(2))
        while not bomb5 and len(body) > 105:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' ') or ord('$'):
                bomb5 = True
                screen.addstr(y, x, '++', curses.color_pair(2))
        while not bomb6 and len(body) > 155:
            y, x = random.randrange(
                1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' ') or ord('$'):
                bomb6 = True
                screen.addstr(y, x, '||||', curses.color_pair(2))
# movement
        if deadcell not in body:
            screen.addch(deadcell[0], deadcell[1], ' ')

        screen.addch(head[0], head[1], ord('#'),
                     curses.color_pair(6) | curses.A_BOLD)
        action = screen.getch()

        if action == curses.KEY_UP and direction != 1:
            direction = 3
        elif action == curses.KEY_DOWN and direction != 3:
            direction = 1
        elif action == curses.KEY_LEFT and direction != 0:
            direction = 2
        elif action == curses.KEY_RIGHT and direction != 2:
            direction = 0

# directions
        if direction == 0:
            head[1] += 1

        elif direction == 2:
            head[1] -= 1
            # if head[1] < 1:
            #  head[1] = dims[1]-2
        elif direction == 3:
            head[0] -= 1
            # if head[0] < 1
            #  head[0] = dims[0]-2
        elif direction == 1:
            head[0] += 1
# These lines allow the snake to cross over the screen
        if direction == 0 and head[1] > dims[1]-2:
            head[1] = 1
        if direction == 2 and head[1] < 1:
            head[1] = dims[1]-2
        if direction == 3 and head[0] < 1:
            head[0] = dims[0]-2
        if direction == 1 and head[0] > dims[0]-2:
            head[0] = 1

# this makes dude a snake instead of a really long string
        deadcell = body[-1]
        for z in range(len(body)-1, 0, -1):
            body[z] = body[z-1][:]
# adding food on pickup
        body[0] = head[:]
        if screen.inch(head[0], head[1]) != ord(' '):
            if screen.inch(head[0], head[1]) == (ord('$') | curses.color_pair(3) | curses.A_BOLD):
                foodmade = False
                body.append(body[-1])
            elif screen.inch(head[0], head[1]) == (ord('$') | curses.color_pair(3) | curses.A_BOLD):
                foodmade1 = False
                body.append(body[-1])
            # elif action == ord('c'):
               # cheat()
            else:
                gameover = True

        # if head[1] > 50
        #  head[1] = 2
        screen.refresh()
        action = screen.getch()
        if len(body) < 16:
            time.sleep(.1)
        elif len(body) > 10 and len(body) < 26:
            time.sleep(.08)
# Baller Mode
        elif len(body) > 25 and len(body) < 31:
            foodmade1 = False
            time.sleep(.07)
        elif len(body) > 30 and len(body) < 66:
            foodmade1 = True
            foodmade = True
            time.sleep(.07)
        elif len(body) > 65 and len(body) < 81:
            time.sleep(.065)
# Bomb mode
        elif len(body) > 80 and len(body) < 82:
            time.sleep(.06)
            bomb3 = False
        elif len(body) > 81 and len(body) < 101:
            foodmade = True
            foodmade1 = True
            bomb3 = True
            time.sleep(.055)
# Baller Bomb mode
        elif len(body) > 100 and len(body) < 102:
            foodmade = False
            bomb2 = False
            time.sleep(.055)
        elif len(body) > 101 and len(body) < 121:
            foodmade = True
            bomb2 = True
            time.sleep(.052)
        elif len(body) > 120:
            time.sleep(.05)

# Gameover Menu

    screen.nodelay(0)
    screen.clear()
    selection = -1
    option = 0
    while selection < 0:
        graphics = [0]*3
        graphics[option] = curses.A_BOLD | curses.color_pair(3)
        screen.addstr(1, 30, '''
     __          _____  __           ___ 
    |__)/\|  |  |__|__)/__`|\ |/\|__/__  
    |__)~~\__|__|__|  \.__/| \/~~\  \___ 
                                         ''', curses.color_pair(3) | curses.A_BOLD | curses.A_REVERSE)
        screen.addstr(9, int(dims[1]/2-4), 'GAMEOVER',
                      curses.color_pair(1) | curses.A_BOLD)
       # screen.addstr(dims[0]/2+1, dims[1]/2-11, 'Please Select:', curses.color_pair(4))
        screen.addstr(int(dims[0]/2-1), int(dims[1]/2-9), 'You got ' +
                      str(len(body)-5) + ' points!', curses.color_pair(5))
        screen.addstr(int(dims[0]/2+2), int(dims[1]/2-4),
                      'New Game', graphics[0])
        screen.addstr(int(dims[0]/2+4), int(dims[1]/2-7),
                      'Return to Menu', graphics[1])
        screen.addstr(int(dims[0]/2+6), int(dims[1]/2-2), 'Exit', graphics[2])
        screen.refresh()
        action = screen.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 3
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 3
        elif action == ord('\n'):
            selection = option
    screen.clear()
    if selection == 0:
        game()
    if selection == 1:
        menu()
    if selection == 2:
        curses.endwin()


def menu():
    screen.nodelay(0)
    screen.clear()
    selection = -1
    option = 0
    while selection < 0:
        screen.addstr(int(dims[0]-1), int(dims[1]-6), 'v0.13', curses.A_BOLD)
        graphics = [0]*4
        graphics[option] = curses.color_pair(3) | curses.A_BOLD

        # optional title
        # screen.addstr(2, 1, '''
        #  .-.    . .       .-.      .
        #  |< .-. | | .-,.-.`-.-..-. |_,.-,
        #  '-'`-`-'-'-`'-'  `-' '`-`-' ``'-
        # ''', curses.color_pair(5) | curses.A_BOLD)

        screen.addstr(1, 30, '''
   __          _____  __           ___ 
  |__)/\|  |  |__|__)/__`|\ |/\|__/__  
  |__)~~\__|__|__|  \.__/| \/~~\  \___ 
                                       ''', curses.color_pair(3) | curses.A_BOLD | curses.A_REVERSE)
        screen.addstr(int(dims[0]/2-2), int(dims[1]/2-4), 'Play!', graphics[0])
        screen.addstr(int(dims[0]/2), int(dims[1]/2-5), 'Options', graphics[1])
        screen.addstr(int(dims[0]/2+2), int(dims[1]/2-5),
                      'Credits', graphics[2])
        screen.addstr(int(dims[0]/2+4), int(dims[1]/2-4), 'Exit?', graphics[3])
        screen.refresh()
        action = screen.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 4
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 4
        elif action == ord('\n'):
            selection = option
        # if  option = 3:
        #  graphics[3] = curses.color_pair(1)
    screen.clear()
    if selection == 0:
        game()
    if selection == 1:
        options()
    if selection == 2:
        credits()
    if selection == 3:
        curses.endwin()


def options():
    screen.clear()
    action = 0
    colors = 0
    speed = 0
    selection = -1
    while selection < 0:
        menulist = [0]*3
        menulist[colors] = curses.A_REVERSE
        screen.addstr(2, int(dims[1]/2-len('Options')+1),
                      'OPTIONS', curses.color_pair(1) | curses.A_BOLD)
        screen.addstr(int(dims[0]/3), int(dims[1]/4), 'Colors:', curses.A_BOLD)
        #screen.addstr(dims[0]/3+10-len(str(colors)), dims[1]/4, str(colors), menulist[:])
        screen.addstr(int(dims[0]-1), int(dims[1]-6), 'v0.12', curses.A_BOLD)

        screen.refresh()
        action = screen.getch()
        if action == curses.KEY_LEFT:
            colors = (colors - 1) % 3
        elif action == curses.KEY_RIGHT:
            colors = (colors + 1) % 3
        if action == ord('\n'):
            menu()


def credits():
    screen.clear()
    action = 0
    while action == 0:
        screen.addstr(int(dims[0]-1), int(dims[1]-6), 'v0.12', curses.A_BOLD)
        screen.addstr(int(dims[0]/2-2), int(dims[1]/2-17),
                      'Created and maintained by bertLz')
        screen.refresh()
        action = screen.getch()
        if action == ord('\n'):
            menu()


menu()
curses.endwin()
