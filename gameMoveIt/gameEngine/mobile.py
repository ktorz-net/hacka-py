"""
Test - MoveIt Robot Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg

class Mobile(hg.PodInterface):
    TYPE_ROBOT= 0
    TYPE_HUMAN= 1

    #Construction: 
    def __init__(self, number, x=0, y=0, type= TYPE_ROBOT):
        self._num= number
        self._x= x
        self._y= y
        self._goalx= x
        self._goaly= y
        self._goalOk= False
        self._error= 0.0
        self._type= type
    
    # Pod interface:
    def asPod(self, family="Robot"):
        return hg.Pod( family, str(self._num),
            [self._x, self._y, self._goalx, self._goaly, int(self._goalOk)]
            )
    
    def fromPod(self, aPod):
        self._num= int(aPod.status())
        self._x= aPod.flag(1)
        self._y= aPod.flag(2)
        self._goalx= aPod.flag(3)
        self._goaly= aPod.flag(4)
        self._goalOk= bool(aPod.flag(5))

    # Accessor: 
    def number(self): 
        return self._num
    
    def x(self):
        return self._x
    
    def y(self):
        return self._y

    def position(self):
        return self._x, self._y
    
    def goal(self):
        return self._goalx, self._goaly
    
    def isGoalSatisfied(self):
        return self._goalOk

    def error(self):
        return self._error
    
    def isRobot(self):
        return self._type == Mobile.TYPE_ROBOT
    
    def isHuman(self):
        return self._type == Mobile.TYPE_HUMAN
    
    
    # Modifier
    def setPosition(self, x, y):
        self._x= x
        self._y= y
    
    def setGoal(self, x, y):
        self._goalx= x
        self._goaly= y
        self._goalOk= False

    def updateGoalSatifaction(self):
        self._goalOk= self._goalOk or ( self.position() == self.goal() )
        return self._goalOk
        
    def setError(self, aValue):
        assert( -0.1 < aValue and aValue <= 1.1 )
        self._error= aValue
    
    def setRobot(self):
        self._type= Mobile.TYPE_ROBOT

    def setHuman(self):
        self._type= Mobile.TYPE_HUMAN

    # str
    def __str__(self):
        s= f"Robot-{self._num}[on({self._x}, {self._y}), "
        s+= f"goal({self._goalx}, {self._goaly})-{self._goalOk}, "
        s+= f"error({self._error})]"
        return s
