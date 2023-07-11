from . import pieceOfData as pod

class Cell():

    # Constructor:

    def __init__( self, num= 0 ):
        self._num= num
        self._adjacencies= []
        self._pieces= []
    
    # accessor:
    
    def number(self):
        return self._num
    
    def adjacencies(self):
        return self._adjacencies
    
    def edges(self):
        num= self.number()
        return [ [num, i] for i in self.adjacencies() ] 

    def pieces(self) :
        return self._pieces

    # Construction:

    def connect(self, iTo):
        if iTo not in self._adjacencies :
            self._adjacencies.append(iTo)
            self._adjacencies.sort()
        return self

    # Pod interface:
    
    def asPod(self, name="Cell"):
        return pod.Pod( f"{name}-{self.number()}", [self.number()]+self.adjacencies(), [] )
    
    def fromPod(self, aPod):
        attrs= aPod.attributes()
        self._num= attrs[0]
        self._adjacencies= attrs[1:]
        return self

class Board():

    # Constructor:

    def __init__( self, size= 0 ):
        self._cells= [ Cell(i) for i in range(size+1) ]
        self._size= size
        self._ite= 1

    # Pod accessor:
    
    def size(self):
        return self._size

    def isCell(self, iCell):
        return 0 < iCell and iCell <= self.size()
    
    def cells(self):
        return self._cells[1:]

    def cell(self, iCell):
        return self._cells[iCell]

    def edges(self):
        edgeList= []
        for c in self.cells() :
            edgeList+= c.edges()
        return edgeList

    def isEdge(self, iFrom, iTo):
        return iTo in self.edgesFrom(iFrom)
    
    # Construction:

    def connect(self, iFrom, iTo):
        self.cell(iFrom).connect(iTo)
        return self

    def connectAll(self, aList):
        for anElt in aList :
            self.connect( anElt[0], anElt[1] )

    # Pod interface:

    def asPod(self, name= "Board"):
        bPod= pod.Pod( name )
        for c in self.cells() :
            bPod.append( c.asPod() )
        return bPod
    
    def fromPod(self, aPod):
        cells= aPod.children()
        self.__init__( len(cells) )
        for c in cells :
            self.cell( c.attribute(1) ).fromPod( c )
        return self

    # Iterator over board cells

    def __iter__(self):
        self._ite = 1
        return self

    def __next__(self):
        if self._ite <= self.numberOfCells() :
            cell = self.cell( self._ite )
            edges= self.edgesFrom( self._ite )
            self._ite += 1
            return cell, edges
        else:
            raise StopIteration

    def iCell(self):
        return self._ite-1