import math
from ..pylib import pod

class Shape(pod.PodInterface):

    # Initialization Destruction:
    def __init__( self, type= 0, size= 1.0 ):

        self._type= type
        self.setShapeSquare( size )

    # Accessor:
    def type(self):
        return self._type

    def envelope(self):
        return self._envs
    
    def box(self):
        env= self.envelope()
        minx, miny= env[0]
        maxx, maxy= env[0]
        for x, y in env[1:] :
            if x < minx :
                minx= x
            if y < miny :
                miny= y
            if x > maxx :
                maxx= x
            if y > maxy :
                maxy= y
        return [(minx, miny), (maxx, maxy)]

    # list accessors: 
    def envelopeAsList(self):
        l= []
        for x, y in self._envs :
            l+= [x, y]
        return l

    # Construction:
    def setType(self, t):
        self._type= t
        return self
    
    def setCenter(self, x, y):
        self._center= (x, y)
        return self
    
    def setEnveloppe( self, envelopes ):
        self._envs= list(envelopes)
        return self
    
    # Shape Construction:
    def setShapeSquare(self, size):
        demi= size*0.5
        self._envs= [
            ( -demi, +demi ),
            ( +demi, +demi ),
            ( +demi, -demi ),
            ( -demi, -demi )
        ]
        return self

    def setShapeRegular(self, size, numberOfVertex= 6):
        radius= size*0.5
        self._envs= []
        delta= math.pi/(numberOfVertex/2)
        angle= math.pi  - delta/2
        delta= math.pi/(numberOfVertex/2)
        for i in range(numberOfVertex) :
            self._envs.append( (
                math.cos(angle)*radius,
                math.sin(angle)*radius
            ) )
            angle+= -delta
        return self
    
    # to str
    def str(self, name="Shape", ident=0): 
        # Myself :
        s= f"{name}-{self.type()}/{len(self._envs)} " 
        s+= str( [(round(x, 2), round(y, 2)) for x, y in self.box()] )
        return s
    
    def __str__(self): 
        return self.str()
    
    # Pod interface:
    def asPod(self, family="Shape"):
        tilePod= pod.Pod(
            family,
            "",
            [self.type()],
            self.envelopeAsList()
        )
        return tilePod
    
    def fromPod(self, aPod):
        # Convert flags:
        self._type= aPod.flag(1)
        # Convert Values:
        vals= aPod.values()
        xs= [ vals[i] for i in range( 0, len(vals), 2 ) ]
        ys= [ vals[i] for i in range( 1, len(vals), 2 ) ]
        self._envs= [ (x, y) for x, y in zip(xs, ys) ]
        return self
