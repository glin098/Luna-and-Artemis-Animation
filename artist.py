from cs1graphics import *
from time import sleep

canvas = Canvas(600, 500, 'powderblue', 'Luna + Artemis: Hide and Go Seek')

#floor
ground = Rectangle(600, 200, Point(300, 400))
ground.setFillColor('pink')
ground.setBorderColor('pink')
ground.setDepth(65)
canvas.add(ground)

#tree
bush = Circle(50, Point(90,150))
bush.setFillColor('orchid')
bush.setBorderWidth(0)
canvas.add(bush)
bush2 = bush.clone()
bush2.setFillColor('violet')
bush2.scale(1.3)
bush2.move(65,-22)
bush2.setBorderWidth(0)
canvas.add(bush2)
bush3 = bush.clone()
bush3.setFillColor('plum')
bush3.move(0,-50)
bush3.setDepth(75)
bush3.setBorderWidth(0)
canvas.add(bush3)
tree = Polygon(Point(130, 350), Point(100,350), Point(100, 200), Point(50, 150), Point(60,150), Point(100,185), Point(120,120), Point(130,120), Point(120, 185), Point(180,180), Point(190,190), Point(120,195))
tree.setFillColor('wheat')
tree.setBorderWidth(0)
canvas.add(tree)

#sun
sun = Circle(80, Point(300,300))
sun.setFillColor('gold')
sun.setBorderColor('moccasin')
sun.setBorderWidth(10)
sun.setDepth(75)
canvas.add(sun)

#--------------------artemis--------------------------------------------------
art = Layer()

#artemis body
tail = Ellipse(15,60, Point(350,260))
tail.setFillColor('white')
tail.rotate(40)
art.add(tail)

body = Ellipse(50,90, Point(300, 265)) 
body.setFillColor('white')
art.add(body)

leg1 = Ellipse(15,55, Point(275,290))
leg1.setFillColor('white')
leg1.rotate(-20)
art.add(leg1)
leg2 = leg1.clone()
leg2.move(50,0)
leg2.rotate(40)
art.add(leg2)
leg3 = Ellipse(15, 70, Point(290,280))
leg3.setFillColor('white')
leg4 = leg3.clone()
leg4.move(20,0)
art.add(leg3)
art.add(leg4)

paw1 = Ellipse(18,8, Point(278,315))
paw1.setFillColor('white')
art.add(paw1)
paw2 = Ellipse(18,8, Point(322,315))
paw2.setFillColor('white')
art.add(paw2)

#artemis head
rightear = Polygon(Point(270,200), Point(280, 150), Point(290, 180))
rightear.setFillColor('white')
art.add(rightear)
rightear1 = rightear.clone()
rightear1.scale(0.8)
rightear1.setFillColor('pink')
rightear1.move(3, 0)
art.add(rightear1)
leftear = rightear.clone()
leftear.flip()
leftear.move(60,0)
art.add(leftear)
leftear1 = rightear1.clone()
leftear1.flip()
leftear1.move(55,0)
art.add(leftear1)

head = Circle(30, Point(300, 200))
head.setFillColor('white')
art.add(head)

#ornament moon for head
orna = Circle(5, Point(300,180))
orna.setFillColor('goldenrod')
orna.setBorderWidth(0)
art.add(orna)
orna1 = Circle(3, Point(300, 177)) #to give the ornament a crescent shape
orna1.setFillColor('white')
orna1.setBorderWidth(0)
art.add(orna1)

lefteye = Layer()
eye1 = Ellipse(10,16, Point(289, 198)) #transparent interior bc artemis is white
lefteye.add(eye1)

iris1 = Ellipse(8,15, Point(289, 200))
iris1.setFillColor('royalblue')
iris1.scale(0.8)
lefteye.add(iris1)

dot1 = Circle(2, Point(290,199))
dot1.setFillColor('white')
lefteye.add(dot1)
art.add(lefteye)

righteye = lefteye.clone()
righteye.move(22, 0)
art.add(righteye)

whiskers = Layer()
w1 = Path(Point(300, 211), Point(275, 208))
w2 = Path(Point(300, 211), Point(280,215))
w3 = Path(Point(300, 211), Point(325, 208))
w4 = Path(Point(300, 211), Point(320, 215))
whiskers.add(w1)
whiskers.add(w2)
whiskers.add(w3)
whiskers.add(w4)
art.add(whiskers)

nose = Ellipse(5,5, Point(300, 211))
nose.setFillColor('pink')
art.add(nose)

#to give artemis natural looking arms
arm_cover = Rectangle(35,20, Point(300,250))
arm_cover.setFillColor('white')
arm_cover.setBorderColor('white')
art.add(arm_cover)

collar = Rectangle(30,5, Point(300,230))
collar.setFillColor('grey')
art.add(collar)
bell = Circle(3, Point(300,235))
bell.setFillColor('yellow')
art.add(bell)

#--------------------------luna---------------------------------------------
luna = Layer()

#luna body
tail = Ellipse(15,60, Point(350,260))
tail.setFillColor('dimgrey')
tail.rotate(40)
luna.add(tail)

body = Ellipse(50,90, Point(300, 265)) 
body.setFillColor('dimgrey')
luna.add(body)

