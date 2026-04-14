#----------------------------------------------------------------------------------------------------------#
#                                   H A C K A P Y  :  P O D
#----------------------------------------------------------------------------------------------------------#
# DataTree : Piece Of Data
# A structure to generatize interactation between game actors (Master and player)
#----------------------------------------------------------------------------------------------------------#

import re, struct

class Head():
    LABEL= 0
    LABEL_NONE= 0
    LABEL_ONE= 1
    LABEL_FEW= 2
    LABEL_LONG= 3

    DIGIT= 1
    DIGIT_NONE= 0
    DIGIT_FEW_OCT= 1
    DIGIT_FEW_SHORT= 2
    DIGIT_ALOT_INT= 3

    VALUE= 2
    VALUE_NONE= 0
    VALUE_FEW_FLOAT= 1
    VALUE_ALOT_FLOAT= 2
    VALUE_ALOT_DOUBLE= 3

    TREE= 3
    TREE_LEAF= 0
    TREE_BINARY= 1
    TREE_FEW= 2
    TREE_ALOT= 3

    p_pos= [6, 4, 2, 0 ]
    p_mask= [0b11000000, 0b00110000, 0b00001100, 0b00000011 ]

    p_struct= [
        ["", "s", "s", "s"], ["", "B", "h", "i"], ["", "f", "f", "d"], ["", "", "", ""]        
    ]
    p_bits= [
        [0, 1, 1, 1], [0, 1, 2, 4], [0, 4, 4, 8], [0, 0, 0, 0]        
    ]

    def __init__(self, int256= 255):
        assert( 0 <= int256 and int256 < 256 )
        self._states= [
            (int256&self.p_mask[i]) >> self.p_pos[i]
            for i in range(4)
        ]

    def get(self, id):
        return self._states[id]
    
    def set(self, id, value):
        self._states[id]= value
        return self

    def toInt(self):
        bint= 0b0
        for i in range(4) :
            bint = bint | ( self._states[i] << Head.p_pos[i] )
        return bint

    def toStr(self):
        return '0b' + format(self.toInt(), '08b')
    
class DataTreeInterface():
    
    # DataTreeAbs:
    def asDataTree(self):
        # Should return self as a DataTree instance
        assert "Should be implemented" == None
        
    def fromDataTree(self):
        # Should rebuild self from a DataTree instance
        assert "Should be implemented" == None
      
