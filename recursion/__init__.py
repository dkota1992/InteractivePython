import turtle

myTurtle = turtle.Turtle()
myScreen = turtle.Screen()

def drawSpiral(myTurtle,length):
    if length>0:
        myTurtle.forward(length)
        myTurtle.left(90)
        drawSpiral(myTurtle,length-10)
        
# drawSpiral(myTurtle,200)
# myScreen.exitonclick()

def tree(treeTurtle,branchlength):
    if branchlength>10:
        treeTurtle.forward(branchlength)
        treeTurtle.right(20)
        tree(treeTurtle,branchlength-5)

# def main():
#     treeTurtle = turtle.Turtle()
#     myScreen = turtle.Screen()
#     treeTurtle.left(90)
#     treeTurtle.up()
#     treeTurtle.backward(100)
#     treeTurtle.down()
#     treeTurtle.color("blue")
#     tree(treeTurtle,85)
def swap(array,pos1,pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp
    return array

def bubblesort(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            array = swap(array,i,i+1)
    return array
        
from required import Queue
import random

def main():
    a = Queue()
    a.add(44)
    a.add(53)
    a.add(22)
    a.add(51)
    a.add(500)
    a.add(53)
    print(a.next())
    print(a.report())
    
if __name__ == '__main__':
    main()
    
        