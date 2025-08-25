#----------------------------------------------------------------------------------------------------------#
#                                   H A C K A P Y  :  P O D
#----------------------------------------------------------------------------------------------------------#
# Pod : Piece Of Data, but limied (max: 3x256 variables)
# And so, efficiently serializable...
#----------------------------------------------------------------------------------------------------------#

from .pod import Pod

class Pod256(Pod):
    def __init__( self, aPod= None ):
        super( Pod256, self ).__init__(aPod)
        self.castChildrenAsPod256()
        #assert self.is256()
    
    # Construction: 
    def castChildrenAsPod256(self):
        self._children= [ Pod256( child )
                         for child in self.children() ]
        return self
    
    # Serializer :
    def dump(self):
        return self.dump_str()

    def dump_str(self):
        # Element to dumps:
        label= self.label()
        integers= self.integers()
        values= self.values()
        children= self.children()

        labelSize= len(label)
        intSize= len( integers )
        valuesSize= len( values )
        childrenSize= len( self.children() )

        buffer= f'{labelSize} {intSize} {valuesSize} {childrenSize} : {label}'
        if intSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in integers )
        if valuesSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in values )
        for c in children :
            buffer+= "\n" + c.dump_str()
        return buffer

    def load(self, buffer):
        return self.load_str(buffer)
    
    def load_str(self, buffer):
        if type(buffer) == str :
            buffer= buffer.splitlines()
        self.loadLines_str( buffer )
        return self
    
    def loadLines_str(self, buffer):
        # current line:
        line= buffer.pop(0)

        print( f"> load line : {line}" )

        # Get meta data (type, name and structure sizes):
        metas, data= tuple( line.split(' : ') )
        metas= [ int(x) for x in metas.split(' ') ]
        labelSize, intsSize, valuesSize, childrenSize= tuple( metas )
        
        self._label= data[:labelSize]

        elements= data[labelSize+1:]
        if elements == '' :
            elements= []
        else : 
            elements= elements.split(" ")

        assert( len(elements) == intsSize + valuesSize )

        # Get words:
        self._integers= [ int(i) for i in elements[:intsSize] ]
        self._values= [ float(f) for f in elements[intsSize:] ]
        
        # load children
        self.clear()
        for iChild in range(childrenSize) :
            child= Pod256()
            buffer= child.loadLines_str(buffer)
            self._children.append( child )

        return buffer