class DataTree():
    def __init__(self, label= "DataTree", digits= [], values= [], children= []):
        assert type(label) == type("")
        self.initialize(label, digits, values, children)
    
    # Initialization:
    def initialize(self, label= "DataTree", digits= [], values= [], children= []):
        self._label= label
        self._digits= [elt for elt in digits ]
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
    
    # Corrections :
    def round(self, precision, recursif=True):
        for i in range(self.numberOfValues()):
            self._values[i]= round( self._values[i], precision )
        if recursif :
            for c in self.children() :
                c.round(precision, recursif)
    
    # Meta :
    def isDigitSigned(self) :
        negatif= False
        for d in self.digits() :
            negatif= negatif or (d < 0)
        return negatif
    
    def isDigitLargeRange(self) :
        return False
    
    def isValuesPrecise(self) :
        return False

    # header :
    def head(self):
        return self.header()
    
    def header(self):
        head= Head()

        labelSize= len(self.label())
        childrenSize= self.numberOfChildren()
        digitsSize= self.numberOfDigits()
        valuesSize= self.numberOfValues()
        
        # Tree :
        if childrenSize == 0 :
           head.set(Head.TREE, Head.TREE_LEAF)
        elif childrenSize == 2 :
           head.set(Head.TREE, Head.TREE_BINARY)
        elif childrenSize < 256 :
           head.set(Head.TREE, Head.TREE_FEW)
        else :
           head.set(Head.TREE, Head.TREE_ALOT)

        # Label :
        if labelSize == 0 :
           head.set(Head.LABEL, Head.LABEL_NONE)
        elif labelSize == 1 :
           head.set(Head.LABEL, Head.LABEL_ONE)
        elif labelSize < 256 :
           head.set(Head.LABEL, Head.LABEL_FEW)
        else :
           head.set(Head.LABEL, Head.LABEL_LONG)
        
        # Digit :
        if digitsSize == 0 :
           head.set(Head.DIGIT, Head.DIGIT_NONE)
        elif digitsSize < 256 :
           head.set(Head.DIGIT, Head.DIGIT_FEW_SHORT)
        else :
           head.set(Head.DIGIT, Head.DIGIT_ALOT_INT)
        
        # Values :
        if valuesSize == 0 :
           head.set(Head.VALUE, Head.VALUE_NONE)
        elif valuesSize < 256 :
           head.set(Head.VALUE, Head.VALUE_FEW_FLOAT)
        else :
           head.set(Head.VALUE, Head.VALUE_ALOT_FLOAT)
        
        return head


    # Serializer :
    def dump(self):
        return self.dump_bin()

    def load(self, buffer):
        return self.load_bin(buffer)

    def dump_txt(self):
        # Element to dumps:
        label= self.label()
        digits= self.digits()
        values= self.values()
        children= self.children()

        labelSize= len(label)
        intSize= len( digits )
        valuesSize= len( values )
        childrenSize= len( self.children() )

        buffer= f'{labelSize} {intSize} {valuesSize} {childrenSize} : {label}'
        if intSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in digits )
        if valuesSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in values )
        
        for c in children :
            buffer+= "\n" + c.dump_txt()
        
        return buffer

    def load_txt(self, buffer):
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

    def dump_bin(self):
        # Element to dumps:
        label= self.label()
        digits= self.digits()
        values= self.values()
        children= self.children()

        labelSize= len(label)
        digitsSize= len( digits )
        valuesSize= len( values )
        childrenSize= len( self.children() )

        buffer= bytearray( struct.pack( '=B', self.head().toInt() ) )
        buffer+= struct.pack('=H', labelSize)
        buffer+= struct.pack('=H', digitsSize)
        buffer+= struct.pack('=H', valuesSize)
        buffer+= struct.pack('=H', childrenSize)

        if labelSize > 0 :
            buffer += struct.pack( f"<{labelSize}s", bytes( self.label(), "utf8" ) )
        for i in range(1, digitsSize+1) :
            buffer += struct.pack( '=h', self.digit(i) )
        for i in range(1, valuesSize+1) :
            buffer += struct.pack('=f', self.value(i) )
        
        for c in children :
            buffer+= c.dump_bin()

        return buffer

    def load_bin(self, buffer):
        self.load_bin_deep( buffer, 0 )
        return self
    
    def load_bin_deep(self, buffer, ib):
        head, = struct.unpack( "=B", buffer[ib:ib+1] )
        ib+=1
        labelSize, digitsSize, valuesSize, childrenSize= struct.unpack( "=HHHH", buffer[ib:ib+8] )
        ib+= 8

        # Get words:
        self._label= buffer[ib:ib+labelSize].decode('utf-8')
        ib+= labelSize
        ibb= ib + digitsSize*2
        self._digits= [
            up[0]
            for up in struct.iter_unpack( "=h", buffer[ib:ibb] )
        ]
        ib= ibb
        ibb= ib + valuesSize*4
        self._values= [
            up[0]
            for up in struct.iter_unpack( "=f", buffer[ib:ibb] )
        ]
        ib= ibb

        for _ in range( childrenSize ) :
            child= DataTree()
            ib= child.load_bin_deep( buffer, ib )
            self._children.append( child )
        
        return ib
    
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
            if decomp[1] == '' :
                self.initialize( decomp[0] )
            else :
                self.initialize( decomp[0], [ int(v) for v in decomp[1].split(" ") ] )

        else :
            self.initialize( aString )
        
        return self
    
