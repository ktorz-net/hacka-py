import math
from ..pylib import pod

class Shape(pod.PodInterface):

    # Initialization Destruction:
    def __init__( self, num= 0, type= 0, center= (0.0, 0.0), size= 1.0 ):
        self._num= num
        self._type= type
        self.setShapeSquare( center, size )

    # Accessor:
    def number(self):
        return self._num
    
    def type(self):
        return self._type
    
    def center(self):
        return self._center

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
    def setNumber(self, i):
        self._num= i
        return self

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
    def setShapeSquare(self, center, size):
        demi= size*0.5
        x, y= center
        self._envs= [
            ( x-demi, y+demi ),
            ( x+demi, y+demi ),
            ( x+demi, y-demi ),
            ( x-demi, y-demi )
        ]
        self._center= center
        return self

    def setShapeRegular(self, center, size, numberOfVertex= 6):
        radius= size*0.5
        x, y= center
        self._envs= []
        delta= math.pi/(numberOfVertex/2)
        angle= math.pi  - delta/2
        delta= math.pi/(numberOfVertex/2)
        for i in range(numberOfVertex) :
            self._envs.append( (
                x+math.cos(angle)*radius,
                y+math.sin(angle)*radius
            ) )
            angle+= -delta
        self._center= center
        return self
    
    # Comparison :
    def centerDistance(self, another):
        x1, y1= self.center()
        x2, y2= another.center()
        dx= x2-x1
        dy= y2-y1
        return math.sqrt( dx*dx + dy*dy )

    # to str
    def str(self, name="Shape", ident=0): 
        # Myself :
        s= f"{name}-{self.number()}/{self.type()}"
        x, y = self._center
        x, y = round(x, 2), round(y, 2)
        s+= f" center: ({x}, {y})"
        return s
    
    def __str__(self): 
        return self.str()
    
    # Pod interface:
    def asPod(self, family="Shape"):
        tilePod= pod.Pod(
            family,
            "",
            [self.number(), self.type()] + self.adjacencies(),
            list( self.center() ) + self.envelopeAsList()
        )
        for p in self.pieces() :
            tilePod.append( p.asPod() )
        return tilePod
    
    def fromPod(self, aPod):
        # Convert flags:
        flags= aPod.flags()
        self._num= flags[0]
        self._stamp= flags[1]
        self._adjacencies= flags[2:]
        # Convert Values:
        vals= aPod.values()
        xs= [ vals[i] for i in range( 0, len(vals), 2 ) ]
        ys= [ vals[i] for i in range( 1, len(vals), 2 ) ]
        self._center= ( xs[0], ys[0] )
        self._envs= [ (x, y) for x, y in zip(xs[1:], ys[1:]) ]
        # Load pices:
        self.piecesFromChildren( aPod.children() )
        return self
