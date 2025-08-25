#----------------------------------------------------------------------------------------------------------#
#                                   H A C K A P Y  :  P O D
#----------------------------------------------------------------------------------------------------------#
# Pod : Piece Of Data
# A structure to generatize interactation between game actors (Master and player)
#----------------------------------------------------------------------------------------------------------#

class Podable():
    # Podable:
    def asPod(self):
        # Should return self as a Pod instance
        assert "Should be implemented" == None
        
    def fromPod(self):
        # Should rebuild self from a Pod instance
        assert "Should be implemented" == None
      
class Pod(Podable):
    def __init__( self, aPod= None ):
        if aPod is not None :
            self._label= aPod.label()
            self._integers= aPod.integers()
            self._values= aPod.values()
            self._children= aPod.children()
        else :
            self._label= ""
            self._integers= []
            self._values= []
            self._children= []

    # Accessor:
    def label(self):
        return self._label
    
    def integers(self):
        return self._integers
    def integer(self, i=1):
        return self.integers()[i-1]
    def numberOfIntegers(self):
        return len( self.integers() )
    
    def values(self):
        return self._values
    def value(self, i=1):
        return self.values()[i-1]
    def numberOfValues(self):
        return len( self.values() )
    
    def children(self):
        return self._children
    def child(self, i=1):
        return self.children()[i-1]
    def numberOfChildren(self):
        return len( self.children() )

    # Construction:
    def setLabel( self, aLabel ):
        self._label= aLabel
        return self
    
    def setIntegers( self, aList ):
        self._integers= aList
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
    
    # Initialization:
    def initialize(self, label= "", integers= [], values= [], children= []):
        self._label= label
        self._integers= [elt for elt in integers ]
        self._values= [elt for elt in values ]
        self._children= [elt for elt in children ]
        return self
    
    def fromDico(self, aDico):
        self._label= aDico["label"]
        self._integers= aDico["integers"]
        self._values= aDico["values"]
        self._children= aDico["children"]
        return self

    # transfrom:
    def asDico(self, aDico):
        aDico= { "label": self._label }
        aDico["integers"]= self._integers
        aDico["values"]= self._values
        aDico["children"]= self._children
        return aDico

    # Podable:
    def asPod( self ):
        return Pod().initialize(
            self.label(),
            self.integers(),
            self.values(),
            [ child.asPod() for child in self.children() ]
        )
    
    def fromPod( self, aPod ):
        self._label= aPod.label()
        self._integers= aPod.integers()
        self._values= aPod.values()
        self._children= [ Pod().fromPod(child) for child in aPod.children() ]
        return self

    # Comparison:
    def __eq__(self, another):
        return (
            self._label == another.label()
            and self._integers == another.integers()
            and self._values == another.values()
            and self._children == another.children()
        )
    
    # String :
    def __str__(self):
        return self.str(0)

    def str(self, ident=0):
        # Get pod info
        label= self.label()
        integers= self.integers()
        values= self.values()

        # Print
        msg= label+":"
        if len( integers ) > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in integers ) + "]"
        if len( values ) > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in values ) + "]"
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
