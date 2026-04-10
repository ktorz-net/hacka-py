#----------------------------------------------------------------------------------------------------------#
#                                   H A C K A P Y  :  P O D
#----------------------------------------------------------------------------------------------------------#
# DataTree : Piece Of Data
# A structure to generatize interactation between game actors (Master and player)
#----------------------------------------------------------------------------------------------------------#

import re

class DataTreeInterface():
    # DataTreeAbs:
    def asDataTree(self):
        # Should return self as a DataTree instance
        assert "Should be implemented" == None
        
    def fromDataTree(self):
        # Should rebuild self from a DataTree instance
        assert "Should be implemented" == None
      
class DataTree():
    def __init__(self, label= "DataTree", integers= [], values= [], children= []):
        assert type(label) == type("")
        self.initialize(label, integers, values, children)
    
    # Initialization:
    def initialize(self, label= "DataTree", integers= [], values= [], children= []):
        self._label= label
        self._digits= [elt for elt in integers ]
        self._values= [elt for elt in values ]
        self._children= [elt for elt in children ]
        return self
    
    def fromDico(self, aDico):
        self._label= aDico["label"]
        self._digits= aDico["digits"]
        self._values= aDico["values"]
        self._children= aDico["children"]
        return self

    def fromDataTree( self, aDataTree ):
        self._label= aDataTree.label()
        self._digits= aDataTree.digits()
        self._values= aDataTree.values()
        self._children= [ DataTree().fromDataTree(child) for child in aDataTree.children() ]
        return self

    # Morphing:
    def asDataTree( self ):
        return DataTree().initialize(
            self.label(),
            self.digits(),
            self.values(),
            [ child.asDataTree() for child in self.children() ]
        )

    def asDico(self):
        aDico= { "label": self._label }
        aDico["digits"]= self._digits
        aDico["values"]= self._values
        aDico["children"]= self._children
        return aDico

    # Accessor:
    def label(self):
        return self._label
    
    def digits(self):
        return self._digits
    def digit(self, i=1):
        return self._digits[i-1]
    def numberOfDigits(self):
        return len( self._digits )
    
    def values(self):
        return self._values
    def value(self, i=1):
        return self._values[i-1]
    def numberOfValues(self):
        return len( self._values )
    
    def children(self):
        return self._children
    def child(self, i=1):
        return self._children[i-1]
    def numberOfChildren(self):
        return len( self._children )

    # Construction:
    def setLabel( self, aLabel ):
        self._label= aLabel
        return self
    
    def setIntegers( self, aList ):
        self._digits= aList
        return self
    
    def setValues( self, aList ):
        self._values= aList
        return self
    
    def setChildren( self, aList ):
        self._children= aList
        return self
    
    # Collection:
    def clear(self):
        self._children= []
        return self
    
    def append(self, aChild):
        self._children.append( aChild )
        return self

    def pop(self, i=1):
        self._children.pop(i-1)

    # Comparison:
    def __eq__(self, another):
        return (
            self.label() == another.label()
            and self.digits() == another.digits()
            and self.values() == another.values()
            and self.children() == another.children()
        )
    
    # String :
    def __str__(self):
        return self.str(0)

    def str(self, ident=0):
        # Get datatree info
        label= self.label()
        integers= self.digits()
        values= self.values()

        # Print self
        msg= label+" :"
        for v in integers :
            msg+= ' '+ str(v)
        msg+= " :"
        for v in values :
            msg+= ' '+ str(v)
        
        # Print children
        msg+= self.strChildren( ident )
        
        return msg

    def strChildren( self, ident ):
        msg= ""
        newLine= '\n'
        for i in range(ident) :
            newLine+= '  '
        newLine+= '- '
        
        for c in self.children() :
            msg+= newLine + c.str(ident+1)
        return msg

    def decode( self, aString ):
        mFull= re.search("^(.*):( [0-9]+)* ?:( [0-9]*.?[0-9]+)*", aString)
        mInts= re.search("^(.*):( [0-9]+)*", aString)
        
        if mFull :
            datatreeSring= mFull.group()
            decomp= re.search("^(.*):(.*):(.*)", datatreeSring)
            decomp= [grp.strip() for grp in decomp.groups()]

            intergers= []
            if decomp[1] != '' :
                intergers= [ int(v) for v in decomp[1].split(" ") ]

            values= []
            if decomp[2] != '' :
                values= [ float(v) for v in decomp[2].split(" ") ]
            
            self.initialize( decomp[0], intergers, values )

        elif mInts : 
            datatreeSring= mInts.group()
            decomp= re.search("^(.*):(.*)", datatreeSring)
            decomp= [grp.strip() for grp in decomp.groups()]
            print( f"> {decomp}" )
            if decomp[1] == '' :
                self.initialize( decomp[0] )
            else :
                self.initialize( decomp[0], [ int(v) for v in decomp[1].split(" ") ] )

        else :
            self.initialize( aString )
        
        return self
    
    # Serializer :
    def dump(self):
        return self.dump_str()

    def dump_str(self):
        # Element to dumps:
        label= self.label()
        integers= self.digits()
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
        self._digits= [ int(i) for i in elements[:intsSize] ]
        self._values= [ float(f) for f in elements[intsSize:] ]
        
        # load children
        self.clear()
        for iChild in range(childrenSize) :
            child= DataTree()
            buffer= child.loadLines_str(buffer)
            self._children.append( child )

        return buffer
