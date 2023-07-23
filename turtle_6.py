import turtle
bob=turtle.Turtle()
bob.getscreen().bgcolor("blue") # background colour
# for i in range(5):
 # bob.forward(100)
  #bob.left(216)
  
def star(turle,size):
    if size<=10:
        return
    else:
       for i in range(5):
        turtle.forward(size)
        star(turtle,size/2)
        turtle.left(216)


star(bob,100)
















turtle.done()