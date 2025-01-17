import math
from .shape import Shape
from ..pylib import pod

class Tile(Shape):

    # Initialization Destruction:
    def __init__( self, num= 0, type= 0, center= (0.0, 0.0), size= 1.0 ):
        self._num= num
        super().__init__(type, center, size)
        self._adjacencies= []
        self._pieces= []
    
    # Accessor:
    def number(self):
        return self._num

    def adjacencies(self):
        return self._adjacencies
    
    def pieces(self) :
        return self._pieces
    
    def piece(self, i=1) :
        return self._pieces[i-1]

    # Construction    
    def setNumber(self, i):
        self._num= i
        return self

    # Connection:
    def connect(self, iTo):
        if iTo not in self._adjacencies :
            self._adjacencies.append(iTo)
            self._adjacencies.sort()
        return self

    def connectAll( self, aList ):
        for iTo in aList :
            self.connect( iTo )
        return self
    
    # Piece managment
    def append(self, aPod ): 
        self._pieces.append( aPod )
        return self
    
    def addPiece(self, aPiece ): # Depreciated
        x, y= self.center()
        aPiece.setCenter(x, y)
        self._pieces.append( aPiece )
        return self
    
    def clear(self):
        self._pieces = []
        return self
    
    # Pod interface:
    def asPod(self, family="Tile"):
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
        self._type= flags[1]
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

    def piecesFromChildren(self, aListOfPod):
        self._pieces= aListOfPod
        return self

    # to str
    def str(self, name="Tile", ident=0): 
        # Myself :
        s= f"{name}-{self.number()}/{self.type()}"
        x, y = self._center
        x, y = round(x, 2), round(y, 2)
        s+= f" center: ({x}, {y})"
        s+= " adjs: "+ str(self._adjacencies)
        s+= f" pieces({ len(self.pieces()) })"
        return s
    
    def __str__(self): 
        return self.str()
    