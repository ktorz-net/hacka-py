
class Robot:
    #Construction: 
    def __init__(self, number):
        self._num= number
        self._goalx= 0
        self._goaly= 0

    def setGoal(self, x, y):
        self._goalx= x
        self._goaly= y
    
    #Accessor: 
    def number(self): 
        return self._num
    
    def goal(self):
        return self._goalx, self._goaly