leg1 = Ellipse(15,55, Point(275,290))
leg1.setFillColor('dimgrey')
leg1.rotate(-20)
luna.add(leg1)
leg2 = leg1.clone()
leg2.move(50,0)
leg2.rotate(40)
luna.add(leg2)
leg3 = Ellipse(15, 70, Point(290,280))
leg3.setFillColor('dimgrey')
leg4 = leg3.clone()
leg4.move(20,0)
luna.add(leg3)
luna.add(leg4)

paw1 = Ellipse(18,8, Point(278,315))
paw1.setFillColor('dimgrey')
luna.add(paw1)
paw2 = Ellipse(18,8, Point(322,315))
paw2.setFillColor('dimgrey')
luna.add(paw2)

#luna head
rightear = Polygon(Point(270,200), Point(280, 150), Point(290, 180))
rightear.setFillColor('dimgrey')
luna.add(rightear)
rightear1 = rightear.clone()
rightear1.scale(0.8)
rightear1.setFillColor('maroon')
rightear1.move(3, 0)
luna.add(rightear1)

leftear = rightear.clone()
leftear.flip()
leftear.move(60,0)
luna.add(leftear)
leftear1 = rightear1.clone()
leftear1.flip()
leftear1.move(55,0)
luna.add(leftear1)

head = Circle(30, Point(300, 200))
head.setFillColor('dimgrey')
luna.add(head)

#ornament for forehead
orna = Circle(5, Point(300,180))
orna.setFillColor('goldenrod')
orna.setBorderWidth(0)
luna.add(orna)
orna1 = Circle(3, Point(300, 178)) #crescent shape
orna1.setFillColor('dimgrey')
orna1.setBorderWidth(0)
luna.add(orna1)

lefteye = Layer()
eye1 = Ellipse(10,16, Point(289, 198))
eye1.setFillColor('white')
lefteye.add(eye1)

iris1 = Ellipse(8,15, Point(289, 200))
iris1.setFillColor('mediumaquamarine')
iris1.scale(0.8)
lefteye.add(iris1)

dot1 = Circle(2, Point(290,199))
dot1.setFillColor('white')
lefteye.add(dot1)
luna.add(lefteye)

righteye = lefteye.clone()
righteye.move(22, 0)
luna.add(righteye)

whiskers = Layer()
w1 = Path(Point(300, 211), Point(275, 208))
w2 = Path(Point(300, 211), Point(280,215))
w3 = Path(Point(300, 211), Point(325, 208))
w4 = Path(Point(300, 211), Point(320, 215))
whiskers.add(w1)
whiskers.add(w2)
whiskers.add(w3)
whiskers.add(w4)
luna.add(whiskers)

nose = Ellipse(5,5, Point(300, 211))
nose.setFillColor('maroon')
luna.add(nose)

#to give natural looking arms
arm_cover = Rectangle(35,20, Point(300,250))
arm_cover.setFillColor('dimgrey')
arm_cover.setBorderColor('dimgrey')
luna.add(arm_cover)

collar = Rectangle(30,5, Point(300,230))
collar.setFillColor('red')
luna.add(collar)
bell = Circle(3, Point(300,235))
bell.setFillColor('yellow')
luna.add(bell)

luna.move(400,100)
luna.scale(.7)

#--------------------------animation/dialouge-------------------------------
canvas.add(art)
art.move(400,300)
sleep(4)
art.move(-100,0)
sleep(2)
art.move(-100,0)
sleep(2)
art.move(-200,-50) #artemis popping her head out

message = Text('Try and find me, Luna!', 15, Point(300,380))
canvas.add(message)
sleep(2)
canvas.remove(message)

art.move(-100, -150)
sleep(1)
art.scale(0.8)
art.setDepth(65)
art.move(-30,-6) #artemis moves behind tree
canvas.add(luna) #luna comes into frame
sleep(1.5)
luna.move(-50,0)
sleep(1)
luna.move(-10,0)
sleep(1)
luna.move(-10,0)
sleep(1)
luna.move(-10,0)
sleep(1)

message = Text('Luna won\'t be able\n to find me here...', 9, Point(200,220))
canvas.add(message)
sleep(2)
canvas.remove(message)
               
message = Text('I can see you behind\nthat tree, Artemis...', 10, Point(500,190))
canvas.add(message)
sleep(3)
canvas.remove(message)

art.setDepth(0)
message = Text('Well, try and catch me then~', 10, Point(210,220))
canvas.add(message)
sleep(3)
canvas.remove(message)
luna.scale(1.1)
art.move(-50,0)
luna.move(-150,0)
sleep(.5)
luna.move(-150,0)
sleep(.3)
luna.move(-140,0)

message = Text('*boop*', 8, Point(80,200))
canvas.add(message)
sleep(3)
canvas.remove(message)

art.move(-20,0)
sleep(.5)
art.move(-30,0)
sleep(.5)
canvas.remove(art)

message = Text('Hey! Where are you going?\nI caught you! Get back here!', 9, Point(80,200))
canvas.add(message)
sleep(3)
canvas.remove(message)
luna.move(-50,0)
sleep(1)
canvas.remove(luna)

message = Text('THE END :D', 10, Point(300,250))
canvas.add(message)








