import turtle               #import turtle module
gg=turtle.Turtle()          #Create a new turtle object
turtle.bgcolor("black")     #Set the color of the background to black.
gg.color("#f65314")         #Set the initial color of the turtle’s pen to #f65314.
gg.pensize(1)               #Set the size of the turtle's pen to 1.


#defining the function which will draw the logo.
def microsoft():

 gg.begin_fill()        #The starting point for filling 1st square.
 gg.backward(150)       #moves the pen in the backward direction by 150 units.
 gg.left(90)            #turn the turtle neck by 90 degrees toward left.
 gg.forward(150)        #moves the pen in the forward direction by 150 units.
 gg.right(90)           #turn the turtle neck by 90 degrees toward right.
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.end_fill()          #Closing point of 1st square and fill with the current fill color.
 
 #for adding the space between the squares.
 gg.color("#000")
 gg.left(90)
 gg.forward(15)

 #for creating 2nd square.
 gg.begin_fill()
 gg.color("#7cbb00")
 gg.left(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.end_fill()

 #for adding the space between the squares.
 gg.color("#000")
 gg.left(90)
 gg.forward(15)

 #for creating 3rd square.
 gg.begin_fill()
 gg.color("#ffbb00")
 gg.left(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.end_fill()

 #for adding the space between the squares.
 gg.color("#000")
 gg.left(90)
 gg.forward(15)

 #for creating 4th square.
 gg.begin_fill()
 gg.color("#00a1f1")
 gg.left(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.right(90)
 gg.forward(150)
 gg.end_fill()
 gg.left(180)
 gg.forward(150)


microsoft()         #calling the function.
gg.hideturtle()
turtle.done()       #stop execution.



















