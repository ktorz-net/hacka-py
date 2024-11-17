from ..core import pod

from . import tile

Tile= tile.Tile

class Board(pod.PodInterface):

    # Constructor:

    def __init__( self, size= 0 ):
        self._tiles= [ Tile(i) for i in range(size+1) ]
        self._size= size
        self._ite= 1

    # Pod accessor:
    
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
    
    # Construction:

    def connect(self, iFrom, iTo):
        self.tile(iFrom).connect(iTo)
        return self

    def connectAll(self, aList):
        for anElt in aList :
            self.connect( anElt[0], anElt[1] )

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
        self._ite = 1
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