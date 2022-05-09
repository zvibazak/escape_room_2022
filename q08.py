import turtle

SIZE=20

#COLORS
GREEN   = 1 * SIZE
RED     = 2 * SIZE
YELLOW  = 3 * SIZE
ORANGE  = 4 * SIZE
GREY    = 5 * SIZE
BLUE    = 6 * SIZE
AZURE   = 7 * SIZE

def turn(direction, color):
  if direction=='r':
    turtle.right(90)
  else:
    turtle.left(90)
  turtle.forward(color)
  
#1
turn('l', RED)
turn('r', RED)
turn('l', GREEN)
turn('r', GREEN)
turn('l', RED)
turn('r', GREEN)
turn('r', GREEN)
turn('l', GREEN)

#2
turn('l', GREEN)
turn('r', GREEN)
turn('r', GREEN)
turn('l', GREEN)
turn('l', GREEN)
turn('r', GREEN)
turn('r', RED)
turn('r', ORANGE)

#3
turn('l', GREEN)
turn('r', GREEN)
turn('l', YELLOW)
turn('l', GREEN)
turn('r', GREEN)
turn('l', AZURE)
turn('r', YELLOW)
turn('r', GREEN)

#4
turn('r', RED)
turn('l', GREEN)
turn('l', BLUE)
turn('r', GREEN)
turn('r', RED)
turn('l', GREEN)
turn('r', RED)
turn('l', YELLOW)

#4
turn('l', RED)
turn('r', GREEN)
turn('l', RED)
turn('r', GREEN)
turn('r', GREY)
turn('l', GREEN)
turn('r', ORANGE)
turn('l', GREEN)

turtle.Screen().exitonclick()
