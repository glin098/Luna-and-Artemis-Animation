from cs1graphics import *
from time import sleep

class Luna(Layer):
    '''
    The Luna creates a graphical class that represents the cartoon cat, Luna,
    from Sailor Moon. The user will be able to change the body color of Luna,
    set the color of the ornament on Luna's head, change the collar color,
    wink an eye, and speak.
    '''
    def __init__(self, color = 'white'):
        '''
        Creates a new instance of Luna. The default body color of Luna is white.
        Newly contructed layers have a reference point of (0,0).
        '''
        super().__init__() # calling the parent constructor
        #tail
        self._tail = Ellipse(15,60, Point(50,5))
        self._tail.setFillColor(color)
        self._tail.rotate(40)
        self.add(self._tail)
        #body
        self._body = Ellipse(50,90) 
        self._body.setFillColor(color)
        self.add(self._body)
        #legs and paws
        self._leg1 = Ellipse(15,55, Point(-25,25))
        self._leg1.setFillColor(color)
        self._leg1.rotate(-20)
        self.add(self._leg1)
        self._leg2 = self._leg1.clone()
        self._leg2.move(50,0)
        self._leg2.rotate(40)
        self.add(self._leg2)
        self._leg3 = Ellipse(15, 70, Point(-10,15))
        self._leg3.setFillColor(color)
        self.add(self._leg3)
        self._leg4 = self._leg3.clone()
        self._leg4.move(20,0)
        self.add(self._leg4)
        self._paw1 = Ellipse(18,8, Point(22,50))
        self._paw1.setFillColor(color)
        self.add(self._paw1)
        self._paw2 = Ellipse(18,8, Point(-22,50))
        self._paw2.setFillColor(color)
        self.add(self._paw2)
        #head
        self._rightear = Polygon(Point(-30,-65), Point(-20, -115), Point(-10, -85))
        self._rightear.setFillColor(color)
        self.add(self._rightear)
        self._rightear1 = self._rightear.clone()
        self._rightear1.scale(0.8)
        self._rightear1.setFillColor('pink')
        self._rightear1.move(3, 0)
        self.add(self._rightear1)
        self._leftear = self._rightear.clone()
        self._leftear.flip()
        self._leftear.move(60,0)
        self.add(self._leftear)
        self._leftear1 = self._rightear1.clone()
        self._leftear1.flip()
        self._leftear1.move(55,0)
        self.add(self._leftear1)
        self._head = Circle(30, Point(0, -65))
        self._head.setFillColor(color)
        self.add(self._head)
        #ornament
        self._orna = Circle(5, Point(0,-85))
        self._orna.setFillColor('goldenrod')
        self._orna.setBorderWidth(0)
        self.add(self._orna)
        self._orna1 = Circle(3, Point(0, -88)) 
        self._orna1.setFillColor(color)
        self._orna1.setBorderWidth(0)
        self.add(self._orna1)
        #eyes - opened
        self._lefteye = Layer()
        self._eye1 = Ellipse(10,16, Point(-11, -67)) 
        self._lefteye.add(self._eye1)
        self._iris1 = Ellipse(8,15, Point(-11, -65))
        self._iris1.setFillColor('royalblue')
        self._iris1.scale(0.8)
        self._lefteye.add(self._iris1)
        self._dot1 = Circle(2, Point(-10,-66))
        self._dot1.setFillColor(color)
        self._lefteye.add(self._dot1)
        self.add(self._lefteye)
        self._righteye = self._lefteye.clone()
        self._righteye.move(22, 0)
        self.add(self._righteye)
        #eyes - closed
        self._closedEyes = Layer()
        leftEyeClosed = Rectangle(10,2, Point(-11, -67))
        leftEyeClosed.setFillColor('black')
        self._closedEyes.add(leftEyeClosed)
        self._closedEyes.setDepth(60)
        self.add(self._closedEyes)
        self._closedP = False
        #whiskers
        self._whiskers = Layer()
        self._w1 = Path(Point(0, -54), Point(-25, -57))
        self._w2 = Path(Point(0, -54), Point(-20,-50))
        self._w3 = Path(Point(0, -54), Point(25, -57))
        self._w4 = Path(Point(0, -54), Point(20, -50))
        self._whiskers.add(self._w1)
        self._whiskers.add(self._w2)
        self._whiskers.add(self._w3)
        self._whiskers.add(self._w4)
        self.add(self._whiskers)
        #nose
        self._nose = Ellipse(5,5, Point(0, -54))
        self._nose.setFillColor('pink')
        self.add(self._nose)
        #to make arms look natural
        self._arm_cover = Rectangle(35,20, Point(0,-15))
        self._arm_cover.setFillColor(color)
        self._arm_cover.setBorderColor(color)
        self.add(self._arm_cover)
        #collar
        self._collar = Rectangle(30,5, Point(0,-35))
        self._collar.setFillColor('grey')
        self.add(self._collar)
        self._bell = Circle(3, Point(0,-30))
        self._bell.setFillColor('yellow')
        self.add(self._bell)
        #message
        self._txt = Text('',12, Point(0, -160))
        self.add(self._txt)
        #mouth
        self._mouth = Spline()
        self._mouth.addPoint(Point(-7,-48))
        self._mouth.addPoint(Point(0,-40))
        self._mouth.addPoint(Point(7,-48))
        self._mouth.adjustReference(7,1)
        self.add(self._mouth)
        self._smiling = True

    def setColor(self, color):
        '''
        Change the body color of Luna only. Other attributes such as eyes, ornament
        color, ear color, etc, will remain unchanged.
        '''
        self._tail.setFillColor(color)
        self._body.setFillColor(color)
        self._leg1.setFillColor(color)
        self._leg2.setFillColor(color)
        self._leg3.setFillColor(color)
        self._leg4.setFillColor(color)
        self._paw1.setFillColor(color)
        self._paw2.setFillColor(color)
        self._rightear.setFillColor(color)
        self._leftear.setFillColor(color)
        self._head.setFillColor(color)
        self._arm_cover.setFillColor(color)

    def setOrnaColor(self, ornaColor):
        '''
        Change the ornament color that is on Luna's forehead.
        '''
        self._orna.setFillColor(ornaColor)

    def setCollarColor(self, collarColor):
        '''
        Change the collar color of Luna
        '''
        self._collar.setFillColor(collarColor)

    def speak(self, message):
        self._txt.setMessage(message)

    def openEyesWink(self):
        '''
        Opens the left eye to animate Luna winking.
        '''
        if self._closedP:
            self._lefteye.setDepth(40)
            self._closedEyes.setDepth(60)
            self._closedP = False

    def closedEyesWink(self):
        '''
        Closes the left eye to animate Luna winking.
        '''
        if not self._closedP:
            self._lefteye.setDepth(60)
            self._closedEyes.setDepth(40)
            self._closedP = True
            
    def smile(self):
        if not self._smiling:
            self._mouth.rotate(180)
            self._smiling = True

    def frown(self):
        if self._smiling:
            self._mouth.rotate(180)
            self._smiling = False

    


