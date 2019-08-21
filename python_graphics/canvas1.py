from graphics import*
import math
import time
from PIL import Image

'''
This project shows the relation between maths and graphic pattern.
written by Harish Dalal.
'''
win = GraphWin("new canvas" , 700 , 700)
win.setBackground(color_rgb(0,0,0))

def main(radius , dist , total_points , ratio):
    center = 350
    cen = Circle(Point(center,center),2)
    cen.setFill(color_rgb(255,255,153))
    cen.draw(win)
    rad_inner = 20
    List = []
    angle = 0
    flag = False
    for i in range(total_points):
        if(flag):
            temp1 = rad_inner * (math.sin(angle))
            temp2 = temp1+center
            if(temp2>=center):
                rad_inner = rad_inner + dist
                y = rad_inner * (math.sin(angle))
                p2 = y+center
                flag = False
            else:
                y = rad_inner * (math.sin(angle))
                p2 = y+center
                flag = False
        else:
            y = rad_inner * (math.sin(angle))
            p2 = y+center
        x = rad_inner * (math.cos(angle))
        p1 = x+center
        #print("",p1,p2)#for printing out location of each file
        List.append(Circle(Point(p1,p2),radius))
        List[i].setFill(color_rgb(255,255,153))
        List[i].draw(win)
        angle = angle + (2*math.pi/ratio)
        '''
        commenting out below line will make the pattern change after eveery loop
        making pattern unstable but making it look beautiful
        '''
        #ratio = ratio+0.000001
        if(p2<center-.00000001):
            flag = True
    '''
    To save all the images as a png on local system need to be little changed
    for using it
    
    win.postscript(file = str(ratio)+".eps")
    imgNew = Image.open(str(ratio)+".eps")
    imgNew.convert("RGBA")
    imgNew.thumbnail((2000,2000), Image.ANTIALIAS)
    imgNew.save(str(ratio)+'.png', quality=90)
    '''
    time.sleep(1)
    '''
    for cleaing the output and redrawing it again between different variables
    doing recursion
    
    win.clear()
    main(radius , dist , ratio + 0.01)#This values to be changed if want to
    win.close()
    main(radius , dist , ratio+.015335)
    '''
    
radius = 2                  #changing radius
dist = .1                   #changing distance between two layers
total_points = 5000         #Total number of points to be made.
ratio = (1+math.sqrt(5))/2  #golden ratio. Can be changed if want to
main(radius , dist , total_points , ratio)

