from ..pylib import pod
from .tile import Tile

class Board( pod.PodInterface ):

    # Constructor:
    def __init__( self, size= 0, tileSize=0.9, separator=0.1 ):
        self.initializeLine( size, tileSize, separator )
        self._ite= 1

    # Accessor:
    def size(self):
        return self._size

    def isTile(self, iTile):
        return 0 < iTile and iTile <= self.size()
    
    def tiles(self):
        return self._tiles[1:]

    def tile(self, iCell):
        return self._tiles[iCell]

    def edges(self):
        edgeList= []
        for t in self.tiles() :
            edgeList+= [ (t.number(), neibor) for neibor in t.adjacencies() ]
        return edgeList

    def isEdge(self, iFrom, iTo):
        return iTo in self.tile(iFrom).adjacencies()
    
    def box(self):
        if self.size() == 0 :
            return [ (0.0, 0.0), (0.0, 0.0) ]
        tiles= self.tiles()
        box= tBox= [ [x, y] for x, y in tiles[0].box() ]
        for t in tiles[1:] :
            tBox= [ [x, y] for x, y in t.box() ]
            if tBox[0][0] < box[0][0] :
                box[0][0] = tBox[0][0]
            if tBox[0][1] < box[0][1] :
                box[0][1] = tBox[0][1]
            if tBox[1][0] > box[1][0] :
                box[1][0] = tBox[1][0]
            if tBox[1][1] > box[1][1] :
                box[1][1] = tBox[1][1]

        return [ (box[0][0], box[0][1]), (box[1][0], box[1][1]) ]

    # Construction:
    def initializeLine( self, size, tileSize= 1.0, separation=0.1 ):
        dist= tileSize+separation
        self._tiles= [None] + [
            Tile(i+1, 0, (dist*i, 0.0), tileSize )
            for i in range(size)
        ]
        self._size= size
        return self
    
    def initializeSquares( self, matrix, tileSize= 1.0, separation=0.1 ):
        dist= tileSize+separation
        self._tiles= [None]
        
        iTile= 0
        maxLine= len(matrix)-1
        for i in range( len(matrix) ) :
            for j in range( len(matrix[i]) ) :
                if matrix[i][j] >= 0 : 
                    iTile+= 1
                    tile= Tile(
                        iTile, matrix[i][j],
                        ( dist*j, dist*(maxLine-i) ),
                        tileSize
                    )
                    self._tiles.append(tile)
                    matrix[i][j]= iTile
        self._size= iTile
        return self

    def addTile( self, aTile ):
        aTile.setNumber( len(self._tiles) )
        self._tiles.append( aTile )
        return aTile.number()

    def connect(self, iFrom, iTo):
        self.tile(iFrom).connect(iTo)
        return self

    def connectAll(self, aList):
        for anElt in aList :
            self.connect( anElt[0], anElt[1] )

    def connectAllCondition(self, conditionFromTo=lambda tfrom, tto : True, conditionFrom=lambda tfrom : True ):
        size= self.size()
        for i in range(1, size) :
            tili= self.tile(i)
            if conditionFrom( tili ) :
                for j in range(i+1, size+1) :
                    tilj= self.tile(j)
                    if conditionFromTo( tili, tilj ): # :
                       self.connect( i, j )

    # Pod interface:
    def asPod(self, family= "Board"):
        bPod= pod.Pod( family )
        for c in self.tiles() :
            bPod.append( c.asPod() )
        return bPod
    
    def fromPod(self, aPod):
        tiles= aPod.children()
        self.__init__( len(tiles) )
        for t in tiles :
            self.tile( t.flag(1) ).fromPod( t )
        return self

    # Iterator over board cells
    def __iter__(self):
        self._ite= 1
        return self

    def __next__(self):
        if self._ite <= self.size() :
            tile = self.tile( self._ite )
            edges= self.edgesFrom( self._ite )
            self._ite += 1
            return tile, edges
        else:
            raise StopIteration

    def iTile(self):
        return self._ite-1
    
    # string:
    def str(self, name="Board"):
        tileStrs =[]
        for t in self.tiles() :
            tileStrs.append( f"- {t}" )
            for piece in t.pieces() :
                tileStrs.append( f"  - {piece}" )
        return f"{name}:\n" + "\n".join( tileStrs )
    
    def __str__(self): 
        return self.str()