if __name__ == '__main__':
    paper = Canvas(600, 500, 'lightcyan')
    #ground
    ground = Rectangle(600, 200, Point(300, 400))
    ground.setFillColor('plum')
    ground.setBorderColor('palegreen')
    ground.setDepth(65)
    paper.add(ground)
    
    #cats
    luna1 = Luna()
    luna1.moveTo(300,250)
    paper.add(luna1)
    luna1.speak('Hello')
    luna1.closedEyesWink()
    sleep(2)
    luna1.openEyesWink()
    sleep(.5)
    luna1.speak('My name is Luna.\nThese are my children.\nPlease watch over them while I am gone.')
    sleep(3)
    luna1.speak('')
    sleep(2)
    luna1.move(610,510)
    
    luna2 = Luna('grey')
    luna2.moveTo(240, 300)
    luna2.scale(.65)
    luna2.setOrnaColor('red')
    luna2.setCollarColor('black')
    luna2.speak('  meow\nmeow meow')
    paper.add(luna2)
    
    luna3 = Luna('mistyrose')
    luna3.moveTo(400, 300)
    luna3.scale(.8)
    luna3.setOrnaColor('violet')
    luna3.setCollarColor('gold')
    luna3.speak('meow   meow\n      meow')
    paper.add(luna3)

    luna4 = Luna('lightcyan')
    luna4.moveTo(180,310)
    luna4.scale(.7)
    luna4.setOrnaColor('darkcyan')
    luna4.setCollarColor('mediumaquamarine')
    luna4.speak('   meow\nmeow')
    paper.add(luna4)

    #animation
    sleep(3)
    luna3.move(50,0)
    sleep(1)
    luna3.move(100,0)
    sleep(1)
    luna3.move(100,0)
    luna2.frown()
    luna2.move(-50,0)
    sleep(2)
    luna2.move(-50,0)
    sleep(1)
    luna2.move(-200,0)
    luna4.frown()
    luna4.speak('I wanna go play too...')
    sleep(2)
    luna4.speak('')
    luna4.smile()
    luna4.move(-50,0)
    sleep(2)
    luna4.move(-50,0)
    sleep(1)
    luna4.move(-200,0)
    sleep(2)
    luna1.move(-610,-510)
    luna1.speak('I am back...Where is everyone?')
    sleep(1)
    luna1.frown()
    luna1.speak('You had one job :(')
    sleep(2)
    luna1.move(0,50)
    luna1.scale(3)
    
    
    
